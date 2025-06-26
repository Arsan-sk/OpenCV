# here i will be learning a drawing circles , rectangle on screen by using a open cv
# 
# Co-Ordinate system in open cv is different from the normal co-ordinate system we use in maths,
# here the origin (0,0) is at the top-left corner of the image, with the x-axis extending to the right and the y-axis extending downwards. This means that as you move down the image, the y-coordinate increases, and as you move to the right, the x-coordinate increases. 
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) # as its width it goes end i.e left-right at x coordinate
    height = int(cap.get(4)) # as its height it goes end i.e top-down at y coordinate

    img = cv2.line(frame, (0,0), (width,height), (0,0,255), 5)
    # pass : image, start point, end point, color in BGR format, thickness of the line
    img = cv2.line(img, (0,height), (width,0), (0,255,0), 5)

    img = cv2.rectangle(img, (100,100), (200,200), (128,128,128), 5, ) 
    # pass : image, start point, end point, color in BGR format, thickness of the rectangle and -1 for filled rectangle
    # img = cv2.rectangle(img, (200,200), (300,300), (128,128,128), -1) 

    img = cv2.circle(img, (300,300), 55, (0,0,255), -1)
    # pass : image, center point, radius, color in BGR format, thickness of the circle and -1 for filled circle

    # writing a text on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Arsan Is Cool', (20, height - 20), font, 2, (0,0,0), 5, cv2.LINE_AA)
    # pass : image, text, position, font, font scale, color in BGR format, thickness of the text, line type its said in doctn that ots make font look good

    cv2.imshow('Camera Feed', img) # passing img instead of frame as linemust be drawn on frame as we already passed frame in img variable

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
