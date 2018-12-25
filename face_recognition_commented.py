# Face Recognition

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # load the cascade for the face.
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') # load the cascade for the eyes.

def detect(frame): 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    for (x, y, w, h) in faces: # For each detected face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = frame[y:y+h, x:x+w] 
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) 
        for (ex, ey, ew, eh) in eyes: 
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2) 
    return frame

video_capture = cv2.VideoCapture(0) # turn the webcam on.

while True: # We repeat infinitely (until break):
    _, frame = video_capture.read()     
    canvas = detect(frame)
    cv2.imshow('Video', canvas) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

video_capture.release() # turn the webcam off.
cv2.destroyAllWindows() # destroy all the windows inside which the images were displayed.
