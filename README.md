# SENTRA – Smart Enhanced Navigation & Threat Recognition Architecture

## AI-Based Railway Obstacle Detection and Real-Time Sensor Integration Prototype

SENTRA is a proof-of-concept railway safety and obstacle detection system developed to identify potential obstacles on railway tracks and support real-time safety assessment.

The project combines YOLO-based computer vision, railway ego-path detection, LiDAR-based distance sensing, and edge computing. The prototype involves an NVIDIA Jetson Nano, USB camera, Benewake TF-Luna LiDAR, trained YOLO models, and a physical railway-track demonstration setup.

---

## Project Overview

Railway safety applications require more than conventional object detection. Detecting an object in a camera frame does not necessarily indicate whether it is relevant to the railway path or whether it represents an immediate safety risk.

SENTRA was developed to explore a railway-aware sensing pipeline that combines visual perception with distance information.

The project development includes:

- YOLO-based obstacle detection
- Railway ego-path detection
- Track-aware object analysis
- LiDAR-based distance sensing
- Real-time camera sensing
- Edge computing using NVIDIA Jetson Nano
- Physical prototype development and testing
- Remote Jetson Nano access and development using PuTTY and NoMachine

The objective is to develop a sensing framework capable of identifying obstacles and supporting safety-oriented decision making.

---

## Problem Statement

Obstacles such as humans, animals, or other objects may obstruct railway tracks. A camera-based object detection system can identify objects but does not independently provide complete information about their relevance to the railway path or their distance from the sensing system.

The system therefore aims to address the following questions:

1. Is an object detected?
2. Is the object associated with the railway path?
3. What is the distance to the detected obstacle?
4. Does the obstacle require monitoring or a safety response?

SENTRA combines computer vision and distance sensing to improve obstacle awareness in a railway environment.

---

## System Components

### YOLO-Based Obstacle Detection

A YOLO-based object detection pipeline was developed for detecting objects in railway scenes.

The development process included:

- Dataset preparation
- Model training
- Model validation
- Image-based prediction
- Railway obstacle detection experiments

The detection system provides object class information, bounding boxes, confidence scores, and object location within the image.

---

### Railway Ego-Path Detection

Object detection alone cannot determine whether an obstacle is relevant to the railway path.

The ego-path detection component was developed to estimate the railway track region and analyze the position of detected objects relative to the expected path.

This supports track-aware obstacle analysis and helps prioritize objects associated with the railway path.

---

### LiDAR-Based Distance Sensing

The prototype uses a Benewake TF-Luna LiDAR sensor for distance measurement.

The LiDAR component provides physical distance information that complements camera-based obstacle detection.

The sensor is used for:

- Real-time distance measurement
- Obstacle proximity analysis
- Distance-aware safety assessment
- Supporting visual sensing with physical range information

---

## Hardware Components

### NVIDIA Jetson Nano Developer Kit

The NVIDIA Jetson Nano serves as the edge computing platform for the prototype.

It was used for:

- Camera interfacing
- Real-time video capture
- OpenCV-based image processing
- Computer vision experiments
- YOLO deployment experiments
- LiDAR communication
- Sensor data processing
- Real-time system testing

---

### USB Camera

A USB camera provides real-time visual input for obstacle detection.

The camera was configured and tested on the NVIDIA Jetson Nano for:

- Camera device detection
- Real-time video capture
- OpenCV-based processing
- Railway obstacle sensing experiments

---

### Benewake TF-Luna LiDAR

The Benewake TF-Luna LiDAR is used for real-time distance sensing.

It provides distance measurements to support obstacle proximity analysis and sensor-based safety assessment.

---

### Physical Railway Prototype

A physical railway-track prototype was developed for controlled testing and demonstration of the SENTRA concept.

The prototype was used for:

- Obstacle placement
- Camera-based sensing
- LiDAR distance sensing
- Real-time processing experiments
- System demonstration

---

## Jetson Nano Remote Access and Development

The NVIDIA Jetson Nano was configured and operated remotely from a Windows laptop during development and testing.

This remote development setup enabled system configuration, hardware troubleshooting, software testing, and desktop access without requiring continuous use of a dedicated monitor and keyboard connected directly to the Jetson Nano.

---

### PuTTY

PuTTY was used for remote terminal access to the NVIDIA Jetson Nano.

It was used for:

- Remote command-line access
- System configuration
- Package installation and updates
- Network troubleshooting
- Camera device verification
- Kernel and module troubleshooting
- Hardware verification
- Running Python applications
- Monitoring connected devices

---

### NoMachine

NoMachine was used to access the complete NVIDIA Jetson Nano desktop environment remotely from a Windows laptop.

This enabled:

- Remote access to the Jetson Nano graphical desktop
- Remote development and debugging
- Running graphical applications
- Monitoring system output
- Viewing the Jetson Nano desktop directly on the laptop
- Testing and operating applications remotely

The Jetson Nano desktop environment was successfully accessed and operated remotely using NoMachine.

---

## Software and Technologies

| Technology | Purpose |
|---|---|
| Python | System development and experimentation |
| YOLO / YOLOv8 | Object detection |
| Ultralytics | YOLO training and inference |
| OpenCV | Camera interfacing and image processing |
| Google Colab | Model training and experimentation |
| NVIDIA Jetson Nano | Edge computing platform |
| Ubuntu | Jetson Nano operating environment |
| PuTTY | Remote terminal and command-line access |
| NoMachine | Remote graphical desktop access |
| UART | LiDAR communication |

---

## Development Modules

### Obstacle Detection

The obstacle detection development includes:

- YOLO environment setup
- Dataset handling
- Model training
- Model validation
- Prediction and inference
- Railway obstacle detection experiments

### Ego-Path Detection

The ego-path development includes:

- Railway path estimation
- Track-region detection
- Path-mask generation
- Railway-aware image processing

### System Integration

The project development explores the integration of:

- Object detection
- Railway ego-path information
- Track-aware obstacle analysis
- LiDAR distance sensing
- Safety-oriented decision logic

---

## Testing and Verification

The project was developed and evaluated through multiple stages.

### Software-Level Development

- YOLO model training and validation
- Image-based prediction
- Obstacle detection experiments
- Ego-path detection
- Railway-track-aware image processing
- Computer vision integration experiments

### Hardware-Level Testing

- NVIDIA Jetson Nano configuration
- Remote terminal access using PuTTY
- Remote desktop access using NoMachine
- USB camera detection and configuration
- Real-time camera testing
- LiDAR communication and distance sensing
- Hardware troubleshooting and verification

### Prototype-Level Testing

- Physical railway-track prototype testing
- Camera-based obstacle sensing
- LiDAR-based distance measurement
- Real-time sensing experiments

---

Current Project Status

The project is currently developed as a proof-of-concept prototype.

Completed development and testing activities include:

YOLO-based obstacle detection
Ego-path and railway-track detection development
Computer vision experimentation
NVIDIA Jetson Nano setup and configuration
USB camera configuration and testing
Real-time camera sensing
TF-Luna LiDAR distance sensing
Physical railway prototype development
Remote terminal access using PuTTY
Remote desktop access using NoMachine


Current Limitations

SENTRA is currently a prototype developed and tested in a controlled environment.

The current limitations include:

Testing has not been performed on an operational railway system
Performance may depend on lighting and environmental conditions
Additional sensor calibration is required
Object-to-distance association requires further refinement
Large-scale field validation has not yet been performed



Future Development

Potential future improvements include:

Thermal camera integration
Advanced multi-sensor fusion
Improved object-to-distance association
Sensor confidence scoring
TensorRT optimization for NVIDIA Jetson Nano
Improved real-time inference performance
Low-light testing
Testing under adverse weather conditions
Large-scale railway dataset evaluation
Field-level validation and deployment studies



Key Learning Outcomes

Through the development of SENTRA, the project involved practical work in:

AI-based object detection
YOLO model training and inference
Computer vision
Railway ego-path detection
Track-aware perception
LiDAR distance sensing
NVIDIA Jetson Nano
Edge AI and embedded computing
UART communication
OpenCV
Real-time camera processing
Linux system configuration
Remote SSH access using PuTTY
Remote desktop operation using NoMachine
Hardware and driver troubleshooting
Embedded system integration
Physical prototype development



Author

P Bhavitha
B.Tech, Electronics and Communication Engineering
PDPM IIITDM Jabalpur
