from flask import Flask, render_template, jsonify
from gpiozero import LED, DistanceSensor, Buzzer
from threading import Thread
from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep

app = Flask(__name__)

ledGreen = LED(6)
ledYellow = LED(19)
ledRed = LED(26)
reading = True
sensor = DistanceSensor(echo=20, trigger=21)
buzzer = Buzzer(18)
message = {"distance": "---", "status": "Unknown"}  # Initialize with "Unknown" status

def safe_exit(signum, frame):
    exit(1)

def get_status(distance):
    if distance < 10:
        status = "Risk"
    elif distance < 30:
        status = "Caution"
    else:
        status = "Safe"
        
    return status
    
def read_distance():
    global message
    while reading:
        distance = sensor.distance * 100  # Convert to cm
        status = get_status(distance)
        message = {"distance": distance, "status": status}
        print("Distance:", distance, "Status:", status)
        sleep(0.1)
        if distance > 30:
            ledGreen.on()
            ledYellow.off()
            ledRed.off()
            buzzer.off()
        elif distance > 20:
            ledGreen.off()
            ledYellow.on()
            ledRed.off()
            buzzer.beep(0.05, 0.05, 1)
        else:
            ledGreen.off()
            ledYellow.off()
            ledRed.on()
            buzzer.on()
        sleep(0.1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_distance')
def get_distance():
    global message
    distance = sensor.distance * 100  # Convert to cm
    status = get_status(distance)
    message = {"distance": distance, "status": status}
    return jsonify(message)

if __name__ == '__main__':
    reader = Thread(target=read_distance, daemon=True)
    reader.start()
    app.run(host='0.0.0.0', port=8000)
    try:
        pause()
    except KeyboardInterrupt:
        pass
    finally:
        ledGreen.close()
        ledYellow.close()
        ledRed.close()
        buzzer.close()
        reading = False
        sensor.close()
