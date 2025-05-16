import serial
import keyboard
import time

# Replace 'COM3' with your ESP32's COM port (e.g., 'COM4', 'COM5', etc.)
SERIAL_PORT = 'COM11'
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
except serial.SerialException:
    print(f"Could not open serial port {SERIAL_PORT}. Check your connection and port name.")
    exit(1)

print("Use UP for Forward, DOWN for Backward. Press ESC to exit.")

last_cmd = None

try:
    while True:
        if keyboard.is_pressed('up'):
            if last_cmd != 'F':
                ser.write(b'F')
                last_cmd = 'F'
                print('Forward')
            time.sleep(0.1)
        elif keyboard.is_pressed('down'):
            if last_cmd != 'B':
                ser.write(b'B')
                last_cmd = 'B'
                print('Backward')
            time.sleep(0.1)
        elif keyboard.is_pressed('esc'):
            print('Exiting...')
            break
        else:
            # If no key is pressed, don't spam stop
            pass
        time.sleep(0.01)
finally:
    ser.close()
