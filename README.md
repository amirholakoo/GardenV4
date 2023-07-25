# GardenV4

Garden Monitoring System
========================

This repository contains the code for a Garden Monitoring System using an ESP32 CAM and a Raspberry Pi. The system captures images of the garden, processes the images to detect soil conditions and sprouts, and decides whether to water the garden based on the sensor data. The data is logged to a CSV file and displayed on a web-based dashboard.

Table of Contents
-----------------

-   [Installation](https://chat.openai.com/c/92bacfaf-5b3f-45b6-b93c-33a469abb1e1#installation)
-   [Setup](https://chat.openai.com/c/92bacfaf-5b3f-45b6-b93c-33a469abb1e1#setup)
-   [Usage](https://chat.openai.com/c/92bacfaf-5b3f-45b6-b93c-33a469abb1e1#usage)
-   [License](https://chat.openai.com/c/92bacfaf-5b3f-45b6-b93c-33a469abb1e1#license)

Installation
------------

To run the system, you'll need to install Python and several Python libraries on your Raspberry Pi. You can do this using the following commands:

bashCopy code

`sudo apt-get update`

`sudo apt-get install python3 python3-pip`

`pip3 install flask pandas numpy matplotlib opencv-python-headless pillow requests`


You'll also need to install the Arduino IDE and the ESP32 board definitions on your computer to program the ESP32 CAM. You can find instructions on how to do this [here](https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/).

Setup
-----

1.  Clone this repository to your Raspberry Pi using the command `git clone https://github.com/amirholakoo/GardenV4.git`.

2.  Navigate to the directory containing the repository using the command `cd GardenV4`.

3.  Update the IP address and port of the ESP32 server in the `MonitoringV3_HeadLess.py` script to match your actual setup.

4.  Create the following directories in the same location as your `app.py` file:

    -   `data`: This directory will store the CSV files with the sensor data.
    -   `images`: This directory will store the images captured by the ESP32 CAM.
    -   `static`: This directory will store the images for the web dashboard.
5.  Program the ESP32 CAM with the `ESP32_AI_MonitoringV208.ino` and `CameraWebServer.ino` scripts using the Arduino IDE.

Usage
-----

To run the system, navigate to the directory containing the repository and run the command `python3 MonitoringV3_HeadLess.py`.

To view the dashboard, open a web browser and navigate to `http://<raspberry_pi_ip_address>:5000/dashboard`, replacing `<raspberry_pi_ip_address>` with the actual IP address of your Raspberry Pi.

License
-------

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.

* * * * *

Please replace `<raspberry_pi_ip_address>` with the actual IP address of your Raspberry Pi. You can find the IP address by running the command `hostname -I` on your Raspberry Pi.
