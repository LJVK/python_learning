import cv2
import cvzone

# Initialize camera capture
cap= cv2.VideoCapture(1)

# Start an infinite loop to continuously capture the frames
while True:
    # Read image frame from camera
    success, img = cap.read()
    # Convert the image to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Resize the image to be smaller (0.1* of original image)
    imgSmall = cv2.resize(img, (0,0), None, 0.1, 0.1)
    # Resize the image to be larger (3* of original image)
    imgBig = cv2.resize(img, (0,0), None, 3, 3)
    # Apply Canny Edge Detection on the grayscale image
    imgCanny = cv2.Canny(imgGray, 50, 150)
    # Convert the Image to HSV color space
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create a list of all processed images
    imgList = [img, imgGray, imgCanny, imgSmall, imgBig, imgHSV]

    # Stack the images together using the cvzone's stackImages function
    stackedImg = cvzone.stackImages(imgList, 3, 0.5)

    # Display the stacked images
    cv2.imshow("stackedImages", stackedImg)

    # Wait for 1 ms, this will also allow for keyboard inputs
    cv2.waitKey(1)
