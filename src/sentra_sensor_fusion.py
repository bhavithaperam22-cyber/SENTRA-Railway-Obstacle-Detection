import cv2
import numpy as np
import serial

SERIAL_PORT = "/dev/ttyTHS1"
BAUD_RATE = 115200

FRAME_WIDTH = 640
FRAME_HEIGHT = 480

print("====================================")
print(" SENTRA SENSOR FUSION DEMO ")
print("====================================")

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

if not cap.isOpened():
    print("Camera failed")
    exit()

try:
    ser = serial.Serial(
        SERIAL_PORT,
        BAUD_RATE,
        timeout=0.05
    )
    print("LiDAR Connected")
except Exception as e:
    print(e)
    ser = None

cv2.namedWindow(
    "SENTRA Sensor Fusion",
    cv2.WINDOW_NORMAL
)

cv2.resizeWindow(
    "SENTRA Sensor Fusion",
    900,
    600
)

while True:
    ret, frame = cap.read()

    if not ret:
        continue

    h, w = frame.shape[:2]

    # ----------------------------
    # Read LiDAR Distance
    # ----------------------------
    distance = None

    if ser is not None:
        while ser.in_waiting >= 9:
            data = ser.read(9)
            if data[0] == 0x59 and data[1] == 0x59:
                dist = data[2] + data[3] * 256
                distance = dist / 100.0
                break

    # ----------------------------
    # Fake obstacle box (center)
    # ----------------------------
    box_w = 240
    box_h = 240

    x1 = w // 2 - box_w // 2
    y1 = h // 2 - box_h // 2

    x2 = x1 + box_w
    y2 = y1 + box_h

    color = (0, 255, 255)
    status = "SEARCHING"

    if distance is not None:
        if distance < 1.0:
            color = (0, 0, 255)
            status = "STOP"
        elif distance < 2.5:
            color = (0, 165, 255)
            status = "WARNING"
        else:
            color = (0, 255, 0)
            status = "SAFE"

    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        color,
        3
    )

    cv2.circle(
        frame,
        (w // 2, h // 2),
        6,
        color,
        -1
    )

    cv2.line(
        frame,
        (w // 2 - 20, h // 2),
        (w // 2 + 20, h // 2),
        color,
        2
    )

    cv2.line(
        frame,
        (w // 2, h // 2 - 20),
        (w // 2, h // 2 + 20),
        color,
        2
    )

    if distance is None:
        text = "Obstacle  |  Distance : --"
    else:
        text = f"Obstacle  |  Distance : {distance:.2f} m"

    cv2.putText(
        frame,
        text,
        (x1, y1 - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        color,
        2
    )

    cv2.putText(
        frame,
        f"Status : {status}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        color,
        2
    )

    # ----------------------------
    # Legend
    # ----------------------------
    cv2.putText(
        frame,
        "GREEN : SAFE",
        (20, h - 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        "ORANGE : WARNING",
        (20, h - 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 165, 255),
        2
    )

    cv2.putText(
        frame,
        "RED : STOP",
        (20, h - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 255),
        2
    )

    # Title
    cv2.putText(
        frame,
        "SENTRA Sensor Fusion Demo",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # Display
    cv2.imshow(
        "SENTRA Sensor Fusion",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# ----------------------------
# Cleanup
# ----------------------------
cap.release()

if ser is not None:
    ser.close()

cv2.destroyAllWindows()
