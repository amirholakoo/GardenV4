🌱 GardenV4: An Automated Garden Monitoring System 🌱
=====================================================

Welcome to GardenV4, a comprehensive solution for monitoring and maintaining your garden using ESP32 CAM, various sensors, and a Raspberry Pi. This system allows you to monitor your garden's conditions and automatically waters your plants when necessary.

This project is a garden monitoring system that uses an ESP32 CAM to monitor your garden boxes. The system collects data such as temperature, humidity, pressure, light level, and soil moisture, and uses this data to automatically water the plants when needed. The data is stored in a CSV file and can be viewed on a dashboard.

Features 
--------

  - Data Collection: The system collects various environmental data using the ESP32 CAM and sensors.
  - Automatic Watering: The system automatically waters the plants when the soil is too dry.
  - Dashboard: The system provides a dashboard where you can view the collected data and the status of the watering system.
  - Manual Pump Control: The system allows you to manually control the pumps from the dashboard.

📚 Table of Contents
--------------------

-   [Requirements]
-   [Hardware Setup]
-   [Software Setup]
-   [Running the Application]
-   [Troubleshooting]
-   [Contributing]

📦 Requirements
---------------

-   Raspberry Pi 4
-   ESP32 CAM
-   Various sensors (temperature, humidity, pressure, light level)
-   Python 3.7 or higher
-   Python libraries: Flask, pandas, numpy, matplotlib, os, glob, shutil, datetime, requests, cv2, PIL, csv, logging

🛠️ Hardware Setup
------------------

1.  ESP32 CAM Setup: Connect your ESP32 CAM to your computer using a USB cable. Make sure the ESP32 CAM is connected to the same network as your Raspberry Pi.

2.  Sensors Setup: Connect your sensors (temperature, humidity, pressure, light level) to your ESP32 CAM. Make sure the sensors are placed in appropriate locations in your garden.

💻 Software Setup
-----------------

1.  Python Installation: If you haven't already, install Python on your Raspberry Pi. You can do this by opening the terminal and running the following command:

`sudo apt-get install python3`

1.  Python Libraries Installation: Install the required Python libraries using pip, Python's package installer. You can do this by running the following command in the terminal:

`pip install flask pandas numpy matplotlib os glob shutil datetime requests opencv-python-headless pillow csv logging`

1.  Clone the Repository: Clone this repository to your Raspberry Pi. You can do this by opening the terminal, navigating to the directory where you want to clone the repository, and running the following command:

`git clone https://github.com/amirholakoo/GardenV4.git`

1.  Data and Image Folders: Navigate to the cloned repository directory and create folders named `data` and `images`. The `data` folder will be used to store the CSV files with the sensor data, and the `images` folder will be used to store the images captured by the ESP32 CAM. You can do this by running the following commands in the terminal:

`cd GardenV4`

`mkdir data`

`mkdir images`

1.  Image Cropping: The system processes the images captured by the ESP32 CAM to detect dry and wet soil, and sprouts. You may need to adjust the cropping parameters in the `MonitoringV3_HeadLess.py` script to match your garden setup. Open the `MonitoringV3_HeadLess.py` file in a text editor, find the lines of code that perform the cropping, and adjust the parameters as needed.

🚀 Running the Application
--------------------------

1.  Update ESP32 Server Address: Open the `MonitoringV3_HeadLess.py` script in a text editor, find the line of code that specifies the IP address and port of the ESP32 server, and replace it with the actual IP address and port of your ESP32 CAM.

2.  Run the Monitoring Script: Open the terminal, navigate to the directory containing the `MonitoringV3_HeadLess.py` script, and run the following command:


`python3 MonitoringV3_HeadLess.py`

1.  Run the Flask Application: In the same terminal window, run the following command:

`python3 app.py`

1.  View the Dashboard: Open a web browser and navigate to `http://<your-raspberry-pi-ip-address>:5000` to view the dashboard.

Manual Pump Control
-------------------
The manual pump control feature allows you to manually turn each pump on or off from the dashboard. This can be useful if you need to water the plants outside of the automatic watering schedule, or if you need to stop the watering for some reason.

To use the manual pump control feature, follow these steps:

- Go to the dashboard by opening a web browser and navigating to the IP address of your Raspberry Pi.
- Click on the "Pump Control" link. This will take you to the pump control page.
- On the pump control page, select the pump number and the state (on or off) from the dropdown menus.
- Click the "Submit" button to send the command to the ESP32. The selected pump will turn on or off as commanded.

🛠️ Troubleshooting
-------------------

If you encounter any issues while setting up or running the application, please check the following:

-   Make sure your ESP32 CAM and Raspberry Pi are connected to the same network.
-   Make sure your ESP32 CAM and sensors are properly connected and functioning.
-   Make sure you've installed Python and all the required Python libraries on your Raspberry Pi.
-   Make sure you've correctly updated the IP address and port of the ESP32 server in the `MonitoringV3_HeadLess.py` script.

🤝 Contributing
---------------

Contributions are welcome! Please feel free to submit a pull request.

👥 Authors 👥
-------------

-   Amirholakoo - *Initial work*

🙏 Acknowledgments 🙏
---------------------

-   Thanks to OpenAI's ChatGPT for assistance with coding and troubleshooting.
