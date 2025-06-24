#HSV --> Hue(colour or Shade) Saturation  & lightness Value

# what we do here and how does it work in back ground --> here 
# we are using the HSV color space to detect a specific color (blue) in the video feed from the camera.
# The HSV color space is often more effective for color detection than the RGB color space because it separates color information (hue) from intensity (saturation and value), making it easier to define color ranges.
# The code captures video from the camera, converts each frame to the HSV color space, creates
# a mask for the blue color, and then applies that mask to the original frame to isolate the blue color.
# The result is displayed in a window, and the program continues to run until the user presses the 'q' key to quit.
# This is useful for applications like color-based object tracking or filtering out specific colors from a video


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # passimage to conver and then formate in which you want to convert
    lower_blue = np.array([100, 150, 0]) # lower bound for blue color in HSV
    higher_blue = np.array([140, 255, 255]) # upper bound for blue color in HSV

    mask = cv2.inRange(hsv, lower_blue, higher_blue) # pass image, lower bound and upper bound to get the mask of the blue color i.e. we get a binary image where the pixels within the specified range are white (255) and those outside the range are black (0).
    # how mask work --> its convert all pixel in range to white and all pixel outside the range to black, so what we do to it is we pass this mask to the original image to get only the blue color in the image as we

    result = cv2.bitwise_and(frame, frame, mask=mask) # pass image, image and mask to get the result of the blue color

    cv2.imshow('Camera Feed', result)
    cv2.imshow('Mask', mask) # showing the mask of the blue color

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()