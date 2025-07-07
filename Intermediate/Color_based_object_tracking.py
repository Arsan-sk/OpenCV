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

import numpy as np

color_bounds = {
    "red1": {
        "lower": np.array([0, 120, 70]),
        "upper": np.array([10, 255, 255])
    },
    "red2": {
        "lower": np.array([170, 120, 70]),
        "upper": np.array([180, 255, 255])
    },
    "green": {
        "lower": np.array([40, 70, 70]),
        "upper": np.array([80, 255, 255])
    },
    "blue": {
        "lower": np.array([100, 150, 0]),
        "upper": np.array([140, 255, 255])
    },
    "yellow": {
        "lower": np.array([20, 100, 100]),
        "upper": np.array([30, 255, 255])
    },
    "orange": {
        "lower": np.array([10, 100, 20]),
        "upper": np.array([20, 255, 255])
    },
    "white": {
        "lower": np.array([0, 0, 200]),
        "upper": np.array([180, 55, 255])
    },
    "black": {
        "lower": np.array([0, 0, 0]),
        "upper": np.array([180, 255, 30])
    },
    "gray": {
        "lower": np.array([0, 0, 40]),
        "upper": np.array([180, 20, 200])
    },
    "purple": {
        "lower": np.array([125, 50, 50]),
        "upper": np.array([155, 255, 255])
    },
    "cyan": {
        "lower": np.array([85, 100, 100]),
        "upper": np.array([100, 255, 255])
    },
    "brown": {
        "lower": np.array([10, 100, 20]),
        "upper": np.array([20, 255, 200])
    }
}


cap = cv2.VideoCapture(0)

print("\n|| Color Based Object Detecting ||")
print(100*"-")
print("Foloowing is a list of color you can detect using this program\n")
print("1.Red\t2.Green\n3.Blue\t4.Yellow\n5.White\t6.Black\n7.Gray\t8.Orange\n9.Cyan\t10.Purple\n11.Brown\n")

color_to_detect = input("Enter the color to detect: ")

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # passimage to conver and then formate in which you want to convert

    if color_to_detect == "red":
        # Combine both red ranges
        lower1 = color_bounds["red1"]["lower"]
        upper1 = color_bounds["red1"]["upper"]
        lower2 = color_bounds["red2"]["lower"]
        upper2 = color_bounds["red2"]["upper"]
        mask1 = cv2.inRange(hsv, lower1, upper1)
        mask2 = cv2.inRange(hsv, lower2, upper2)
        mask = cv2.bitwise_or(mask1, mask2)
    else:
        lower_bond = color_bounds[color_to_detect]["lower"]
        upper_bond = color_bounds[color_to_detect]["upper"]
        mask = cv2.inRange(hsv, lower_bond, upper_bond)

    # pass image, lower bound and upper bound to get the mask of the blue color i.e. we get a binary image where the pixels within the specified range are white (255) and those outside the range are black (0).
    # how mask work --> its convert all pixel in range to white and all pixel outside the range to black, so what we do to it is we pass this mask to the original image to get only the blue color in the image as we

    result = cv2.bitwise_and(frame, frame, mask=mask) # pass image, image and mask to get the result of the blue color

    cv2.imshow('Camera Feed', result)
    cv2.imshow('Mask', mask) # showing the mask of the blue color

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()