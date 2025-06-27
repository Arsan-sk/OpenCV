# 📂 Face and Eye Detection

## 🧠 Overview
Face and eye detection is a powerful computer vision technique that identifies human faces and eyes in images or video streams. This module demonstrates how to use pre-trained Haar Cascade classifiers in OpenCV to detect faces and eyes in real-time from a webcam feed. These techniques form the foundation for more advanced applications like facial recognition, emotion detection, and augmented reality filters.

## 📘 Learnings & Concepts Covered
- Understanding and using pre-trained Haar Cascade classifiers
- Real-time face detection in video streams
- Nested object detection (eyes within faces)
- Region of Interest (ROI) extraction and processing
- Drawing bounding boxes around detected features
- Working with grayscale conversion for improved detection

### 🎯 File: `Face_Eye_Detection.py`
#### 📌 Concept/Goal
This script demonstrates how to detect faces and eyes in real-time using a webcam feed. It uses pre-trained Haar Cascade classifiers provided by OpenCV to identify facial features. The script first detects faces in each frame, then searches for eyes only within the detected face regions (ROI - Region of Interest) to improve accuracy and performance. Detected features are highlighted with colored rectangles.

#### ⚙️ Functions & Methods Used
- `cv2.CascadeClassifier()`
  ```python
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
  ```
  Loads pre-trained Haar Cascade classifier XML files for face and eye detection. These classifiers contain features trained on thousands of positive and negative images to recognize specific patterns that constitute faces and eyes.

- `cv2.VideoCapture()`
  ```python
  cap = cv2.VideoCapture(0)
  ```
  Creates a video capture object to read frames from the default camera (index 0).

- `cv2.cvtColor()`
  ```python
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  ```
  Converts the color space of an image from BGR (OpenCV's default) to grayscale, which simplifies processing and improves detection performance.

- `cascade.detectMultiScale()`
  ```python
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  ```
  Detects objects of different sizes in the input image using the loaded cascade classifier. Parameters include:
  - `gray`: The input grayscale image
  - `1.3`: Scale factor that specifies how much the image size is reduced at each image scale (smaller values = higher accuracy but slower performance)
  - `5`: MinNeighbors parameter specifying how many neighbors each candidate rectangle should have to be retained (higher values = fewer detections but higher quality)

- `cv2.rectangle()`
  ```python
  cv2.rectangle(frame, (x,y), (x + w, y + h), (0,255,0), 5)
  ```
  Draws a rectangle on the image. Parameters include:
  - `frame`: The image to draw on
  - `(x,y)`: Top-left corner coordinates
  - `(x + w, y + h)`: Bottom-right corner coordinates
  - `(0,255,0)`: BGR color (green in this case)
  - `5`: Line thickness in pixels

- Array slicing for ROI extraction
  ```python
  roi_gray = gray[y:y+h, x:x+w]
  roi_frame = frame[y:y+h, x:x+w]
  ```
  Extracts a Region of Interest (ROI) from the image using NumPy array slicing. This creates sub-images containing only the detected face regions, which are then used for eye detection.

#### ▶️ How it Works (Step-by-step)
1. Load the pre-trained Haar Cascade classifiers for face and eye detection
2. Initialize the webcam capture using `cv2.VideoCapture(0)`
3. Enter a continuous loop to process frames:
   - Read a frame from the webcam using `cap.read()`
   - Convert the frame to grayscale using `cv2.cvtColor()`
   - Detect faces in the grayscale image using `face_cascade.detectMultiScale()`
4. For each detected face:
   - Draw a green rectangle around the face using `cv2.rectangle()`
   - Extract the face region (ROI) from both the grayscale and color images
   - Detect eyes within the face ROI using `eye_cascade.detectMultiScale()`
5. For each detected eye within a face:
   - Draw a red rectangle around the eye using `cv2.rectangle()`
6. Display the processed frame with `cv2.imshow()`
7. Check for the 'q' key press to exit the loop
8. Release resources with `cap.release()` and `cv2.destroyAllWindows()`

#### 📄 External References
- [OpenCV Haar Cascades](https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html)
- [Face Detection using Haar Cascades](https://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html)
- [Cascade Classifier Training](https://docs.opencv.org/master/dc/d88/tutorial_traincascade.html)
- [Pre-trained Haar Cascade models](https://github.com/opencv/opencv/tree/master/data/haarcascades)

## ▶️ How to Run
```bash
# Navigate to the Face_Eye_Detection directory
cd "path/to/Open CV/Advanced/Face_Eye_Detection"

# Run the face and eye detection script
python Face_Eye_Detection.py
```

## 📄 Function Documentation
- [cv2.CascadeClassifier](https://docs.opencv.org/master/d1/de5/classcv_1_1CascadeClassifier.html)
- [cv2.VideoCapture](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html)
- [cv2.cvtColor](https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab)
- [detectMultiScale](https://docs.opencv.org/master/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498)
- [cv2.rectangle](https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga07d2f74cadcf8e305e810ce8eed13bc9)
- [cv2.imshow](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563)
- [cv2.waitKey](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7)

## 😎 Fun Fact
The Haar Cascade classifiers used in this script were originally proposed by Paul Viola and Michael Jones in their groundbreaking 2001 paper, which revolutionized face detection. Before their work, face detection was slow and unreliable. Their algorithm made real-time face detection possible on consumer hardware for the first time! This technology is what powers the face detection feature in most digital cameras today, allowing them to automatically focus on faces when taking photos. The same technique is also used in popular social media filters that add virtual elements to your face in real-time.