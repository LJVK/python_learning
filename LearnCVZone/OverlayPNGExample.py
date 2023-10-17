import cv2
import cvzone

#Initialize Camera Capture
cap = cv2.VideoCapture(1)

#Getting the image from URL
imgPNG = cvzone.downloadImageFromUrl(url='https://github.com/cvzone/cvzone/blob/master/Results/cvzoneLogo.png?raw=true',
                                     keepTransparency=True)

#Getting image from directory
# imgPNG = cv2.imread("cvzoneLogo.png", cv2.IMREAD_UNCHANGED)

while True:
    #Read image Frame from Camera
    success, img = cap.read()

    imgOverlay = cvzone.overlayPNG(img, imgPNG, pos=[-30, 100])
    imgOverlay = cvzone.overlayPNG(img, imgPNG, pos=[500, 300])
    imgOverlay = cvzone.overlayPNG(img, imgPNG, pos=[1100, 700])

    cv2.imshow("imgOverlay", imgOverlay)
    cv2.waitKey(1)