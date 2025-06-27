# 📂 Basics
Welcome to the Basics folder of OpenCV-Projects — your official baby steps into the world of computer vision 👶🔍

Here we begin from understanding images as pixel matrices, explore image reading and manipulation, and even draw on real-time camera feeds like a pro!


## 📘 Learnings & Concepts Covered

-Reading and writing images in OpenCV
-BGR vs RGB vs GRAYSCALE
-Resizing and rotating images
-Pixel access and manipulation
-Drawing shapes and text on images
-Camera feed frame processing
-Coordinate system in OpenCV

## 🗂️ Files & Explanations
### opencv_basics1.py

 #### 📚 Concepts: 
-Reading image in different modes:
--cv2.IMREAD_COLOR (-1)
--cv2.IMREAD_GRAYSCALE (0)
--cv2.IMREAD_UNCHANGED (1)

-Resizing:
```sh
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
```

-Rotating:
```sh
cv2.rotate(img, cv2.ROTATE_180)
```

-Displaying and saving:
```sh
cv2.imshow("Window", img)
cv2.imwrite("output.jpg", img)
```

*** 💡 Note: OpenCV uses BGR, not RGB — so img[0][0] = [255, 0, 0] is blue, not red 😄 ***


### opencv_basics2.py

#### 📚 Concepts:
-Images = NumPy arrays
-Pixel access:
```sh
print(img[50][100])  # BGR value of pixel at row 50, column 100
```
-Modifying pixels:
```sh
img[i][j] = [randB, randG, randR]
```
-Copy-pasting a region (ROI):
```sh
tag = img[100:500, 200:400]
img[100:500, 300:500] = tag
```

*** 🧠 This is how meme engineers copy that sus face and paste it on everyone 😜 ***


### drawing_in_opencv.py

#### 📚 Concepts:
-Drawing:
--cv2.line()
--cv2.rectangle()
--cv2.circle()

-Writing text:
```sh
cv2.putText(img, 'Text Here', (x, y), font, scale, color, thickness, cv2.LINE_AA)
```

-Real-time drawing over camera feed
-Coordinate system: Top-left is (0,0), X goes →, Y goes ↓

*** 🧙‍♂️ Feel like an artist? Here’s where code meets canvas 🎨 ***


## ▶️ Run This Folder
```sh
python basics/opencv_basics1.py
```
Ensure the path to the image file (like 'assets/AS.jpg') exists. Otherwise, update it accordingly.

## 📄 Function Documentation

- [`cv2.imread()`](https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html#ga14b471d44c629f12bce908891f1006f5) – Read an image from file.
- [`cv2.imshow()`](https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga7cbe95544b3c9c6f72f6cce72d08b55c) – Display an image in a window.
- [`cv2.putText()`](https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html) – Draw text on an image.

## 🧠 Tip
*** Want to see magic? Try changing the entire image’s top half to green using pixel slicing 😈 ***



 

