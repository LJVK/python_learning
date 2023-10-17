import cv2
import cvzone.ColorModule

# Create an instance of colorFinder class with TrackBar=True
myColorFinder = cvzone.ColorModule.ColorFinder(trackBar=False)

# Initializing the video capture using openCV
cap = cv2.VideoCapture(1)

# Set the dimensions of camera feed to 640*480
cap.set(3, 640)
cap.set(4, 480)

#Custom color value for detecting Orange
# 'hmin', 'smin', 'vmin' are the minimum values for Hue, Saturation, and Value.
# 'hmax', 'smax', 'vmax' are the maximum values for Hue, Saturation, and Value.
hsvVals = {'hmin': 10, 'smin': 55, 'vmin': 216, 'hmax': 179, 'smax': 255, 'vmax': 255}

#Main loop to continuously get frames from camera
while True:
    #Read the current frame from the camera
    success, img = cap.read()

    #Use the update method from the colorFinder class to detect the color
    #It returns the masked color image and a binary mask
    imgOrange, mask = myColorFinder.update(img, hsvVals)

    #Stack the original image, the masked color image and the binary mask
    imgStack = cvzone.stackImages([img, imgOrange, mask], 3, 2)

    #Show the stacked images
    cv2.imshow("Image Stack", imgStack)

    #Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

