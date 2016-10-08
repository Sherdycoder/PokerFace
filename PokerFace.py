import cv2
import sys
import numpy as np

# Starting arguments and definitions
cascPath = ('haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier(cascPath)
myface = 0
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
        w = w
        h = h

    # Scale the original face image to fit the area of the detect face for each frame
    if np.any(myface) != 0: 
        myfacer = cv2.resize(
            myface,
            (w, h), 
            myface,
            fx = 0,
            fy = 0,
            interpolation = cv2.INTER_NEAREST
        )
 
    # Put the first detected face in ROI and modify the main image        
        frame[y:y+h, x:x+w] = myfacer
   


    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
