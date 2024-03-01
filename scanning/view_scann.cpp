#include <fstream> // For std::ifstream
#include <sstream> // For std::ostringstream
#include "Læsning af punktskyer v3-1.h"
// Include other necessary headers

int main() {
    std::ifstream inFile("01331_000_recog_cam0_pz15.pc3d", std::ios::binary);
    if (!inFile) {
        std::cerr << "Failed to open file" << std::endl;
        return 1;
    }

    CPointCloud3D pointCloud;
    try {
        pointCloud.ReadBinary(inFile);
        // Visualization code goes here
    } catch (const std::exception& e) {
        std::cerr << "Error reading point cloud: " << e.what() << std::endl;
        return 1;
    }

    // Visualization code would continue here...
    return 0;
}
