# 📂 Template Matching

## 🧠 Overview
Template matching is a technique in digital image processing for finding small parts of an image that match a template image. This module demonstrates how to use OpenCV's template matching functionality to locate a specific object (template) within a larger image. The technique compares pixel values between the template and source image to find the best match using various correlation methods.

## 📘 Learnings & Concepts Covered
- Understanding template matching concepts and algorithms
- Working with multiple matching methods and comparing their results
- Processing grayscale images for improved matching
- Visualizing matching results with bounding boxes
- Handling different template matching algorithms:
  - Cross-Correlation methods
  - Squared Difference methods
  - Normalized variants for better accuracy

### 🎯 File: `Template_Matching.py`
#### 📌 Concept/Goal
This script demonstrates how to find a specific object (a soccer ball) within a larger image (a soccer game scene) using template matching. It implements all six template matching methods available in OpenCV, compares their results, and visualizes the best match for each method by drawing a rectangle around the detected object. This technique is useful for object detection, image registration, and feature tracking.

#### ⚙️ Functions & Methods Used
- `cv2.imread()`
  ```python
  img = cv2.imread("assets/socerPlay.jpg", 0)
  template = cv2.imread("assets/socerBall.png", 0)
  ```
  Loads images from the specified file paths. The parameter `0` loads the images in grayscale mode, which simplifies processing and improves matching performance.

- `template.shape`
  ```python
  h, w = template.shape
  ```
  Retrieves the dimensions (height and width) of the template image. For grayscale images, `.shape` returns a tuple of (height, width).

- `cv2.matchTemplate()`
  ```python
  result = cv2.matchTemplate(img2, template, method)
  ```
  Performs template matching between the source image and template using the specified method. Returns a grayscale image where each pixel denotes how much the neighborhood of that pixel matches the template. Parameters include:
  - `img2`: The source image
  - `template`: The template image to find
  - `method`: The matching method to use (one of the six available methods)

- `cv2.minMaxLoc()`
  ```python
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  ```
  Finds the global minimum and maximum values in the result array and their locations. Returns:
  - `min_val`: Minimum value in the result
  - `max_val`: Maximum value in the result
  - `min_loc`: (x, y) location of the minimum value
  - `max_loc`: (x, y) location of the maximum value

- `cv2.rectangle()`
  ```python
  cv2.rectangle(img2, location, bottom_right, 255, 5)
  ```
  Draws a rectangle on the image. Parameters include:
  - `img2`: The image to draw on
  - `location`: Top-left corner coordinates
  - `bottom_right`: Bottom-right corner coordinates
  - `255`: Grayscale color (white in this case)
  - `5`: Line thickness in pixels

#### ▶️ How it Works (Step-by-step)
1. Load the source image (soccer game) and template image (soccer ball) in grayscale mode using `cv2.imread()`
2. Get the dimensions (height and width) of the template image using `template.shape`
3. Define an array of six template matching methods available in OpenCV:
   - `cv2.TM_CCOEFF`: Correlation Coefficient
   - `cv2.TM_CCOEFF_NORMED`: Normalized Correlation Coefficient
   - `cv2.TM_CCORR`: Cross Correlation
   - `cv2.TM_CCORR_NORMED`: Normalized Cross Correlation
   - `cv2.TM_SQDIFF`: Squared Difference
   - `cv2.TM_SQDIFF_NORMED`: Normalized Squared Difference
4. For each matching method:
   - Create a copy of the source image to draw on
   - Perform template matching using `cv2.matchTemplate()`
   - Find the best match location using `cv2.minMaxLoc()`
   - Determine the correct location based on the method type:
     - For `TM_SQDIFF` and `TM_SQDIFF_NORMED`, use the minimum location
     - For all other methods, use the maximum location
   - Calculate the bottom-right corner of the match by adding the template dimensions to the top-left corner
   - Draw a rectangle around the matched area using `cv2.rectangle()`
   - Display the result and wait for a key press

#### 📄 External References
- [OpenCV Template Matching](https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html)
- [Template Matching Theory](https://docs.opencv.org/master/df/dfb/group__imgproc__object.html#ga586ebfb0a7fb604b35a23d85391329be)
- [Different Matching Methods Comparison](https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html)

## ▶️ How to Run
```bash
# Navigate to the Template_Matching directory
cd "path/to/Open CV/Advanced/Template_Matching"

# Run the template matching script
python Template_Matching.py
```

## 📄 Function Documentation
- [cv2.imread](https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da88aa7049e415041d2ece152)
- [cv2.matchTemplate](https://docs.opencv.org/master/df/dfb/group__imgproc__object.html#ga586ebfb0a7fb604b35a23d85391329be)
- [cv2.minMaxLoc](https://docs.opencv.org/master/d2/de8/group__core__array.html#gab473bf2eb6d14ff97e89b355dac20707)
- [cv2.rectangle](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga07d2f74cadcf8e305e810ce8eed13bc9)
- [cv2.imshow](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563)
- [cv2.waitKey](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7)

## 😎 Fun Fact
Template matching is one of the oldest computer vision techniques, dating back to the 1960s! Despite its simplicity, it's still widely used today in applications ranging from optical character recognition (OCR) to medical image analysis. The technique is even used in some photo editing software to help with the "content-aware fill" feature that can magically remove unwanted objects from photos. While modern deep learning approaches have surpassed template matching in many applications, its computational efficiency and lack of training requirements make it a valuable tool in the computer vision toolkit, especially for real-time applications with known templates.