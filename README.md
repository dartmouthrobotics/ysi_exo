# ysi_exo

Driver for the YSI EXO sondes that interface with the computer through the signal output adapter (v1 or v2), via RS232. This fork has been updated to work with ROS noetic and Ubuntu 20.04. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details

[Dartmouth Reality and Robotics Lab](http://rlab.cs.dartmouth.edu/home/)

Authors: [Alberto Quattrini Li](https://sites.google.com/view/albertoq) - Dartmouth College.

## Installation

After following the instructions for the hardware setup, available in the manual from YSI, the following will set the environment to make the ROS driver running.
`ysi_exo` has been tested under ROS noetic and Ubuntu 20.04. This is research code, expect that it changes often and any fitness for a particular purpose is disclaimed.

### Dependencies

- [Robot Operating System (ROS)](http://wiki.ros.org) (middleware for robotics),
- [minimalmodbus](ihttps://minimalmodbus.readthedocs.io/en/stable/) API for MODBUS.
 
		sudo pip install minimalmodbus


### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using

	cd catkin_workspace/src
	git clone https://github.com/jakebonney10/ysi_exo.git
	cd ../
	catkin_make


## Usage
You can run the node with (the default values are for the DCP Modbus)

	roslaunch ysi_exo ysi_exo.launch

## Nodes

### sonde

Publishes sonde measurements.


#### Published Topics

* **`sonde`** ([ysi_exo/Sonde])

	Custom message that includes all parameters recorded.
