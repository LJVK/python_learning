import cv2
import cvzone

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    # cv2.rectangle(img, (900, 150), (500, 700), (255, 0, 255), 3)
    # cv2.putText(img, "CVZone", (550, 150), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 5)
    # cvzone.cornerRect(img, (450, 250, 500, 400))
    cvzone.putTextRect(img, "CVZone", (200, 300), border=5, offset=20)
    cv2.imshow("Image", img)
    cv2.waitKey(1)