# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Ainstec
else:
    import _Ainstec

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Ainstec.delete_SwigPyIterator

    def value(self):
        return _Ainstec.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _Ainstec.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _Ainstec.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _Ainstec.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _Ainstec.SwigPyIterator_equal(self, x)

    def copy(self):
        return _Ainstec.SwigPyIterator_copy(self)

    def next(self):
        return _Ainstec.SwigPyIterator_next(self)

    def __next__(self):
        return _Ainstec.SwigPyIterator___next__(self)

    def previous(self):
        return _Ainstec.SwigPyIterator_previous(self)

    def advance(self, n):
        return _Ainstec.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _Ainstec.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _Ainstec.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _Ainstec.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _Ainstec.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _Ainstec.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _Ainstec.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Ainstec:
_Ainstec.SwigPyIterator_swigregister(SwigPyIterator)

class CameraInfoVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _Ainstec.CameraInfoVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Ainstec.CameraInfoVector___nonzero__(self)

    def __bool__(self):
        return _Ainstec.CameraInfoVector___bool__(self)

    def __len__(self):
        return _Ainstec.CameraInfoVector___len__(self)

    def __getslice__(self, i, j):
        return _Ainstec.CameraInfoVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Ainstec.CameraInfoVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Ainstec.CameraInfoVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Ainstec.CameraInfoVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Ainstec.CameraInfoVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Ainstec.CameraInfoVector___setitem__(self, *args)

    def pop(self):
        return _Ainstec.CameraInfoVector_pop(self)

    def append(self, x):
        return _Ainstec.CameraInfoVector_append(self, x)

    def empty(self):
        return _Ainstec.CameraInfoVector_empty(self)

    def size(self):
        return _Ainstec.CameraInfoVector_size(self)

    def swap(self, v):
        return _Ainstec.CameraInfoVector_swap(self, v)

    def begin(self):
        return _Ainstec.CameraInfoVector_begin(self)

    def end(self):
        return _Ainstec.CameraInfoVector_end(self)

    def rbegin(self):
        return _Ainstec.CameraInfoVector_rbegin(self)

    def rend(self):
        return _Ainstec.CameraInfoVector_rend(self)

    def clear(self):
        return _Ainstec.CameraInfoVector_clear(self)

    def get_allocator(self):
        return _Ainstec.CameraInfoVector_get_allocator(self)

    def pop_back(self):
        return _Ainstec.CameraInfoVector_pop_back(self)

    def erase(self, *args):
        return _Ainstec.CameraInfoVector_erase(self, *args)

    def __init__(self, *args):
        _Ainstec.CameraInfoVector_swiginit(self, _Ainstec.new_CameraInfoVector(*args))

    def push_back(self, x):
        return _Ainstec.CameraInfoVector_push_back(self, x)

    def front(self):
        return _Ainstec.CameraInfoVector_front(self)

    def back(self):
        return _Ainstec.CameraInfoVector_back(self)

    def assign(self, n, x):
        return _Ainstec.CameraInfoVector_assign(self, n, x)

    def resize(self, *args):
        return _Ainstec.CameraInfoVector_resize(self, *args)

    def insert(self, *args):
        return _Ainstec.CameraInfoVector_insert(self, *args)

    def reserve(self, n):
        return _Ainstec.CameraInfoVector_reserve(self, n)

    def capacity(self):
        return _Ainstec.CameraInfoVector_capacity(self)
    __swig_destroy__ = _Ainstec.delete_CameraInfoVector

# Register CameraInfoVector in _Ainstec:
_Ainstec.CameraInfoVector_swigregister(CameraInfoVector)

class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _Ainstec.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Ainstec.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _Ainstec.DoubleVector___bool__(self)

    def __len__(self):
        return _Ainstec.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _Ainstec.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Ainstec.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Ainstec.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Ainstec.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Ainstec.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Ainstec.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _Ainstec.DoubleVector_pop(self)

    def append(self, x):
        return _Ainstec.DoubleVector_append(self, x)

    def empty(self):
        return _Ainstec.DoubleVector_empty(self)

    def size(self):
        return _Ainstec.DoubleVector_size(self)

    def swap(self, v):
        return _Ainstec.DoubleVector_swap(self, v)

    def begin(self):
        return _Ainstec.DoubleVector_begin(self)

    def end(self):
        return _Ainstec.DoubleVector_end(self)

    def rbegin(self):
        return _Ainstec.DoubleVector_rbegin(self)

    def rend(self):
        return _Ainstec.DoubleVector_rend(self)

    def clear(self):
        return _Ainstec.DoubleVector_clear(self)

    def get_allocator(self):
        return _Ainstec.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _Ainstec.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _Ainstec.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _Ainstec.DoubleVector_swiginit(self, _Ainstec.new_DoubleVector(*args))

    def push_back(self, x):
        return _Ainstec.DoubleVector_push_back(self, x)

    def front(self):
        return _Ainstec.DoubleVector_front(self)

    def back(self):
        return _Ainstec.DoubleVector_back(self)

    def assign(self, n, x):
        return _Ainstec.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _Ainstec.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _Ainstec.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _Ainstec.DoubleVector_reserve(self, n)

    def capacity(self):
        return _Ainstec.DoubleVector_capacity(self)
    __swig_destroy__ = _Ainstec.delete_DoubleVector

# Register DoubleVector in _Ainstec:
_Ainstec.DoubleVector_swigregister(DoubleVector)

class StringVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _Ainstec.StringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Ainstec.StringVector___nonzero__(self)

    def __bool__(self):
        return _Ainstec.StringVector___bool__(self)

    def __len__(self):
        return _Ainstec.StringVector___len__(self)

    def __getslice__(self, i, j):
        return _Ainstec.StringVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Ainstec.StringVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Ainstec.StringVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Ainstec.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Ainstec.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Ainstec.StringVector___setitem__(self, *args)

    def pop(self):
        return _Ainstec.StringVector_pop(self)

    def append(self, x):
        return _Ainstec.StringVector_append(self, x)

    def empty(self):
        return _Ainstec.StringVector_empty(self)

    def size(self):
        return _Ainstec.StringVector_size(self)

    def swap(self, v):
        return _Ainstec.StringVector_swap(self, v)

    def begin(self):
        return _Ainstec.StringVector_begin(self)

    def end(self):
        return _Ainstec.StringVector_end(self)

    def rbegin(self):
        return _Ainstec.StringVector_rbegin(self)

    def rend(self):
        return _Ainstec.StringVector_rend(self)

    def clear(self):
        return _Ainstec.StringVector_clear(self)

    def get_allocator(self):
        return _Ainstec.StringVector_get_allocator(self)

    def pop_back(self):
        return _Ainstec.StringVector_pop_back(self)

    def erase(self, *args):
        return _Ainstec.StringVector_erase(self, *args)

    def __init__(self, *args):
        _Ainstec.StringVector_swiginit(self, _Ainstec.new_StringVector(*args))

    def push_back(self, x):
        return _Ainstec.StringVector_push_back(self, x)

    def front(self):
        return _Ainstec.StringVector_front(self)

    def back(self):
        return _Ainstec.StringVector_back(self)

    def assign(self, n, x):
        return _Ainstec.StringVector_assign(self, n, x)

    def resize(self, *args):
        return _Ainstec.StringVector_resize(self, *args)

    def insert(self, *args):
        return _Ainstec.StringVector_insert(self, *args)

    def reserve(self, n):
        return _Ainstec.StringVector_reserve(self, n)

    def capacity(self):
        return _Ainstec.StringVector_capacity(self)
    __swig_destroy__ = _Ainstec.delete_StringVector

# Register StringVector in _Ainstec:
_Ainstec.StringVector_swigregister(StringVector)

class Point3fVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _Ainstec.Point3fVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Ainstec.Point3fVector___nonzero__(self)

    def __bool__(self):
        return _Ainstec.Point3fVector___bool__(self)

    def __len__(self):
        return _Ainstec.Point3fVector___len__(self)

    def __getslice__(self, i, j):
        return _Ainstec.Point3fVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Ainstec.Point3fVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Ainstec.Point3fVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Ainstec.Point3fVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Ainstec.Point3fVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Ainstec.Point3fVector___setitem__(self, *args)

    def pop(self):
        return _Ainstec.Point3fVector_pop(self)

    def append(self, x):
        return _Ainstec.Point3fVector_append(self, x)

    def empty(self):
        return _Ainstec.Point3fVector_empty(self)

    def size(self):
        return _Ainstec.Point3fVector_size(self)

    def swap(self, v):
        return _Ainstec.Point3fVector_swap(self, v)

    def begin(self):
        return _Ainstec.Point3fVector_begin(self)

    def end(self):
        return _Ainstec.Point3fVector_end(self)

    def rbegin(self):
        return _Ainstec.Point3fVector_rbegin(self)

    def rend(self):
        return _Ainstec.Point3fVector_rend(self)

    def clear(self):
        return _Ainstec.Point3fVector_clear(self)

    def get_allocator(self):
        return _Ainstec.Point3fVector_get_allocator(self)

    def pop_back(self):
        return _Ainstec.Point3fVector_pop_back(self)

    def erase(self, *args):
        return _Ainstec.Point3fVector_erase(self, *args)

    def __init__(self, *args):
        _Ainstec.Point3fVector_swiginit(self, _Ainstec.new_Point3fVector(*args))

    def push_back(self, x):
        return _Ainstec.Point3fVector_push_back(self, x)

    def front(self):
        return _Ainstec.Point3fVector_front(self)

    def back(self):
        return _Ainstec.Point3fVector_back(self)

    def assign(self, n, x):
        return _Ainstec.Point3fVector_assign(self, n, x)

    def resize(self, *args):
        return _Ainstec.Point3fVector_resize(self, *args)

    def insert(self, *args):
        return _Ainstec.Point3fVector_insert(self, *args)

    def reserve(self, n):
        return _Ainstec.Point3fVector_reserve(self, n)

    def capacity(self):
        return _Ainstec.Point3fVector_capacity(self)
    __swig_destroy__ = _Ainstec.delete_Point3fVector

# Register Point3fVector in _Ainstec:
_Ainstec.Point3fVector_swigregister(Point3fVector)

class Point2fVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _Ainstec.Point2fVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Ainstec.Point2fVector___nonzero__(self)

    def __bool__(self):
        return _Ainstec.Point2fVector___bool__(self)

    def __len__(self):
        return _Ainstec.Point2fVector___len__(self)

    def __getslice__(self, i, j):
        return _Ainstec.Point2fVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Ainstec.Point2fVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Ainstec.Point2fVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Ainstec.Point2fVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Ainstec.Point2fVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Ainstec.Point2fVector___setitem__(self, *args)

    def pop(self):
        return _Ainstec.Point2fVector_pop(self)

    def append(self, x):
        return _Ainstec.Point2fVector_append(self, x)

    def empty(self):
        return _Ainstec.Point2fVector_empty(self)

    def size(self):
        return _Ainstec.Point2fVector_size(self)

    def swap(self, v):
        return _Ainstec.Point2fVector_swap(self, v)

    def begin(self):
        return _Ainstec.Point2fVector_begin(self)

    def end(self):
        return _Ainstec.Point2fVector_end(self)

    def rbegin(self):
        return _Ainstec.Point2fVector_rbegin(self)

    def rend(self):
        return _Ainstec.Point2fVector_rend(self)

    def clear(self):
        return _Ainstec.Point2fVector_clear(self)

    def get_allocator(self):
        return _Ainstec.Point2fVector_get_allocator(self)

    def pop_back(self):
        return _Ainstec.Point2fVector_pop_back(self)

    def erase(self, *args):
        return _Ainstec.Point2fVector_erase(self, *args)

    def __init__(self, *args):
        _Ainstec.Point2fVector_swiginit(self, _Ainstec.new_Point2fVector(*args))

    def push_back(self, x):
        return _Ainstec.Point2fVector_push_back(self, x)

    def front(self):
        return _Ainstec.Point2fVector_front(self)

    def back(self):
        return _Ainstec.Point2fVector_back(self)

    def assign(self, n, x):
        return _Ainstec.Point2fVector_assign(self, n, x)

    def resize(self, *args):
        return _Ainstec.Point2fVector_resize(self, *args)

    def insert(self, *args):
        return _Ainstec.Point2fVector_insert(self, *args)

    def reserve(self, n):
        return _Ainstec.Point2fVector_reserve(self, n)

    def capacity(self):
        return _Ainstec.Point2fVector_capacity(self)
    __swig_destroy__ = _Ainstec.delete_Point2fVector

# Register Point2fVector in _Ainstec:
_Ainstec.Point2fVector_swigregister(Point2fVector)

INFINITE = _Ainstec.INFINITE
DEPTH_MAP_ALIGN_RGB = _Ainstec.DEPTH_MAP_ALIGN_RGB
DEPTH_MAP_ALIGN_CAMERA = _Ainstec.DEPTH_MAP_ALIGN_CAMERA
BINOCULAR_RECONSTRUCTION = _Ainstec.BINOCULAR_RECONSTRUCTION
MONOCULAR_RECONSTRUCTION = _Ainstec.MONOCULAR_RECONSTRUCTION
CamPro = _Ainstec.CamPro
Camera_SoftTrigger = _Ainstec.Camera_SoftTrigger
Camera_GPIOTrigger = _Ainstec.Camera_GPIOTrigger
Camera_SoftSingleAsyncTrigger = _Ainstec.Camera_SoftSingleAsyncTrigger
ParamType_Begin = _Ainstec.ParamType_Begin
Capture_WorkMode = _Ainstec.Capture_WorkMode
Capture_Delay = _Ainstec.Capture_Delay
IR_Exposure = _Ainstec.IR_Exposure
IR_Gain = _Ainstec.IR_Gain
IR_LightSource = _Ainstec.IR_LightSource
IR_HDRCnt = _Ainstec.IR_HDRCnt
IR_HDRExposure2 = _Ainstec.IR_HDRExposure2
IR_HDRExposure3 = _Ainstec.IR_HDRExposure3
IR_PixelType = _Ainstec.IR_PixelType
Rgb_BrightnessSet = _Ainstec.Rgb_BrightnessSet
Rgb_Contrast = _Ainstec.Rgb_Contrast
Rgb_Saturation = _Ainstec.Rgb_Saturation
Rgb_Hue = _Ainstec.Rgb_Hue
Rgb_Gamma = _Ainstec.Rgb_Gamma
Rgb_WhiteBalanceTemperature = _Ainstec.Rgb_WhiteBalanceTemperature
Rgb_Sharpness = _Ainstec.Rgb_Sharpness
Rgb_BacklightCompensation = _Ainstec.Rgb_BacklightCompensation
Rgb_ExposureAbsolute = _Ainstec.Rgb_ExposureAbsolute
Rgb_WhiteBalanceTemperatureAuto = _Ainstec.Rgb_WhiteBalanceTemperatureAuto
Rgb_ExposureAuto = _Ainstec.Rgb_ExposureAuto
Mems_TriggerDelay = _Ainstec.Mems_TriggerDelay
Mems_LaserKValue = _Ainstec.Mems_LaserKValue
Algo_DepthMapType = _Ainstec.Algo_DepthMapType
Algo_DilateKsize = _Ainstec.Algo_DilateKsize
Algo_FillHole = _Ainstec.Algo_FillHole
Algo_KSize = _Ainstec.Algo_KSize
Algo_Sigma = _Ainstec.Algo_Sigma
Algo_Smooth = _Ainstec.Algo_Smooth
Algo_SmoothType = _Ainstec.Algo_SmoothType
Algo_ZfRangeMax = _Ainstec.Algo_ZfRangeMax
Algo_ZfRangeMin = _Ainstec.Algo_ZfRangeMin
Algo_WrapphaseType = _Ainstec.Algo_WrapphaseType
Algo_FilterType = _Ainstec.Algo_FilterType
Algo_TriThreshold = _Ainstec.Algo_TriThreshold
Algo_ShadowThreshold = _Ainstec.Algo_ShadowThreshold
Algo_GradNeedSerialNum = _Ainstec.Algo_GradNeedSerialNum
Algo_RecommendedZfRangeMax = _Ainstec.Algo_RecommendedZfRangeMax
Algo_RecommendedZfRangeMin = _Ainstec.Algo_RecommendedZfRangeMin
Algo_OutlierRemoval = _Ainstec.Algo_OutlierRemoval
Algo_XfRangeMax = _Ainstec.Algo_XfRangeMax
Algo_XfRangeMin = _Ainstec.Algo_XfRangeMin
Algo_YfRangeMax = _Ainstec.Algo_YfRangeMax
Algo_YfRangeMin = _Ainstec.Algo_YfRangeMin
Algo_ImageFilterType = _Ainstec.Algo_ImageFilterType
Algo_SmoothRadius = _Ainstec.Algo_SmoothRadius
Algo_ZSigma = _Ainstec.Algo_ZSigma
Algo_TextureMappingType = _Ainstec.Algo_TextureMappingType
Algo_LrCheck = _Ainstec.Algo_LrCheck
Algo_LrCheckThreshold = _Ainstec.Algo_LrCheckThreshold
ParamType_End = _Ainstec.ParamType_End
ParamType_Get_Offset = _Ainstec.ParamType_Get_Offset
class FrameInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    frameIndex = property(_Ainstec.FrameInfo_frameIndex_get, _Ainstec.FrameInfo_frameIndex_set)
    frameTimestamp = property(_Ainstec.FrameInfo_frameTimestamp_get, _Ainstec.FrameInfo_frameTimestamp_set)
    frameTotalDuration = property(_Ainstec.FrameInfo_frameTotalDuration_get, _Ainstec.FrameInfo_frameTotalDuration_set)
    frameAcquisitionDuration = property(_Ainstec.FrameInfo_frameAcquisitionDuration_get, _Ainstec.FrameInfo_frameAcquisitionDuration_set)
    frameComputationDuration = property(_Ainstec.FrameInfo_frameComputationDuration_get, _Ainstec.FrameInfo_frameComputationDuration_set)
    frameTransferDuration = property(_Ainstec.FrameInfo_frameTransferDuration_get, _Ainstec.FrameInfo_frameTransferDuration_set)

    def __init__(self):
        _Ainstec.FrameInfo_swiginit(self, _Ainstec.new_FrameInfo())
    __swig_destroy__ = _Ainstec.delete_FrameInfo

# Register FrameInfo in _Ainstec:
_Ainstec.FrameInfo_swigregister(FrameInfo)

class FrameData(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _Ainstec.delete_FrameData

    def __init__(self, *args):
        _Ainstec.FrameData_swiginit(self, _Ainstec.new_FrameData(*args))
    frameInfo = property(_Ainstec.FrameData_frameInfo_get, _Ainstec.FrameData_frameInfo_set)
    point3D = property(_Ainstec.FrameData_point3D_get, _Ainstec.FrameData_point3D_set)
    pointUV = property(_Ainstec.FrameData_pointUV_get, _Ainstec.FrameData_pointUV_set)
    triangleIndices = property(_Ainstec.FrameData_triangleIndices_get, _Ainstec.FrameData_triangleIndices_set)
    depthmap = property(_Ainstec.FrameData_depthmap_get, _Ainstec.FrameData_depthmap_set)
    normals = property(_Ainstec.FrameData_normals_get, _Ainstec.FrameData_normals_set)
    pointColor = property(_Ainstec.FrameData_pointColor_get, _Ainstec.FrameData_pointColor_set)
    texture = property(_Ainstec.FrameData_texture_get, _Ainstec.FrameData_texture_set)
    remapTexture = property(_Ainstec.FrameData_remapTexture_get, _Ainstec.FrameData_remapTexture_set)
    point3DSize = property(_Ainstec.FrameData_point3DSize_get, _Ainstec.FrameData_point3DSize_set)
    pointUVSize = property(_Ainstec.FrameData_pointUVSize_get, _Ainstec.FrameData_pointUVSize_set)
    triangleIndicesSize = property(_Ainstec.FrameData_triangleIndicesSize_get, _Ainstec.FrameData_triangleIndicesSize_set)
    depthmapSize = property(_Ainstec.FrameData_depthmapSize_get, _Ainstec.FrameData_depthmapSize_set)
    normalsSize = property(_Ainstec.FrameData_normalsSize_get, _Ainstec.FrameData_normalsSize_set)
    pointColorSize = property(_Ainstec.FrameData_pointColorSize_get, _Ainstec.FrameData_pointColorSize_set)
    textureSize = property(_Ainstec.FrameData_textureSize_get, _Ainstec.FrameData_textureSize_set)
    pointCount = property(_Ainstec.FrameData_pointCount_get, _Ainstec.FrameData_pointCount_set)
    remapTextureSize = property(_Ainstec.FrameData_remapTextureSize_get, _Ainstec.FrameData_remapTextureSize_set)

# Register FrameData in _Ainstec:
_Ainstec.FrameData_swigregister(FrameData)

class OutputSettings(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    sendPoint3D = property(_Ainstec.OutputSettings_sendPoint3D_get, _Ainstec.OutputSettings_sendPoint3D_set)
    sendPointUV = property(_Ainstec.OutputSettings_sendPointUV_get, _Ainstec.OutputSettings_sendPointUV_set)
    sendTriangleIndices = property(_Ainstec.OutputSettings_sendTriangleIndices_get, _Ainstec.OutputSettings_sendTriangleIndices_set)
    sendDepthmap = property(_Ainstec.OutputSettings_sendDepthmap_get, _Ainstec.OutputSettings_sendDepthmap_set)
    sendNormals = property(_Ainstec.OutputSettings_sendNormals_get, _Ainstec.OutputSettings_sendNormals_set)
    sendPointColor = property(_Ainstec.OutputSettings_sendPointColor_get, _Ainstec.OutputSettings_sendPointColor_set)
    sendTexture = property(_Ainstec.OutputSettings_sendTexture_get, _Ainstec.OutputSettings_sendTexture_set)
    sendRemapTexture = property(_Ainstec.OutputSettings_sendRemapTexture_get, _Ainstec.OutputSettings_sendRemapTexture_set)

    def __init__(self):
        _Ainstec.OutputSettings_swiginit(self, _Ainstec.new_OutputSettings())
    __swig_destroy__ = _Ainstec.delete_OutputSettings

# Register OutputSettings in _Ainstec:
_Ainstec.OutputSettings_swigregister(OutputSettings)

class CameraParam(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    textureWidth = property(_Ainstec.CameraParam_textureWidth_get, _Ainstec.CameraParam_textureWidth_set)
    textureHeight = property(_Ainstec.CameraParam_textureHeight_get, _Ainstec.CameraParam_textureHeight_set)
    irWidth = property(_Ainstec.CameraParam_irWidth_get, _Ainstec.CameraParam_irWidth_set)
    irHeight = property(_Ainstec.CameraParam_irHeight_get, _Ainstec.CameraParam_irHeight_set)
    irPerNum = property(_Ainstec.CameraParam_irPerNum_get, _Ainstec.CameraParam_irPerNum_set)
    hdrCnt = property(_Ainstec.CameraParam_hdrCnt_get, _Ainstec.CameraParam_hdrCnt_set)
    pixelBytes = property(_Ainstec.CameraParam_pixelBytes_get, _Ainstec.CameraParam_pixelBytes_set)
    depthType = property(_Ainstec.CameraParam_depthType_get, _Ainstec.CameraParam_depthType_set)
    reconstructionType = property(_Ainstec.CameraParam_reconstructionType_get, _Ainstec.CameraParam_reconstructionType_set)

    def __init__(self):
        _Ainstec.CameraParam_swiginit(self, _Ainstec.new_CameraParam())
    __swig_destroy__ = _Ainstec.delete_CameraParam

# Register CameraParam in _Ainstec:
_Ainstec.CameraParam_swigregister(CameraParam)

class CameraInfo(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    errorCode = property(_Ainstec.CameraInfo_errorCode_get, _Ainstec.CameraInfo_errorCode_set)
    cameraName = property(_Ainstec.CameraInfo_cameraName_get, _Ainstec.CameraInfo_cameraName_set)
    cameraModel = property(_Ainstec.CameraInfo_cameraModel_get, _Ainstec.CameraInfo_cameraModel_set)
    cameraIP = property(_Ainstec.CameraInfo_cameraIP_get, _Ainstec.CameraInfo_cameraIP_set)
    port = property(_Ainstec.CameraInfo_port_get, _Ainstec.CameraInfo_port_set)
    userIP = property(_Ainstec.CameraInfo_userIP_get, _Ainstec.CameraInfo_userIP_set)
    serialNum = property(_Ainstec.CameraInfo_serialNum_get, _Ainstec.CameraInfo_serialNum_set)
    macAddr = property(_Ainstec.CameraInfo_macAddr_get, _Ainstec.CameraInfo_macAddr_set)
    cameraSystemVersion = property(_Ainstec.CameraInfo_cameraSystemVersion_get, _Ainstec.CameraInfo_cameraSystemVersion_set)
    algorithmVersion = property(_Ainstec.CameraInfo_algorithmVersion_get, _Ainstec.CameraInfo_algorithmVersion_set)
    memsVersion = property(_Ainstec.CameraInfo_memsVersion_get, _Ainstec.CameraInfo_memsVersion_set)
    cameraOSVersion = property(_Ainstec.CameraInfo_cameraOSVersion_get, _Ainstec.CameraInfo_cameraOSVersion_set)
    ainstecCamSdkVersion = property(_Ainstec.CameraInfo_ainstecCamSdkVersion_get, _Ainstec.CameraInfo_ainstecCamSdkVersion_set)
    rgbStatus = property(_Ainstec.CameraInfo_rgbStatus_get, _Ainstec.CameraInfo_rgbStatus_set)
    memsStatus = property(_Ainstec.CameraInfo_memsStatus_get, _Ainstec.CameraInfo_memsStatus_set)
    isDHCP = property(_Ainstec.CameraInfo_isDHCP_get, _Ainstec.CameraInfo_isDHCP_set)
    moduleID = property(_Ainstec.CameraInfo_moduleID_get, _Ainstec.CameraInfo_moduleID_set)
    algoType = property(_Ainstec.CameraInfo_algoType_get, _Ainstec.CameraInfo_algoType_set)
    camParam = property(_Ainstec.CameraInfo_camParam_get, _Ainstec.CameraInfo_camParam_set)
    outputSettings = property(_Ainstec.CameraInfo_outputSettings_get, _Ainstec.CameraInfo_outputSettings_set)

    def __init__(self):
        _Ainstec.CameraInfo_swiginit(self, _Ainstec.new_CameraInfo())
    __swig_destroy__ = _Ainstec.delete_CameraInfo

# Register CameraInfo in _Ainstec:
_Ainstec.CameraInfo_swigregister(CameraInfo)

class ErrorCodeHandler(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _Ainstec.delete_ErrorCodeHandler

    def Handle(self, errorCode):
        return _Ainstec.ErrorCodeHandler_Handle(self, errorCode)

    def __init__(self):
        if self.__class__ == ErrorCodeHandler:
            _self = None
        else:
            _self = self
        _Ainstec.ErrorCodeHandler_swiginit(self, _Ainstec.new_ErrorCodeHandler(_self, ))
    def __disown__(self):
        self.this.disown()
        _Ainstec.disown_ErrorCodeHandler(self)
        return weakref.proxy(self)

# Register ErrorCodeHandler in _Ainstec:
_Ainstec.ErrorCodeHandler_swigregister(ErrorCodeHandler)

class FrameDataHandler(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _Ainstec.delete_FrameDataHandler

    def Handle(self, cameraInfo, frameData):
        return _Ainstec.FrameDataHandler_Handle(self, cameraInfo, frameData)

    def __init__(self):
        if self.__class__ == FrameDataHandler:
            _self = None
        else:
            _self = self
        _Ainstec.FrameDataHandler_swiginit(self, _Ainstec.new_FrameDataHandler(_self, ))
    def __disown__(self):
        self.this.disown()
        _Ainstec.disown_FrameDataHandler(self)
        return weakref.proxy(self)

# Register FrameDataHandler in _Ainstec:
_Ainstec.FrameDataHandler_swigregister(FrameDataHandler)

class Point3f(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    x = property(_Ainstec.Point3f_x_get, _Ainstec.Point3f_x_set)
    y = property(_Ainstec.Point3f_y_get, _Ainstec.Point3f_y_set)
    z = property(_Ainstec.Point3f_z_get, _Ainstec.Point3f_z_set)

    def __init__(self):
        _Ainstec.Point3f_swiginit(self, _Ainstec.new_Point3f())
    __swig_destroy__ = _Ainstec.delete_Point3f

# Register Point3f in _Ainstec:
_Ainstec.Point3f_swigregister(Point3f)

class Point2f(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    x = property(_Ainstec.Point2f_x_get, _Ainstec.Point2f_x_set)
    y = property(_Ainstec.Point2f_y_get, _Ainstec.Point2f_y_set)

    def __init__(self):
        _Ainstec.Point2f_swiginit(self, _Ainstec.new_Point2f())
    __swig_destroy__ = _Ainstec.delete_Point2f

# Register Point2f in _Ainstec:
_Ainstec.Point2f_swigregister(Point2f)

CAM_LEFT = _Ainstec.CAM_LEFT
CAM_RGB = _Ainstec.CAM_RGB
CAM_RIGHT = _Ainstec.CAM_RIGHT
POINT_TO_CAM_LEFT = _Ainstec.POINT_TO_CAM_LEFT
POINT_TO_CAM_RGB = _Ainstec.POINT_TO_CAM_RGB
POINT_TO_CAM_RIGHT = _Ainstec.POINT_TO_CAM_RIGHT
class Camera(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def DiscoverCameras(self, camInfoVector, timeout=1000):
        return _Ainstec.Camera_DiscoverCameras(self, camInfoVector, timeout)

    def Open(self, cameraInfo, timeout=60000):
        return _Ainstec.Camera_Open(self, cameraInfo, timeout)

    def Capture(self, cameraInfo, frameData):
        return _Ainstec.Camera_Capture(self, cameraInfo, frameData)

    def RegisterErrorCodeHandler(self, errorCodeHandler):
        return _Ainstec.Camera_RegisterErrorCodeHandler(self, errorCodeHandler)

    def RegisterFrameDataHandler(self, *args):
        return _Ainstec.Camera_RegisterFrameDataHandler(self, *args)

    def CaptureDataAsync(self, cameraInfo):
        return _Ainstec.Camera_CaptureDataAsync(self, cameraInfo)

    def SetCameraIP(self, cameraInfo, newIP):
        return _Ainstec.Camera_SetCameraIP(self, cameraInfo, newIP)

    def SetCameraToDHCP(self, cameraInfo):
        return _Ainstec.Camera_SetCameraToDHCP(self, cameraInfo)

    def CameraGetStatus(self, cameraInfo):
        return _Ainstec.Camera_CameraGetStatus(self, cameraInfo)

    def SendMemsCommands(self, cameraInfo, strCommands):
        return _Ainstec.Camera_SendMemsCommands(self, cameraInfo, strCommands)

    def SendAndRecvMemsCommands(self, cameraInfo, strCommands, strRecv):
        return _Ainstec.Camera_SendAndRecvMemsCommands(self, cameraInfo, strCommands, strRecv)

    def CameraGetVersion(self, cameraInfo):
        return _Ainstec.Camera_CameraGetVersion(self, cameraInfo)

    def CameraSetTriggerOutParam(self, cameraInfo, mode, cycleNumValue, cycleLenValue):
        return _Ainstec.Camera_CameraSetTriggerOutParam(self, cameraInfo, mode, cycleNumValue, cycleLenValue)

    def CameraGetTriggerOutParam(self, cameraInfo, mode, cycleNumValue, cycleLenValue):
        return _Ainstec.Camera_CameraGetTriggerOutParam(self, cameraInfo, mode, cycleNumValue, cycleLenValue)

    def CameraReboot(self, cameraInfo):
        return _Ainstec.Camera_CameraReboot(self, cameraInfo)

    def AddParamGroup(self, cameraInfo, paramGroupName):
        return _Ainstec.Camera_AddParamGroup(self, cameraInfo, paramGroupName)

    def GetParamGroups(self, cameraInfo, paramGroupNames):
        return _Ainstec.Camera_GetParamGroups(self, cameraInfo, paramGroupNames)

    def DeleteParamGroup(self, cameraInfo, paramGroupName):
        return _Ainstec.Camera_DeleteParamGroup(self, cameraInfo, paramGroupName)

    def ApplyParamGroup(self, cameraInfo, paramGroupName):
        return _Ainstec.Camera_ApplyParamGroup(self, cameraInfo, paramGroupName)

    def ReconstructPoints(self, cameraInfo, leftPoints, rightPoints, points):
        return _Ainstec.Camera_ReconstructPoints(self, cameraInfo, leftPoints, rightPoints, points)

    def GetAttributeTreeJson(self, cameraInfo, strAttributeTreeJson):
        return _Ainstec.Camera_GetAttributeTreeJson(self, cameraInfo, strAttributeTreeJson)

    def GetNodeAttributeJson(self, cameraInfo, key, strNodeAttributeJson):
        return _Ainstec.Camera_GetNodeAttributeJson(self, cameraInfo, key, strNodeAttributeJson)

    def SetValue(self, *args):
        return _Ainstec.Camera_SetValue(self, *args)

    def GetValue(self, *args):
        return _Ainstec.Camera_GetValue(self, *args)

    def Get3DCameraIntrinsic(self, cameraInfo, cameraPosition, cameraIntrinsic):
        return _Ainstec.Camera_Get3DCameraIntrinsic(self, cameraInfo, cameraPosition, cameraIntrinsic)

    def Get3DCameraExtrinsic(self, cameraInfo, extrinsicType, cameraExtrinsic):
        return _Ainstec.Camera_Get3DCameraExtrinsic(self, cameraInfo, extrinsicType, cameraExtrinsic)

    def Close(self, cameraInfo):
        return _Ainstec.Camera_Close(self, cameraInfo)
    __swig_destroy__ = _Ainstec.delete_Camera

# Register Camera in _Ainstec:
_Ainstec.Camera_swigregister(Camera)


def CreateCamera(type):
    return _Ainstec.CreateCamera(type)

def DestoryCamera(cam):
    return _Ainstec.DestoryCamera(cam)
ConfigFile = _Ainstec.ConfigFile
CalibrationFile = _Ainstec.CalibrationFile
LogFile = _Ainstec.LogFile
FirmwareFile = _Ainstec.FirmwareFile
ProjectorCalibrationFile = _Ainstec.ProjectorCalibrationFile
MemsFirmwareFile = _Ainstec.MemsFirmwareFile
SaveImagesToLocal = _Ainstec.SaveImagesToLocal
Calibration = _Ainstec.Calibration
Intrinsics = _Ainstec.Intrinsics
Extrinsics = _Ainstec.Extrinsics
Coefficient = _Ainstec.Coefficient
class FrameDataEx(FrameData):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _Ainstec.delete_FrameDataEx

    def __init__(self, *args):
        _Ainstec.FrameDataEx_swiginit(self, _Ainstec.new_FrameDataEx(*args))
    outputIR = property(_Ainstec.FrameDataEx_outputIR_get, _Ainstec.FrameDataEx_outputIR_set)
    outputIRSize = property(_Ainstec.FrameDataEx_outputIRSize_get, _Ainstec.FrameDataEx_outputIRSize_set)

# Register FrameDataEx in _Ainstec:
_Ainstec.FrameDataEx_swigregister(FrameDataEx)

class CameraInterfaceEx(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Ainstec.CameraInterfaceEx_swiginit(self, _Ainstec.new_CameraInterfaceEx(*args))
    __swig_destroy__ = _Ainstec.delete_CameraInterfaceEx

    def CaptureEx(self, cameraInfo, frameDataEx):
        return _Ainstec.CameraInterfaceEx_CaptureEx(self, cameraInfo, frameDataEx)

    def CameraImportFile(self, cameraInfo, fileType, filePath, timeout=30000):
        return _Ainstec.CameraInterfaceEx_CameraImportFile(self, cameraInfo, fileType, filePath, timeout)

    def CameraExportFile(self, cameraInfo, type, fileContent, timeout=30000):
        return _Ainstec.CameraInterfaceEx_CameraExportFile(self, cameraInfo, type, fileContent, timeout)

    def RestoreParam(self, cameraInfo):
        return _Ainstec.CameraInterfaceEx_RestoreParam(self, cameraInfo)

    def SaveParam(self, cameraInfo):
        return _Ainstec.CameraInterfaceEx_SaveParam(self, cameraInfo)

    def GetConnectionStatus(self, cameraInfo):
        return _Ainstec.CameraInterfaceEx_GetConnectionStatus(self, cameraInfo)

    def ExportParamGroup(self, cameraInfo, paramGroupName, destFilePath, timeout=30000):
        return _Ainstec.CameraInterfaceEx_ExportParamGroup(self, cameraInfo, paramGroupName, destFilePath, timeout)

    def SetDebugMode(self, cameraInfo, debugMode):
        return _Ainstec.CameraInterfaceEx_SetDebugMode(self, cameraInfo, debugMode)

    def CameraGetCalibrationMatrix(self, cameraInfo, type, matrix):
        return _Ainstec.CameraInterfaceEx_CameraGetCalibrationMatrix(self, cameraInfo, type, matrix)

# Register CameraInterfaceEx in _Ainstec:
_Ainstec.CameraInterfaceEx_swigregister(CameraInterfaceEx)


cvar = _Ainstec.cvar
mapMemsStripesType = cvar.mapMemsStripesType
