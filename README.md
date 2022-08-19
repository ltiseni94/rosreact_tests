# Rosreact test suite

ROS package for end-to-end tests with the [rosreact library](https://www.npmjs.com/package/rosreact)

## Setup

### 1. Install ROS Noetic

Instructions for ROS Noetic installation on Ubuntu 20.04 LTS - and other distros - can be found [here](http://wiki.ros.org/noetic/Installation/Ubuntu)

### 2. Install ROS dependencies
    
    $ sudo apt-get install ros-noetic-rosbridge-suite
    $ sudo apt-get install ros-noetic-web-video-server
    $ sudo apt-get install ros-noetic-image-transport
    $ sudo apt-get install ros-noetic-image-transport-plugins

Eventually change the name of your distro, if needed.

## Usage

Execute the main launch file, which will run all the nodes and interfaces to the
**rosreact** web application.

    $ roslaunch rosreact_tests main.launch
