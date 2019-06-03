# ee245
A repository for all material relevant to EE245 labs.

## Installation
- `sudo apt install git swig libpython-dev python-numpy python-yaml python-matplotlib gcc-arm-none-eabi libpcl-dev libusb-1.0-0-dev sdcc` install dependency
- `cd ~/catkin_ws/src` please switch to your own ROS workspace
- `git clone https://github.com/UCR-Robotics/ee245.git` (Or git clone your own "forked" repo)
- `cd ee245`  go into this folder
- `./build.sh`   build simulation firmware
- `cd ../..`  go back to ROS workspace
- `catkin_make`  compile ROS package

## Usage
### Running on a real robot
- `roslaunch ee245 robot.launch`
- `roscd ee245`
- `cd scripts`
- `./some_script.py` or `python some_script.py`

### Running on simulation
- `roscd ee245`
- `cd scripts`
- `./some_script.py --sim` or `python some_script.py --sim`

