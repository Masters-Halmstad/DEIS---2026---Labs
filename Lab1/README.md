# Lab 1 - Getting Started with Basic Robotics

This lab introduces the core tools used throughout the Design of Embedded and
Intelligent Systems course. It is performed on a Raspberry Pi 4 running Ubuntu
24.04 with ROS 2 Jazzy and covers remote access, camera-based image
processing, ROS 2 communication, and basic motion-command messages.

The original instructions are available in
[Lab1_basic_robotics1.pdf](LabInstruction/Lab1_basic_robotics1.pdf).

## Objectives

By completing this lab, the learner should be able to:

- Prepare a Raspberry Pi with Ubuntu and ROS 2.
- Verify ROS 2 communication with a talker and listener.
- Connect to the Raspberry Pi remotely using SSH.
- Capture frames from a USB webcam and perform basic edge detection.
- Create and build a ROS 2 C++ package.
- Publish and subscribe to `std_msgs/msg/String` messages.
- Receive motion-control messages on the `/action` topic.

## Setup

### Hardware and network

The lab requires:

- Raspberry Pi 4 with a suitable power supply.
- SD card containing Ubuntu 24.04.
- USB webcam.
- Laptop or another computer with an SSH client.
- A shared network connection between the Raspberry Pi and laptop.

Use the network credentials supplied for the course environment. Do not store
shared passwords or private network details in this repository.

### Software

Install ROS 2 Jazzy and the ROS 2 development tools on Ubuntu. The official
references are:

- [Ubuntu for Raspberry Pi](https://ubuntu.com/download/raspberry-pi)
- [ROS 2 Jazzy installation](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debians.html)
- [ROS 2 C++ publisher and subscriber tutorial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html)

Enable SSH on the Raspberry Pi:

```bash
sudo apt update
sudo apt upgrade
sudo apt install openssh-server
sudo systemctl enable --now ssh
sudo systemctl status ssh
```

Connect from the laptop with:

```bash
ssh <username>@<raspberry-pi-ip>
```

Source ROS 2 before using ROS 2 commands:

```bash
source /opt/ros/jazzy/setup.bash
```

For the webcam task, create and activate an isolated Python environment, then
install OpenCV:

```bash
python3 -m venv opencv-venv
source opencv-venv/bin/activate
python -m pip install --upgrade pip
python -m pip install opencv-python
```

## Lab tasks

### Task 0 - Prepare the Raspberry Pi

Install Ubuntu 24.04 and ROS 2 Jazzy on the Raspberry Pi. Update the system
and confirm that the installation is usable before continuing.

### Task 1 - Verify ROS 2

Open two terminals and source ROS 2 in both. Run the standard ROS 2 talker in
one terminal and the listener in the other:

```bash
ros2 run demo_nodes_cpp talker
ros2 run demo_nodes_py listener
```

The listener should display messages published by the talker. Capture the
working output for the lab report.

### Task 2 - Connect with SSH

Find the Raspberry Pi IP address, confirm that the SSH service is running, and
connect from another computer on the same network. Record a screenshot of the
successful remote session for the report.

### Task 3 - Process a webcam feed

The [`testWebCam.py`](testWebCam.py) script:

1. Opens camera device `0`.
2. Reads frames from the USB webcam.
3. Converts each frame to grayscale.
4. Applies Canny edge detection.
5. Displays the color feed and edge-detection feed.
6. Saves screenshots when `s` is pressed.
7. Exits when `q` is pressed.

Run it from the directory containing the script:

```bash
source opencv-venv/bin/activate
python testWebCam.py
```

The `imgOutput` directory contains example captured images from this task.

### Task 4 - Build a ROS 2 C++ package

The [`src/cpp_pubsub`](src/cpp_pubsub) package uses `ament_cmake` and depends
on `rclcpp` and `std_msgs`. It builds two executables:

- `talker`, implemented in `publisher_lambda_function.cpp`, publishes
  `std_msgs/msg/String` messages on the `topic` topic every 500 milliseconds.
- `listener`, implemented in `subscriber_lambda_function.cpp`, subscribes to
  the `action` topic and logs the received string.

From the ROS 2 workspace root, build and source the package:

```bash
colcon build --packages-select cpp_pubsub
source install/setup.bash
```

Run the nodes in separate terminals:

```bash
ros2 run cpp_pubsub talker
ros2 run cpp_pubsub listener
```

The provided publisher and subscriber use different topic names. Therefore,
use the `topic` topic to test the provided publisher, and use `/action` with a
matching publisher when testing the provided listener.

### Task 5 - Send motion-control messages

The listener receives messages on `/action` using `std_msgs/msg/String`. A
single command can be sent with:

```bash
ros2 topic pub --once /action std_msgs/msg/String \
  "{data: '1/9/2025-11:05:35.859906,g,-1,-1,-2,0;0'}"
```

The final two values represent left and right motor speeds in the course
protocol. Positive and negative values represent opposite directions; `255`
and `-255` represent full speed in opposite directions, `127` represents
half-speed, and `0` stops a motor. The instruction sheet provides forward,
backward, left, right, half-speed, and stop examples.

Verify that the listener prints the received command and capture the terminal
output for the report. Use the course communication-protocol documentation for
the complete message format before sending commands to a real robot.

## Key concepts

### Ubuntu on an embedded computer

Ubuntu provides the operating system and package-management environment for
the Raspberry Pi. The Pi is the target computer on which the ROS 2 nodes and
camera-processing script execute.

### SSH

Secure Shell provides remote command-line access to the Raspberry Pi. It
separates the development interface from the embedded target while allowing
commands and programs to run on the Pi.

### OpenCV image processing

OpenCV is used to acquire camera frames and process them. Grayscale conversion
reduces a color image to intensity values, while Canny edge detection highlights
strong intensity changes that often correspond to object boundaries.

### ROS 2 nodes and topics

ROS 2 nodes are independent processes. A publisher writes typed messages to a
topic, and a subscriber receives messages from that topic. Both endpoints must
use compatible message types and the same topic name.

### QoS queue depth

The C++ nodes create publishers and subscriptions with a queue depth of `10`.
This controls how many messages can be buffered while the endpoint is
processing data.

### Motion-command protocol

The `/action` messages demonstrate how high-level robot actions can be
represented as strings containing metadata and motor-speed values. This is a
communication example; the listener in this repository only logs the message
and does not directly drive motor hardware.

## Expected outcome

After completing the lab, the following outcomes should be demonstrated:

- Ubuntu and ROS 2 Jazzy are installed on the Raspberry Pi.
- The standard ROS 2 talker and listener exchange messages.
- The laptop connects to the Raspberry Pi through SSH.
- The webcam feed is displayed in color and as detected edges.
- Color and edge screenshots are saved successfully.
- The `cpp_pubsub` package builds without errors.
- ROS 2 publisher and subscriber nodes run in separate terminals.
- The listener receives and prints `/action` motion-command messages.
- Screenshots or console captures are available for the lab report.

## Conclusion

Lab 1 establishes the basic workflow for the remaining labs: prepare an
embedded Linux target, access it remotely, process sensor input, build ROS 2
software, and exchange messages over a network. These skills form the
foundation for later sensing, communication, and robot-control exercises.

## Disclaimer

This README documents the repository contents and the intended lab workflow; it
does not replace the official instruction PDF or the course communication
protocol. Exact commands may need adjustment for the configured username, IP
address, workspace location, camera device, network, or installed package
versions.

The repository was fetched from a Raspberry Pi after development over SSH.
Hardware access, camera permissions, ROS 2 environment sourcing, and network
configuration were not independently reproduced on this development machine.
Do not send motion commands to a physical robot until the message format and
motor behavior have been checked safely.

## Back to the main README

[Return to the DEIS lab repository README](../README.md)
