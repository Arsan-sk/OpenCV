# images we seeare nothing but a collection of pixels which is use numpy array to form in a way that firstly we have an arry that have arrays for multiple rows and columns ehre each array is a pixel and each pixel have 3 values for BGR color scheme from 0 to 255 where 0 is black and 255 is white and in between we have different shades of colors for eg we 255 0 0 is blue in opencv and 0 255 0 is green and 0 0 255 is red and so on sowe can actually see the perticular array of pixel of our image make changes to a color and so many things we can do with images using opencv
import cv2
import random

# print(img[0]) # Print the first row of pixels in the image
# print(img[0][0]) # Print the first pixel in the first row
# print(img[257][45:50])  # Print the pixel values from row 257, columns 45 to 50

img = cv2.imread('assets/AS.jpg', -1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# img.shape[1] # Get the number of columns in the image

# changing color of each pixel in the first 100 rows of the image to a random color

# for i in range(100): # Iterate through the first 100 rows of the image
#     for j in range(img.shape[1]): # iterate through all columns in the current row
#         img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]  # Set each pixel to a random color as img[][] = [B, G, R] where B is blue, G is green and R is red


# copy and paste the certain part of the image to another part

tag = img[100:500, 200:400] # # Copy a portion of the image from row 200 to 400 and columns 550 to 650
img[100:500, 300:500] = tag  # Paste the copied portion to a new location in the image from row 50 to 700 and columns 150 to 350

# cv2.imwrite('assets/AS_Cp_pst.jpg', img)
cv2.imshow('Logo', img)  
cv2.waitKey(0)
cv2.destroyAllWindows()  
# it actually changing the color of each pixelin the first 100 rows of the image to a random color, which is why you see a colorful pattern in the output image.