import cv2
from cvzone.Utils import rotateImage # Import just the rotateImage module alone from cvzone.Utils

# Initialize the video capture
cap = cv2.VideoCapture(1) # capturing video from 2nd webcam (index starts from 0)

# Start the loop to continuously gt frames from webcam
while True:
    # Read a frame from the webcam
    success, img = cap.read() # 'success' will be true if the frame is read successfully, 'img' will contain the frame

    # Rotate the image by 60 degree without keeping the size
    imgRotated60 = rotateImage(img, 60, scale=1, keepSize=False) # Rotate Image 60 degrees, scale it by 1, and don't keep original size

    # Rotate the image by 60 degree while keeping the size
    imgRotated60KeepSize = rotateImage(img, 60, scale=1, keepSize=True)  # Rotate Image 60 degrees, scale it by 1, and keep original size

    # Display the rotated images
    cv2.imshow("img", img)
    cv2.imshow("imgRotated60", imgRotated60) # show the 60 degree rotated image without keeping the size
    cv2.imshow("imgRotated60KeepSize", imgRotated60KeepSize) # show the 60 degree rotated image while keeping the size

    # wait for 1 millisecond between frames
    cv2.waitKey(1) # wait for 1 ms, during which any key can be detected (not being used here)