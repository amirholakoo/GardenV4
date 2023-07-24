from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
from shutil import copyfile
from datetime import datetime, timedelta
from flask import send_from_directory


app = Flask(__name__, static_url_path='/static')


from datetime import datetime

@app.route('/dashboard')
def dashboard():
    # Gather data for the dashboard
    csv_files = glob.glob('data/*_soil_data.csv')
    ip_addresses = [os.path.basename(file).replace('_soil_data.csv', '') for file in csv_files]

    # For each IP address, get the latest image and all data
    cameras = []
    for ip_address in ip_addresses:
        # Get the latest image
        camera_image_folder = f'images/{ip_address.replace(".", "_")}'
        latest_image_file = latest_file_in_dir(camera_image_folder, 'static')

        # Get all data
        data = pd.read_csv(f'data/{ip_address}_soil_data.csv')

        # Find the last watering times
        last_start_watering_time = None
        last_stop_watering_time = None
        # Convert 'start_watering_time' and 'stop_watering_time' to datetime type
        data['start_watering_time'] = pd.to_datetime(data['start_watering_time'], errors='coerce')
        data['stop_watering_time'] = pd.to_datetime(data['stop_watering_time'], errors='coerce')

        # Find the last non-null watering times and format them
        last_start_watering_time = pd.to_datetime(data['start_watering_time'].dropna().tail(1).values[0]).strftime('%Y-%m-%d %H:%M:%S') if not data['start_watering_time'].dropna().empty else 'None'
        last_stop_watering_time = pd.to_datetime(data['stop_watering_time'].dropna().tail(1).values[0]).strftime('%Y-%m-%d %H:%M:%S') if not data['stop_watering_time'].dropna().empty else 'None'




        cameras.append({
            'ip_address': ip_address,
            'latest_image': latest_image_file,
            'data': data.iloc[-1],
            'start_watering_time': last_start_watering_time,
            'stop_watering_time': last_stop_watering_time
        })

    # Render the dashboard template
    return render_template('dashboard.html', cameras=cameras)


@app.route('/data/<path:filename>')
def serve_data(filename):
    return send_from_directory('data', filename)



@app.route('/')
def index():
    
    # Read the log file
    log_info = read_last_24_hours('monitoring.log')
        
    # Find all CSV files in the data directory
    csv_files = glob.glob('data/*_soil_data.csv')

    # Extract the IP addresses from the file names
    ip_addresses = [os.path.basename(file).replace('_soil_data.csv', '') for file in csv_files]

    # Render the index page
    return render_template('index.html', ip_addresses=ip_addresses, log_info=log_info)


@app.route('/camera/<ip_address>')
def camera(ip_address):
    csv_file = f'data/{ip_address}_soil_data.csv'  # Path to your CSV file

    # Check if the file exists
    if not os.path.isfile(csv_file):
        return "Data file not found"

    # Load the data
    data = pd.read_csv(csv_file)

    # Generate the graphs and save them as images
    graph_types = ['num_dry_pixels', 'num_wet_pixels', 'num_sprout_pixels', 'temperature', 'humidity', 'pressure', 'light_level']
    graph_titles = ['Number of Dry Pixels', 'Number of Wet Pixels', 'Number of Sprout Pixels', 'Temperature', 'Humidity', 'Pressure', 'Light Level']

    filenames = [generate_graph(data, graph_type, title, f"{ip_address}_{graph_type}.png") for graph_type, title in zip(graph_types, graph_titles)]

    # Get latest image 
    camera_image_folder = f'images/{ip_address.replace(".", "_")}'
    latest_image_file = latest_file_in_dir(camera_image_folder, 'static')
    
    # Read the log file
    log_filename = f'monitoring_{ip_address.replace(".", "_")}.log'
    log_info = read_last_8_hours(log_filename)
    
    gen_filename = ('monitoring.log')
    gen_log = read_last_24_hours(gen_filename)
    



    # Render the camera page
    
    #return render_template('camera.html', ip_address=ip_address, data=data)
    return render_template('camera.html', filenames=filenames, ip_address=ip_address, latest_image=latest_image_file, log_info=log_info, gen_log=gen_log)

def latest_file_in_dir(dir, static_dir):
    files = glob.glob(dir + '/*')
    if files:
        latest_file = max(files, key=os.path.getctime)
        latest_filename = latest_file.split('/')[-1]  # get file name only
        pure_filename = latest_filename.split("\\")[-1]  # get only the filename without IP

        # Create static directory if not exists
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)

        # Copy file to static folder
        copyfile(latest_file, f"{static_dir}/{pure_filename}")

        return pure_filename
    else:
        return None
    
def read_last_24_hours(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Get the current time
    now = datetime.now()

    # Filter the lines to include only the last 24 hours
    lines_last_24_hours = [line for line in lines if now - datetime.strptime(line.split()[0] + ' ' + line.split()[1], '%Y-%m-%d %H:%M:%S,%f') <= timedelta(hours=24)]

    return ''.join(lines_last_24_hours)

def read_last_8_hours(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Get the current time
    now = datetime.now()

    # Filter the lines to include only the last 24 hours
    lines_last_8_hours = [line for line in lines if now - datetime.strptime(line.split()[0] + ' ' + line.split()[1], '%Y-%m-%d %H:%M:%S,%f') <= timedelta(hours=8)]

    return ''.join(lines_last_8_hours)

def generate_graph(data, column, title, filename):
    plt.figure()
    plt.plot(data['timestamp'], data[column])
    plt.title(title)
    plt.grid(True)
    plt.savefig('static/' + filename)  # Save the graph as an image in the static folder
    return filename

if __name__ == '__main__':
    app.run(debug=True)
