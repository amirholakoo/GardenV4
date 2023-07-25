Garden Monitoring System
========================

This repository contains the code for a Garden Monitoring System using an ESP32 CAM and a Raspberry Pi. The system captures images of the garden, processes the images to detect soil conditions and sprouts, and decides whether to water the garden based on the sensor data. The data is logged to a CSV file and displayed on a web-based dashboard.

Table of Contents
-----------------

-   [Installation](https://chat.openai.com/c/92bacfaf-5b3f-45b6-b93c-33a469abb1e1#installation)
-   [Setup](https://chat.openai.com/c/92bacfaf-5b3f-45b6-b93c-33a469abb1e1#setup)

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

Running the Project
-------------------

Before you can run the project, you need to set up the ESP32 server and update the IP address and port in the "MonitoringV3_HeadLess.py" script to match your actual setup.

You also need to create a "data" directory in the project directory to store the CSV files, and an "images" directory to store the images captured by the ESP32 CAM. The "images" directory should have a subdirectory for each ESP32 CAM, named with the IP address of the ESP32 CAM with dots replaced by underscores.

Once everything is set up, you can run the project by navigating to the project directory in the terminal and running the following command:

`python3 MonitoringV3_HeadLess.py`

This will start the garden monitoring system and the dashboard server. You can view the dashboard by opening a web browser and navigating to "<http://localhost:5000/dashboard>".

Built With
----------

-   [Python](https://www.python.org/) - The programming language used
-   [Flask](https://flask.palletsprojects.com/) - The web framework used
-   [OpenCV](https://opencv.org/) - Used for image processing
-   [Pandas](https://pandas.pydata.org/) - Used for data manipulation and analysis
-   [Matplotlib](https://matplotlib.org/) - Used for data visualization

Authors
-------

-   Amirholakoo - *Initial work*

Acknowledgments
---------------

-   Thanks to OpenAI's ChatGPT for assistance with coding and troubleshooting.
* * * * *
