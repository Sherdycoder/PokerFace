import cv2
import sys


cascPath = ("C:\Users\Jonathan Yancey.DESKTOP-F2GU005\Documents\GitHub\Webcam-Face-Detect-master\Webcam-Face-Detect-master\haarcascade_frontalface_default.xml")
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
t = 0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
     
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        t = t + 1      
        if t == 1:     
            myface = frame[y:y+h, x:x+w]
            yset = y
            xset = x  
            hset = h
            wset = w
   
   # Put logo in ROI and modify the main image
    frame[y:y+hset, x:x+wset] = myface
   


    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
