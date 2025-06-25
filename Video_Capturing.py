import cv2
import numpy as np

cap = cv2.VideoCapture(0) # Open the default camera (0 is the default camera index) can pass video file path as well

# Capturing frame and show them as a video feed in a window named 'Camera Feed'

# while True:
#     ret, frame= cap.read()  # Read a frame from the camera and return image to frame variable and ret is a boolean value indicating if the frame was read successfully
#     cv2.imshow('Camera Feed', frame)  # Display the frame in a window named 'Camera Feed'

#     if cv2.waitKey(1) == ord('q'): # wait for a key press, if 'q' is pressed, exit the loop where ord('q') is used to get the ASCII value of 'q'
#         break




while True:
    ret, frame= cap.read()  # Read a frame from the camera and return image to frame variable and ret is a boolean value indicating if the frame was read successfully
    # capture frame have 17 properties such as width, height, brightness, contrast, saturation, hue, gain, exposure, frames per second (fps), and so on. You can access these properties using the get(Number of the property) method of the VideoCapture object.
    width = int(cap.get(3)) # Get the width of the frame by default its floot we need int for slice``
    height = int(cap.get(4)) # Get the height of the frame by default its floot we need int for slice``

    image = np.zeros(frame.shape, np.uint8) # Create a black image with the same shape as the frame black bcz np.zeros() creates an array filled with zeros, and np.uint8 specifies the data type of the array elements as unsigned 8-bit integers (0 to 255)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) # reduce frame from both H and W by half

    # now distrubute smaller_frame in 4 part of the main frame size as its now half of the main frame size
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top-left corner, 0:5 can be written as :5
    image[height//2:, :width//2] = smaller_frame  # Bottom-left corner
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top-right corner, 5:end can be written as 5:
    image[height//2:, width//2:] = smaller_frame  # Bottom-right corner

    cv2.imshow('Camera Feed', image)  # Display the 4 frame in a window named 'Camera Feed'

    if cv2.waitKey(1) == ord('q'): # wait for a key press, if 'q' is pressed, exit the loop where ord('q') is used to get the ASCII value of 'q'
        break






cap.release()  # Release the camera
cv2.destroyAllWindows()  # Destroy all the windows created by OpenCV