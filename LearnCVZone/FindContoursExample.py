import cv2
import cvzone
import numpy as np

# Download an image containing shapes from a given url
imgshapes = cvzone.downloadImageFromUrl(url='https://github.com/cvzone/cvzone/blob/master/Results/shapes.png?raw=true')

# Perform edge detection using canny algorithm
imgCanny = cv2.Canny(imgshapes, 50, 150)

# Dilate the shapes to strengthen the detected contours
imgDilated = cv2.dilate(imgCanny, np.ones((5,5), np.uint8), iterations=1)

# Find Contours in the image without any corner filtering
imgContours, conFound = cvzone.findContours(imgshapes, imgDilated, minArea=1000, sort=True, filter=None,
                                            drawCon=True, c=(255,0,0), ct=(255,0,255), retrType=cv2.RETR_EXTERNAL,
                                            approxType=cv2.CHAIN_APPROX_NONE)


# Find Contours in the image and filter them based on corner points (either 3 or 4 corners)
imgContoursFiltered, conFoundFiltered = cvzone.findContours(imgshapes, imgDilated, minArea=1000, sort=True, filter=[3,4],
                                            drawCon=True, c=(255,0,0), ct=(255,0,255), retrType=cv2.RETR_EXTERNAL,
                                            approxType=cv2.CHAIN_APPROX_NONE)

# Display the image with all found contours
cv2.imshow("imgContours", imgContours)

# Display the image with filtered contours (either 3 or 4 corners)
cv2.imshow("imgContoursFiltered", imgContoursFiltered)

# Wait until a key is pressed to close the window
cv2.waitKey(0)

