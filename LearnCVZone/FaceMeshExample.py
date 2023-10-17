from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

#Initialize the webcam
cap = cv2.VideoCapture(1)

# Initialize FaceMeshDetector object
# staticMode: If True, the detection happens only once, else every frame
# maxFaces: Maximum number of faces to detect
# minDetectionCon: Minimum detection confidence threshold
# minTrackCon: Minimum tracking confidence threshold
detector = FaceMeshDetector(staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5)

#Start the loop to continuously get the frames from webcam
while True:
    # Read the current frame from the webcam
    # success: Boolean, whether the frame was successfully grabbed
    # img: The current frame
    success, img = cap.read()

    # Find face mesh in the image
    # img: Updated image with the face mesh if draw=True
    # faces: Detected face information
    img, faces = detector.findFaceMesh(img, draw=True)

    #Check if any face detected
    if faces:
        #Loop through each detected face
        for face in faces:
            # Get specific points for the eye
            # leftEyeUpPoint: Point above the left eye
            # leftEyeDownPoint: Point below the left eye
            leftEyeUpPoint = face[159]
            leftEyeDownPoint = face[23]
            # Calculate the vertical distance between the eye points
            # leftEyeVerticalDistance: Distance between points above and below the left eye
            # info: Additional information (like coordinates)
            leftEyeVerticalDistance, info = detector.findDistance(leftEyeUpPoint, leftEyeDownPoint)

            # Print the vertical distance for debugging or information
            print(leftEyeVerticalDistance)

    #Display the image in a window named 'Image'
    cv2.imshow('Image', img)
    #Wait for 1 millisecond to check for any user input, keeping the window open
    cv2.waitKey(1)