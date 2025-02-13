import serial
import time

printer_port = 'COM3'  # name of serial port
baud_rate = 9600  # baud rate for printer

# Data to send to the printer
data = "hello world \n"

# Try connecting to the printer
try:
    # Open the serial port
    with serial.Serial(printer_port, baud_rate, timeout=1) as ser:
        print(f"Connected to printer at {printer_port}")

        # Send data to the printer
        ser.write(data.encode())  # send the data
        print("Data sent to the printer.")

        # Optionally wait a bit to ensure printing is completed
        time.sleep(2)

except serial.SerialException as e:
    print(f"Error: {e}")