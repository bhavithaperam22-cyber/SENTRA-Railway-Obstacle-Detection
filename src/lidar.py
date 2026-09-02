import serial
import time

# ---------------------------------------
# TF02-Pro UART Settings
# ---------------------------------------

SERIAL_PORT = '/dev/ttyTHS1'
BAUD_RATE = 115200

print("Opening LiDAR connection...")

try:
    ser = serial.Serial(
        port=SERIAL_PORT,
        baudrate=BAUD_RATE,
        timeout=1
    )

    print("LiDAR connected successfully")
    print("Reading distance...")
    print("Press Ctrl+C to stop\n")

except Exception as e:
    print("Cannot open serial port:", e)
    exit()


try:
    while True:

        # Look for the TF02-Pro frame header
        if ser.read() == b'\x59':

            if ser.read() == b'\x59':

                # Read remaining 7 bytes
                data = ser.read(7)

                if len(data) == 7:

                    # Full frame:
                    # 0x59 0x59 + 7 bytes
                    frame = [0x59, 0x59] + list(data)

                    # Calculate checksum
                    checksum = sum(frame[0:8]) & 0xFF

                    # Verify checksum
                    if checksum == frame[8]:

                        # Distance in centimeters
                        distance_cm = frame[2] + (frame[3] << 8)

                        # Signal strength
                        strength = frame[4] + (frame[5] << 8)

                        # Temperature
                        temperature = (
                            frame[6] + (frame[7] << 8)
                        ) / 8.0 - 256

                        # Convert distance to meters
                        distance_m = distance_cm / 100.0

                        print(
                            "Distance: {:.2f} m | {} cm | "
                            "Strength: {} | Temperature: {:.1f} C"
                            .format(
                                distance_m,
                                distance_cm,
                                strength,
                                temperature
                            )
                        )

except KeyboardInterrupt:

    print("\nStopping LiDAR...")

finally:

    ser.close()
    print("Serial connection closed.")
