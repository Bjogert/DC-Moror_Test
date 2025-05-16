import serial
import time

# Use COM11 as you confirmed this is the correct port
SERIAL_PORT = 'COM11'
BAUD_RATE = 9600

print(f"Attempting to connect to {SERIAL_PORT} at {BAUD_RATE} baud...")

try:
    # Open the serial port
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Successfully connected to {SERIAL_PORT}!")
    
    # Send a test command (Forward)
    print("Sending 'F' command to test motor (Forward)...")
    ser.write(b'F')
    time.sleep(2)
    
    # Send stop command
    print("Sending 'S' command to stop motor...")
    ser.write(b'S')
    time.sleep(1)
    
    # Send another test command (Backward)
    print("Sending 'B' command to test motor (Backward)...")
    ser.write(b'B')
    time.sleep(2)
    
    # Stop the motor again
    print("Sending 'S' command to stop motor...")
    ser.write(b'S')
    
    # Close the connection
    ser.close()
    print("Test completed successfully!")
    
except serial.SerialException as e:
    print(f"Error: {e}")
    print("\nTroubleshooting tips:")
    print("1. Make sure the ESP32 is properly connected via USB")
    print("2. Check that no other programs are using COM11")
    print("3. Try unplugging and reconnecting the ESP32")
    print("4. Make sure you've uploaded the code to the ESP32")
