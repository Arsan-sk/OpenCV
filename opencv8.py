# Face and Eye Detection --
# use prbuild/ preTrain classifiers here to detect/recognise the eyes and faces in camera feed
# Each classfier is trained on specific thing like eyes, faces, birdm and so on they had trained over million of images so when that come on feed the detect it we are just using them here
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)# return locations of all of the faces in given image/feed as we given gray 
    # return [[x,y,w,h],...] co-ordinates of top righ and width and height  for rectange forthe detected face
    # pass : 
    # - base image, 
    # - scale --> to shrink by as it may be image larger than the model train on suggusted is 1.05 
    #  - scale : Smaller value higher acuracy slow performing algorithm || while larger value less acuracy fast performing algorithm
    # - minNeighbours --> parameter specifies howmany neighbours candidate each rectangele should have to retain
    #  - effect quality of detect faces. high value result in less detectionbut with high quality. 3-6 is good
    # then also have minSize and maxSize fordefining rectangle size based on faces if you know like the faces will be small so why make large rectangles just define we ignor in our case
    print(faces)
    # [[224 219 255 255]] like these give coordinates and width and height we can find bottom just by adding w and h in x and y resply
    # [[224 219 255 255]]
    # [[224 219 255 255]]

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x + w , y + h), (0,255,0), 5)
        roi_gray = gray[y:y+h, x:x+w] # now for better eye detection we only search it o region of entrest i.e roi our face as eyes are on face there for we extract only that part of frame image and perform eye detection there only
        roi_frame = frame[y:y+h, x:x+w] # we took y first as at indexing columns come first just so thats it
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_frame, (ex , ey), (ex + ew , ey + eh), (0,0,255), 5)c


    cv2.imshow("Feed", frame)
    

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()