import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import cv2

# Initialize the web cam
cap = cv2.VideoCapture(0)
# Set the frame width to 640 pixels
# cap.set(3, 640)
# Set the frame height to 480 pixels
# cap.set(4, 480)
# Initialize the Selfi Segmentation class, which will be used for background removal
# model parameter is 0 or 1, 0 - regular 1 - landscape (faster)
segmentor = SelfiSegmentation(model=0)

# Infinite loop to capture frames from webcam
while True:
    success, img = cap.read()
    # Use the Selfisegmentation class to remove the background
    # Replace it with magenta background (255, 0, 255)
    # imgBG can be a color or image as well, must be the same size as the original image
    # cutThreshold is the sensitivity of the segmentation
    imgOut = segmentor.removeBG(img, imgBg=(255, 0, 255), cutThreshold=0.1)
    # Stack the original image and the image with background removed side by side
    imgStacked = cvzone.stackImages([img, imgOut], cols=2, scale=1)
    # Display the stacked images
    cv2.imshow("Image", imgStacked)
    # Check for 'q' key press to break the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
