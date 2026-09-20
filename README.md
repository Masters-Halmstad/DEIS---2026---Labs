# Design of Embedded and Intelligent Systems Labs

This repository contains our individual lab work for the **Design of Embedded and
Intelligent Systems (DEIS)** course. The labs are performed on a Raspberry Pi 4
running Ubuntu and are accessed remotely from a laptop through Visual Studio
Code and SSH. Once a lab is complete, its files are fetched from the Raspberry
Pi and organized here for documentation and submission.

## Repository structure

Each lab is kept in its own directory. The lab directory contains the
implementation, supporting files, and the lab-specific documentation.

```text
.
├── Lab1/
│   ├── LabInstruction/
│   │   └── Lab1_basic_robotics1.pdf
│   ├── imgOutput/
│   ├── src/
│   │   └── cpp_pubsub/
│   ├── testWebCam.py
│   └── README.md
└── README.md
```

## Overall lab goal

The labs develop practical skills for designing embedded and intelligent
systems. Across the course, the work builds experience with:

- Preparing and administering a Raspberry Pi used as an embedded computer.
- Connecting to the Raspberry Pi remotely over a network using SSH.
- Installing and using Ubuntu and ROS 2.
- Capturing and processing sensor data, including camera images.
- Building distributed applications that exchange messages between machines.
- Developing ROS 2 nodes for sensing, communication, and actuator control.

The lab exercises are separate from the course project, although some
techniques may also be useful in the project.

## Initial setup

The following setup is intended for a Raspberry Pi 4. Lab instructions should
be consulted before installing or changing system software.

1. Install Ubuntu 24.04 LTS on the Raspberry Pi.
2. Install ROS 2 Jazzy, including the required development tools.
3. Connect the Raspberry Pi and the development laptop to the same network.
4. Enable SSH on the Raspberry Pi.
5. Create a workspace for ROS 2 packages.
6. Install Python tooling and OpenCV in a virtual environment when a lab
   requires camera processing.
7. Keep the Raspberry Pi implementation and the fetched repository files
   synchronized after each lab session.

Use the official documentation for the current installation procedures:

- [Ubuntu for Raspberry Pi](https://ubuntu.com/download/raspberry-pi)
- [ROS 2 Jazzy installation on Ubuntu](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debians.html)

## Important concepts

### SSH-based development

SSH provides secure terminal access to the Raspberry Pi from the laptop. This
allows commands, builds, and tests to run on the target embedded computer while
the source files are edited through the VS Code SSH interface.

### ROS 2 workspaces and packages

A ROS 2 workspace groups packages that can be built and sourced together. A
package describes its metadata and dependencies, while a build system such as
`ament_cmake` compiles and installs its executables.

### ROS 2 nodes, topics, publishers, and subscribers

A node is a running ROS 2 process. Publishers send typed messages to topics and
subscribers receive messages from topics. Topics provide the communication
layer that allows independent processes, and potentially different computers,
to exchange data.

### Virtual environments and OpenCV

A Python virtual environment isolates Python packages from the operating
system. OpenCV provides tools for camera capture and image processing, such as
converting frames to grayscale and detecting edges.

### Embedded and distributed operation

The Raspberry Pi is the embedded execution target, while SSH and ROS 2 support
distributed development and communication. Commands and sensor data must be
tested on the actual target and on the network configuration used by the lab.

## Universal commands

### Connect to the Raspberry Pi

Replace the username and address with the values configured for the Raspberry
Pi:

```bash
ssh <username>@<raspberry-pi-ip>
```

Useful connection and service checks:

```bash
ip -a
sudo systemctl status ssh
```

### Update Ubuntu packages

```bash
sudo apt update
sudo apt upgrade
```

### Source ROS 2

Source ROS 2 in every terminal where ROS 2 commands or nodes are used:

```bash
source /opt/ros/jazzy/setup.bash
```

After building a workspace, source its overlay as well:

```bash
source install/setup.bash
```

### Build and run a ROS 2 workspace

Run these commands from the workspace root:

```bash
colcon build
source install/setup.bash
ros2 pkg list
```

### Create and use a Python virtual environment

```bash
python3 -m venv <environment-name>
source <environment-name>/bin/activate
python -m pip install --upgrade pip
```

Leave the environment with:

```bash
deactivate
```

## Lab navigation

- [Lab 1 - Basic robotics](Lab1/README.md)

Additional labs will be added to this list as they are completed.

## Disclaimer

This repository documents individual lab work transferred from a Raspberry Pi
to a separate development machine. Commands, package versions, network
addresses, device names, and hardware availability may differ between
environments. Do not copy credentials or network-specific values into the
repository. Always follow the current lab instruction and verify commands on
the target Raspberry Pi.

The code and notes may require adaptation when used with another Raspberry Pi,
Ubuntu release, ROS 2 distribution, camera, network, or robot platform.

## Conclusion

This README is the entry point for the DEIS lab repository. It records the
shared setup and concepts, while each lab README describes the specific
procedure, implementation, expected results, and issues for that lab.
