import os
import numpy as np
import signal

from genicam.genapi import EInterfaceType, EAccessMode, TimeoutException, OutOfRangeException
from genicam.gentl import GenericException as GenTL_GenericException
import harvesters

# Copy of ENUM from scape_toolbox::CCameraReturnCodes::CODES
SUCCESS = 0
UNKNOWN = 1
TIMEOUT = 2
TRIGGER_NODE_NOT_WO = 3
EMPTY_NAME = 4
GRPC_NOT_VALID = 5
NOT_CALIBRATED = 6

from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def set_3d_values_without_data_to_nan(input_array):
    # Turn into an array of 3D point arrays.
    temp_array = input_array.reshape(-1, 3).copy()
    # All arrays that is all zero.
    all_zero_condition = np.all(temp_array == 0, axis=1)
    # Make all those NaN values
    temp_array[all_zero_condition] = [np.nan, np.nan, np.nan]
    # Flatten the array again
    return temp_array.flatten()

def fit_intensities_to_8bit(input_array):
    number_of_bins = np.min([np.max(input_array), 4096])
    percentile_95_value = np.percentile(input_array, 95)

    # In which bin does the 95th percentile recide. Only really needed if
    # the resolution of the input is above 12bits
    if number_of_bins == 4096:
        _, bins = np.histogram(input_array, number_of_bins)
        percentile_95_bin = np.digitize(percentile_95_value, bins) - 1
        scaling_factor = 255 / percentile_95_bin
    else:
        scaling_factor = 255 / int(percentile_95_value)

    scaled_input_array = input_array * scaling_factor
    scaled_input_array = np.clip(scaled_input_array, 0, 255)
    scaled_input_array = scaled_input_array.astype(int)

    return scaled_input_array


@timeit
def acquire(device, features):
    global TRIGGER_SOFTWARE, POINTCLOUD_DATA_INDEX, MONO_DATA_INDEX, CONVERSION_FACTOR
    trigger_node = features.get_node(TRIGGER_SOFTWARE)
    access_mode = trigger_node.get_access_mode()

    if EAccessMode(access_mode) == EAccessMode.WO:
        trigger_node.execute()
    else:
        print("Trigger method is not callable")
        print("Trigger is: " + str(EAccessMode(access_mode)))
    #Fetch a frame with a max timeout of 10 seconds
    buffer = device.fetch(timeout=10)
    # Grab component data
    components = buffer.payload.components
    print("Got the following components")
    print(components)
    print("End of components")
    pointcloud_data = components[POINTCLOUD_DATA_INDEX].data
    mono_texture_data = components[MONO_DATA_INDEX].data

    mono_texture_data = fit_intensities_to_8bit(mono_texture_data)
    pointcloud_data = set_3d_values_without_data_to_nan(
            pointcloud_data)
    pointcloud_data = pointcloud_data * CONVERSION_FACTOR

    print(f"Recieved {len(pointcloud_data)} point pointcloud ")
    print(f"Recieved {len(mono_texture_data)} pixel mono texture ")
    buffer.queue()

@timeit
def SetSettings(features):
    node = features.get_node("SinglePatternExposure")
    print(f"Current Value {node.value}")
    print(f"Max Value {node.max}")
    print(f"Min Value {node.min}")
    print(f"Setting Value to {20}")
    node.value = 20


################## Settings to be used #####################
CTI_FILE = "C:\\Program Files\\Photoneo\\PhoXiControl-1.10.0\\API\\bin\\photoneo.cti"
SERIAL_NUMBER = "[PhoXi3DScan]-(UserExamples-Mark_Scans2)"
TRIGGER_SOFTWARE = "TriggerFrame"

POINTCLOUD_DATA_INDEX = 2
MONO_DATA_INDEX = 0
CONVERSION_FACTOR = 0.001 # The Conversion ratio from scanner units to meters eg. mm to m is 0.001
################## Settings to be used #####################

def main(args=None):
    from harvesters.core import Harvester
    harvester = Harvester()
    harvester.add_file(CTI_FILE,check_existence=True,check_validity=True)
    harvester.update()
    device = harvester.create(
        {'serial_number': SERIAL_NUMBER})

    features = device.remote_device.node_map
    SetSettings(features)

    device.start()
    print("Starting acqusition")
    while (True):
        acquire(device,features)


if __name__ == '__main__':
    main()
