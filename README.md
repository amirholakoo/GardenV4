🌱 Garden Monitoring System 🌱
==============================

This repository contains the code for a smart garden monitoring system that uses an ESP32 CAM to keep an eye on your garden boxes. The system captures images of the garden boxes, processes these images to detect dry and wet soil and sprouts, and decides if the garden needs watering based on sensor data. All the data is logged to a CSV file and a beautiful dashboard is provided for visualizing the data.

🚀 Getting Started 🚀
---------------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### 📋 Prerequisites 📋

#### 🛠️ Hardware 🛠️

The project requires the following hardware:

-   ESP32 CAM: This is a small camera module with a built-in ESP32 chip that is used to capture images of the garden boxes.
-   Various sensors: The project uses sensors to measure temperature, humidity, pressure, and light level. You can use any sensors that are compatible with the ESP32, but the code is currently set up to work with the following sensors:
    -   Temperature and humidity: DHT22
    -   Pressure: BMP280
    -   Light level: BH1750
-   Water pump: The project uses a water pump to water the garden. You can use any pump that can be controlled by the ESP32.

#### 💻 Software 💻

The project requires Python 3 and several Python libraries. You can install Python 3 from the [official website](https://www.python.org/downloads/). Once Python is installed, you can install the required libraries using pip, Python's package installer. Open a terminal and run the following commands:

`pip install flask`

`pip install pandas`

`pip install numpy`

`pip install matplotlib`

`pip install opencv-python`

`pip install Pillow`

`pip install requests`

### 📥 Installing 📥

To install the project, you need to clone the repository to your local machine. You can do this using Git, a version control system. If you don't have Git installed, you can download it from the [official website](https://git-scm.com/downloads). Once Git is installed, open a terminal, navigate to the directory where you want to install the project, and run the following command:

`git clone https://github.com/amirholakoo/GardenV4.git`

This will create a new directory named "GardenV4" containing the project files.

### ⚙️ Configuring the Project ⚙️

Before you can run the project, you need to set up the ESP32 server and update the IP address and port in the "MonitoringV3_HeadLess.py" script to match your actual setup. The IP address and port are used to connect to the ESP32 server to capture images and sensor data. You need to replace the placeholders in the script with the actual IP address and port of your ESP32 server.

You also need to create a "data" directory in the project directory to store the CSV files, and an "images" directory to store the images captured by the ESP32 CAM. The "images" directory should have a subdirectory for each ESP32 CAM, named with the IP address of the ESP32 CAM with dots replaced by underscores.

In the "MonitoringV3_HeadLess.py" script, you may need to adjust the following variables based on your specific setup and preferences:

-   `min_light`: This is the minimum light level required for the system to water the garden. If the light level is below this value, the system will not water the garden, regardless of the soil condition. This is to prevent watering during the night or when it's too cloudy.
-   `min_dry_pixels`: This is the minimum number of dry pixels required for the system to start watering. If the number of dry pixels in the image is below this value, the system will not water the garden, even if the light level is above `min_light`.
-   `min_wet_pixels`: This is the minimum number of wet pixels required for the system to stop watering. If the number of wet pixels in the image is below this value, the system will continue watering, even if the number of dry pixels is below `min_dry_pixels`.

### 🏃 Running the Project 🏃

Once everything is set up, you can run the project by navigating to the project directory in the terminal and running the following command:

`python3 MonitoringV3_HeadLess.py`

This will start the garden monitoring system and the dashboard server. You can view the dashboard by opening a web browser and navigating to "<http://localhost:5000/dashboard>".

🛠️ Built With 🛠️
------------------

-   [Python](https://www.python.org/) - The programming language used
-   [Flask](https://flask.palletsprojects.com/) - The web framework used
-   [OpenCV](https://opencv.org/) - Used for image processing
-   [Pandas](https://pandas.pydata.org/) - Used for data manipulation and analysis
-   [Matplotlib](https://matplotlib.org/) - Used for data visualization

👥 Authors 👥
-------------

-   Amirholakoo - *Initial work*

🙏 Acknowledgments 🙏
---------------------

-   Thanks to OpenAI's ChatGPT for assistance with coding and troubleshooting.
