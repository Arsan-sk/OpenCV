# here we are going to perform a corner detection  

import cv2
import numpy as np

img = cv2.imread('assets/chess board.png')
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75)  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # working with detection using grayscale image is better as it reduces the complexity of the image and makes it easier to detect things for algorithm 

# pass : image, max corners to detect, quality level (0-1), minimum distance between corners
# image is to oprate on
# max corner return is the maximum number of corners to detect
# quality level is the minimum quality of corners to be detected like 0 will detect if its barely look like corner while 1 wil detect only the best / fine cornrs best value is 0.01
# minimum distance is the minimum distance between corners to be detected, like may be there exist a corner which to close and part of one corner like curvy corner so it will not count it two if we have set distance 
# (x1,y1) (x2,y2) = sqrt[(x2-x1)^2 + (y2-y1)^2]  this is the formula to calculate the distance between two points to find minimum distance ie pythagorean theorem
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) # return array of x,y like [[100, 200], [150, 250], ...] for each corner detected
# corners = np.intp(corners) # convert the corners to integer type as it is in float type
corners = corners.astype(np.intp) # as previous method are not working so we use astype to convert the corners to integer type


for corner in corners:
    # print(corner) # if we do this it will give [[[x, y]]] for each corner detectedso we need to do like corner = corner[0] to get the x,y coordinates
    x, y = corner.ravel() # ravel() is used to flatten the array i.e. [[[x, y]]] to [x, y] or any kind like [[a,b],[c,d]] give [a,b,c,d] so we can use it to get the x,y coordinates
    cv2.circle(img, (x,y), 5, (0, 255, 0), -1) 

# here we take corner i loop through each corner remaing in inner loop while draw line i corneer to each and do same for all 
for i in range(len(corners)):# outer loop to iterate through each corner 
    for j in range(i+1, len(corners)): #its i+1 because we want to draw a line between each corner and we dont want to draw a line between the same corner so we start from i+1
        corner1 = tuple(corners[i][0]) # e pass [i][0] as its [[x, y]] and we want to get the x,y coordinates so we need to pass [0] to get the first corner
        corner2 = tuple(corners[j][0]) # get the second corner 
        color = tuple(map(lambda x : int(x) ,np.random.randint(0, 255, size=3)))  # gives list of size 3 with random values between 0 and 255 
        # conver list in tuple as needed
        cv2.line(img, corner1, corner2, color, 1) # draw a line between the two corners

cv2.imshow('Chess Board', img)
cv2.waitKey(0)
cv2.destroyAllWindows()