from cvzone.ClassificationModule import Classifier
import cv2

cap = cv2.VideoCapture(1) #Initialize Video Capture
path = "C:/Learning/Coding/python_learning/LearnCVZone/converted_keras"
maskClassifier = Classifier(f'{path}/keras_model.h5', f'{path}/labels.txt')

while True:
    _, img = cap.read() #Capture frame by frame
    prediction = maskClassifier.getPrediction(img)
    print(prediction) #Print Prediction Result
    cv2.imshow("Image", img)
    cv2.waitKey(1) #Wait for a Ky Press