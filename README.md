# Bus-Parking-Sensors
ParkSense: Ultrasonic Bus Aid. A project for WCM555 at Seneca

[User Manual](WCM-BusPark-Manual.pdf)

## Overview
ParkSense revolutionizes bus parking with ultrasonic technology, enhancing safety and efficiency in urban transit. By providing real-time proximity alerts, it aims to minimize collision risks, ensuring secure parking operations.

## Features
- **Ultrasonic Distance Sensing**: Measures distances to nearby obstacles, providing real-time data for safe parking.
- **Real-Time Alerts**: Visual and auditory notifications to guide bus drivers during parking maneuvers.
- **Web-Based Visualization**: User-friendly interface for drivers, displaying safe, caution, and risk zones based on proximity.

## Components
- Ultrasonic Sensor: Detects objects and measures distances.
- Raspberry Pi: Processes sensor data and controls the system.
- Buzzer & RGB LED: For auditory and visual alerts.
- Custom Web Interface: Displays distance and safety zone information.

## Installation
1. Set up your Raspberry Pi.
2. Connect the ultrasonic sensor, buzzer, and RGB LED to the Raspberry Pi.
3. Upload the Python script to the Raspberry Pi.
4. Configure the web server to host the visualization interface.

## Usage
1. Power on the Raspberry Pi and ensure all components are connected.
2. Access the web-based interface through any supported browser.
3. The interface updates in real-time as the bus approaches obstacles.

## Development
This project was developed with:
- **Python**: For sensor data processing and server-side logic.
- **HTML/CSS**: For crafting the web-based visualization interface.

## References
- Ultrasonic sensor usage and Raspberry Pi integration.
- Web development for real-time data visualization.

For detailed setup instructions and more information, please refer to the project documentation.
