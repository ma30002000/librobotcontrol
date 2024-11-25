from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.files import get, save
from conan.tools.scm import Git
from conan.tools.files import collect_libs
from conan.tools.microsoft import is_msvc
import os

required_conan_version = ">=1.53.0"


class LibRobotcontrolConan(ConanFile):
    name = "librobotcontrol"
    description = "Hardware interface library for the Robotics Cape and later the BeagleBone Blue."
    license = "MIT"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/beagleboard/librobotcontrol"
    package_type = "library"
    settings = "os", "arch", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
    }
    version = "1.0"
    exports_sources = ["CMakeLists.txt", "library/*"]

    def layout(self):
        cmake_layout(self, src_folder=".")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)