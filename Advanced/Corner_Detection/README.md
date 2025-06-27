# 📂 Corner Detection

## 🧠 Overview
Corner detection is a fundamental technique in computer vision used to identify points of interest in an image where two edges meet. These corners are important features for object recognition, motion tracking, image registration, and 3D reconstruction. This module demonstrates how to detect corners in an image using OpenCV's implementation of the Shi-Tomasi corner detection algorithm.

## 📘 Learnings & Concepts Covered
- Understanding what constitutes a corner in computer vision
- Implementation of the Shi-Tomasi corner detection algorithm
- Processing grayscale images for feature detection
- Drawing and visualizing detected corners
- Connecting corners with lines to create a mesh visualization
- Working with random color generation for visualization

### 🎯 File: `Corner_Detection.py`
#### 📌 Concept/Goal
This script demonstrates how to detect corners in an image using OpenCV's `goodFeaturesToTrack()` function, which implements the Shi-Tomasi corner detection algorithm. The script loads a chessboard image, detects corners, marks them with circles, and connects them with randomly colored lines to create a visual mesh of the detected features.

#### ⚙️ Functions & Methods Used
- `cv2.imread()`
  ```python
  img = cv2.imread('assets/chess board.png')
  ```
  Loads an image from the specified file path. Returns a NumPy array containing the image data.

- `cv2.resize()`
  ```python
  img = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
  ```
  Resizes the input image. The parameters `(0,0)` indicate that the output size is not explicitly specified, while `fx=0.75, fy=0.75` scales the image to 75% of its original size in both dimensions.

- `cv2.cvtColor()`
  ```python
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  ```
  Converts the color space of an image. In this case, it converts from BGR (OpenCV's default) to grayscale, which simplifies the image and makes corner detection more efficient.

- `cv2.goodFeaturesToTrack()`
  ```python
  corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
  ```
  Detects corners in the image using the Shi-Tomasi algorithm. Parameters include:
  - `gray`: The input grayscale image
  - `100`: Maximum number of corners to detect
  - `0.01`: Quality level (minimum eigenvalue threshold, where 1 is the highest quality)
  - `10`: Minimum Euclidean distance between detected corners

- `np.intp()` and `astype()`
  ```python
  corners = corners.astype(np.intp)
  ```
  Converts the floating-point coordinates of detected corners to integer values for pixel operations.

- `ravel()`
  ```python
  x, y = corner.ravel()
  ```
  Flattens a multi-dimensional array into a 1D array. Used here to extract x and y coordinates from the nested corner array.

- `cv2.circle()`
  ```python
  cv2.circle(img, (x,y), 5, (0, 255, 0), -1)
  ```
  Draws a filled circle at the specified coordinates. Parameters include:
  - `img`: The image to draw on
  - `(x,y)`: Center coordinates of the circle
  - `5`: Radius of the circle in pixels
  - `(0, 255, 0)`: BGR color (green in this case)
  - `-1`: Thickness (-1 means filled)

- `cv2.line()`
  ```python
  cv2.line(img, corner1, corner2, color, 1)
  ```
  Draws a line between two points. Parameters include:
  - `img`: The image to draw on
  - `corner1`: Starting point coordinates
  - `corner2`: Ending point coordinates
  - `color`: BGR color tuple
  - `1`: Line thickness in pixels

- `np.random.randint()`
  ```python
  color = tuple(map(lambda x : int(x), np.random.randint(0, 255, size=3)))
  ```
  Generates random integers within a specified range. Used here to create random BGR color values for the lines.

#### ▶️ How it Works (Step-by-step)
1. Load the chessboard image using `cv2.imread()`
2. Resize the image to 75% of its original size using `cv2.resize()`
3. Convert the image to grayscale using `cv2.cvtColor()` for better corner detection
4. Detect corners using `cv2.goodFeaturesToTrack()` with specified parameters
5. Convert corner coordinates to integer type using `astype(np.intp)`
6. For each detected corner:
   - Extract x and y coordinates using `ravel()`
   - Draw a green circle at the corner location using `cv2.circle()`
7. For each pair of corners:
   - Generate a random color using `np.random.randint()`
   - Draw a line between the corners using `cv2.line()`
8. Display the result using `cv2.imshow()`
9. Wait for a key press using `cv2.waitKey(0)`
10. Clean up resources using `cv2.destroyAllWindows()`

#### 📄 External References
- [OpenCV goodFeaturesToTrack](https://docs.opencv.org/master/dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541)
- [Shi-Tomasi Corner Detection Algorithm](https://docs.opencv.org/master/d4/d8c/tutorial_py_shi_tomasi.html)
- [OpenCV Drawing Functions](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html)
- [NumPy Random Module](https://numpy.org/doc/stable/reference/random/index.html)

## ▶️ How to Run
```bash
# Navigate to the Corner_Detection directory
cd "path/to/Open CV/Advanced/Corner_Detection"

# Run the corner detection script
python Corner_Detection.py
```

## 📄 Function Documentation
- [cv2.imread](https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da88aa7049e415041d2ece152)
- [cv2.resize](https://docs.opencv.org/master/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab)
- [cv2.goodFeaturesToTrack](https://docs.opencv.org/master/dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541)
- [cv2.circle](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670)
- [cv2.line](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga7078a9fae8c7e7d13d24dac2520ae4a2)
- [cv2.imshow](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563)
- [cv2.waitKey](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7)

## 😎 Fun Fact
The Shi-Tomasi corner detection algorithm, implemented in OpenCV's `goodFeaturesToTrack()` function, is an improvement over the Harris corner detector. It was developed by Jianbo Shi and Carlo Tomasi in their 1994 paper "Good Features to Track." Their key insight was that corners are better defined by the minimum of two eigenvalues rather than a function of them, making the algorithm more reliable for tracking features across multiple frames. This algorithm is widely used in augmented reality applications to track real-world objects and overlay digital content!