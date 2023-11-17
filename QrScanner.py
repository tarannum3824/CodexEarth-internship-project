# First, we need to install the required modules for the project: "opencv and pyzbar"
# You can install them using: pip install opencv-python pyzbar

# Import necessary libraries
import cv2
from pyzbar.pyzbar import decode
import time

# Create a video capture object
camera = cv2.VideoCapture(0)

# Set the frame width and height
camera.set(3, 450)
camera.set(4, 450)

camera1 = True

# Continue capturing video until camera1 is False
while camera1:
    # Read a frame from the camera
    success, frame = camera.read()
    
    # Decode the QR code
    for decoded_object in decode(frame):
        print(decoded_object.type)  # Print the type (qrcode, barcode, etc.)
        print(decoded_object.data.decode('utf-8'))  # Print the decoded data
        time.sleep(6)  # Sleep for 6 seconds (adjust as needed)

    # Display the frame with the QR code
    cv2.imshow("Tarannum's_QRCode_Scanner", frame)
    
    # Wait for a key press (waitKey is corrected from waitkey)
    cv2.waitKey(3)
