import cv2

# Open USB webcam
cap = cv2.VideoCapture(0)

# Set camera format and resolution
cap.set(cv2.CAP_PROP_FOURCC,
        cv2.VideoWriter_fourcc(*'MJPG'))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Check camera
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Camera started successfully")
print("Press 'q' to quit")

while True:

    # Capture frame
    ret, frame = cap.read()

    if not ret:
        print("Frame not received")
        break

    # Display live camera feed
    cv2.imshow("Live Camera", frame)

    # Press q to close
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# Release camera
cap.release()
cv2.destroyAllWindows()
