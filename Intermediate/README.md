# 📂 Intermediate

## 🧠 Overview
The Intermediate section builds upon the basics of OpenCV and introduces more complex concepts like video processing, frame manipulation, and color-based object detection. These techniques are fundamental to computer vision applications ranging from surveillance systems to augmented reality.

## 📘 Learnings & Concepts Covered
- Video capture and processing from webcam feeds
- Frame manipulation (resizing, rotation, and arrangement)
- Color space conversion (BGR to HSV)
- Color-based object detection using masks
- Bitwise operations for image processing
- Real-time video processing techniques

### 🎯 File: `Video_Capturing.py`
#### 📌 Concept/Goal
This script demonstrates how to capture video from a webcam, manipulate the frames by resizing and rotating them, and arrange them into a quad-view display. It showcases frame manipulation techniques that are essential for multi-camera setups, surveillance systems, and creative video applications.

#### ⚙️ Functions & Methods Used
- `cv2.VideoCapture()`
  ```python
  cap = cv2.VideoCapture(0)
  ```
  Creates a video capture object to read frames from a video source. The parameter `0` specifies the default camera. You can also pass a video file path instead.

- `cap.read()`
  ```python
  ret, frame = cap.read()
  ```
  Reads the next frame from the video source. Returns a tuple containing a boolean (`ret`) indicating if the frame was successfully read and the frame itself as a NumPy array.

- `cap.get()`
  ```python
  width = int(cap.get(3))
  height = int(cap.get(4))
  ```
  Retrieves properties of the video capture. Property `3` represents width, and `4` represents height. The method returns float values, which are converted to integers for pixel operations.

- `np.zeros()`
  ```python
  image = np.zeros(frame.shape, np.uint8)
  ```
  Creates a black image (array filled with zeros) with the same dimensions as the input frame. The `np.uint8` parameter specifies 8-bit unsigned integers (0-255) for pixel values.

- `cv2.resize()`
  ```python
  smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
  ```
  Resizes the input frame. The parameters `(0,0)` indicate that the output size is not explicitly specified, while `fx=0.5, fy=0.5` scales the frame to half its original size in both dimensions.

- `cv2.rotate()`
  ```python
  cv2.rotate(smaller_frame, cv2.ROTATE_180)
  ```
  Rotates the input frame by 180 degrees. The constant `cv2.ROTATE_180` specifies the rotation angle.

- `cv2.imshow()`
  ```python
  cv2.imshow('Camera Feed', image)
  ```
  Displays the image in a window with the title 'Camera Feed'.

- `cv2.waitKey()`
  ```python
  cv2.waitKey(1)
  ```
  Waits for a key press for the specified milliseconds (1ms in this case). Returns the ASCII value of the key pressed.

- `cap.release()` and `cv2.destroyAllWindows()`
  ```python
  cap.release()
  cv2.destroyAllWindows()
  ```
  Releases the video capture object and closes all OpenCV windows, freeing up resources.

#### ▶️ How it Works (Step-by-step)
1. Initialize the webcam capture using `cv2.VideoCapture(0)`
2. Enter a continuous loop to process frames
3. Read a frame from the webcam using `cap.read()`
4. Get the dimensions of the frame using `cap.get()`
5. Create a blank image with the same dimensions as the original frame
6. Resize the original frame to half its size using `cv2.resize()`
7. Place the resized frame in each quadrant of the blank image:
   - Top-left: Rotated 180 degrees
   - Bottom-left: Original orientation
   - Top-right: Rotated 180 degrees
   - Bottom-right: Original orientation
8. Display the quad-view image using `cv2.imshow()`
9. Check for the 'q' key press to exit the loop
10. Release resources and close windows when done

#### 📄 External References
- [OpenCV VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [OpenCV resize](https://docs.opencv.org/master/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d)
- [OpenCV rotate](https://docs.opencv.org/master/d2/de8/group__core__array.html#ga4ad01c0978b0ce64baa246811deeac24)
- [OpenCV imshow](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563)
- [OpenCV waitKey](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7)

### 🎯 File: `Color_based_object_tracking.py`
#### 📌 Concept/Goal
This script demonstrates how to detect and track objects based on their color using the HSV color space. It captures video from a webcam, converts the frames to HSV, applies a color filter for blue objects, and displays the result in real-time. This technique is fundamental for applications like object tracking, color filtering, and segmentation.

#### ⚙️ Functions & Methods Used
- `cv2.cvtColor()`
  ```python
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  ```
  Converts the color space of an image. In this case, it converts from BGR (OpenCV's default) to HSV (Hue, Saturation, Value), which is more effective for color-based detection.

- `np.array()`
  ```python
  lower_blue = np.array([100, 150, 0])
  higher_blue = np.array([140, 255, 255])
  ```
  Creates NumPy arrays to define the lower and upper bounds of the blue color in HSV space. The values represent [H, S, V] where H ranges from 0-180 in OpenCV (not 0-360 as in standard HSV), S and V range from 0-255.

- `cv2.inRange()`
  ```python
  mask = cv2.inRange(hsv, lower_blue, higher_blue)
  ```
  Creates a binary mask where pixels within the specified color range are white (255) and pixels outside the range are black (0). Parameters are the input image in HSV format, lower bound array, and upper bound array.

- `cv2.bitwise_and()`
  ```python
  result = cv2.bitwise_and(frame, frame, mask=mask)
  ```
  Performs a bitwise AND operation between the original frame and itself, but only where the mask is white (255). This effectively extracts only the blue regions from the original image.

#### ▶️ How it Works (Step-by-step)
1. Initialize the webcam capture using `cv2.VideoCapture(0)`
2. Enter a continuous loop to process frames
3. Read a frame from the webcam using `cap.read()`
4. Convert the frame from BGR to HSV color space using `cv2.cvtColor()`
5. Define the lower and upper bounds for blue color in HSV space
6. Create a binary mask for blue pixels using `cv2.inRange()`
7. Apply the mask to the original frame using `cv2.bitwise_and()` to extract only the blue regions
8. Display both the mask and the result using `cv2.imshow()`
9. Check for the 'q' key press to exit the loop
10. Release resources and close windows when done

#### 📄 External References
- [OpenCV cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab)
- [OpenCV inRange](https://docs.opencv.org/master/d2/de8/group__core__array.html#ga48af0ab51e36436c5d04340e036ce981)
- [OpenCV bitwise operations](https://docs.opencv.org/master/d2/de8/group__core__array.html#ga60b4d04b251ba5eb1392c34425497e14)
- [HSV Color Space](https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html)

## ▶️ How to Run
```bash
# Navigate to the Intermediate directory
cd "path/to/Open CV/Intermediate"

# Run the video capturing script
python Video_Capturing.py

# Run the color-based object tracking script
python Color_based_object_tracking.py
```

## 📄 Function Documentation
- [cv2.VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [cv2.resize](https://docs.opencv.org/master/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d)
- [cv2.rotate](https://docs.opencv.org/master/d2/de8/group__core__array.html#ga4ad01c0978b0ce64baa246811deeac24)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab)
- [cv2.inRange](https://docs.opencv.org/master/d2/de8/group__core__array.html#ga48af0ab51e36436c5d04340e036ce981)
- [cv2.bitwise_and](https://docs.opencv.org/master/d2/de8/group__core__array.html#ga60b4d04b251ba5eb1392c34425497e14)
- [cv2.imshow](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563)
- [cv2.waitKey](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7)

## 😎 Fun Fact
The HSV color space used in the color detection script was actually invented in 1978 by Alvy Ray Smith, who later co-founded Pixar Animation Studios! It was designed to be more intuitive for artists and is now fundamental in computer vision for isolating objects by color. Next time you watch a Pixar movie, remember that some of the same color science is powering your OpenCV projects!