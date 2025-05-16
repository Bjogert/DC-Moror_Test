import serial.tools.list_ports

print("Available Serial Ports:")
ports = list(serial.tools.list_ports.comports())

if not ports:
    print("No serial ports detected!")
else:
    for i, port in enumerate(ports):
        print(f"{i+1}. {port.device} - {port.description}")
        
input("\nPress Enter to exit...")
