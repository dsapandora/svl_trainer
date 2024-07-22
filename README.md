
# ROS LG SVL Simulation Controller

![Image Description](https://cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/business7/uploads/ros/original/2X/9/922a6723d231dd94c7167636cb03304c227b98bb.jpeg)

This repository contains a ROS library written in Python that interfaces with the LG SVL Simulator. It uses OpenCV and Pygame to control a vehicle in the simulation world through ROS topics. The code captures image data from the simulator, processes it, and allows the user to control the vehicle using keyboard inputs.

## Overview

This project provides an interface between ROS and the LG SVL Simulator. It subscribes to the simulator's camera feed, processes the images using OpenCV, and allows manual control of the vehicle through keyboard inputs. The processed images are displayed using Pygame, and vehicle commands are published to ROS topics to control the vehicle's behavior in the simulation.

## Prerequisites

- ROS (Robot Operating System)
- Python
- OpenCV
- Pygame
- LG SVL Simulator

### Installation

Install the required Python libraries:

```bash
pip install opencv-python pygame
```

Ensure that ROS is installed and properly set up on your machine. You will also need the LG SVL Simulator installed and running.

## Running the Code

To run the code, execute the following command:

```bash
rosrun <your_package_name> svl_human_agent_client.py
```

Make sure to replace `<your_package_name>` with the actual name of your ROS package.

## Code Explanation

### Importing Libraries

The code imports necessary libraries including rospy for ROS, pygame for handling keyboard inputs and displaying images, cv2 for image processing, and numpy for numerical operations.

### Global Variables and Publisher

- `video_size`: Defines the size of the video window.
- `velocity_publisher`: Publishes vehicle control commands to the `/vehicle_cmd` topic.
- `vel_msg`: An instance of `VehicleControlData` message.
- `scale_percent`: Defines the percentage to scale the captured image.

### Key Action Function

The `key_action` function captures keyboard inputs using Pygame and adjusts the vehicle control commands accordingly. It modifies the steering angle, acceleration, braking, and gear based on the pressed keys.

### Callback Function

The `callback` function processes incoming image data from the simulator. It converts the compressed image data to a numpy array, decodes it using OpenCV, and processes it by rotating, resizing, and flipping the image. The processed image is then displayed using Pygame. The function also captures the current key actions and publishes the corresponding vehicle control commands.

### Main Function

The `main` function initializes the ROS node, sets up the subscriber to the simulator's camera feed, and continuously updates the vehicle control commands based on user inputs. It handles graceful shutdown upon receiving a keyboard interrupt.

## About

This project provides an intuitive way to control a simulated vehicle using ROS, OpenCV, and Pygame. It allows for manual control of the vehicle in the LG SVL Simulator, making it a valuable tool for developing and testing autonomous vehicle algorithms.

## Future Enhancements

- Add autonomous control capabilities using pre-trained models.
- Improve the user interface and display additional simulation data.
- Implement advanced image processing techniques for better visual feedback.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## Contact

For any questions or support, please open an issue in this repository.

---
