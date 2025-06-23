import cv2

#open cv have BGR color schem instead of RGB i.e. Blue Green Red not Red Green Blue

# -1, cv2.IMREAD_COLOR READ the image in color
#  0, cv2.IMREAD_GRAYSCALE READ the image in grayscale
#  1, cv2.IMREAD_UNCHANGED READ the image in unchanged mode include alpha channel if present

# img = cv2.imread('assets/AS.jpg', 1) # Read the image in unchanged mode
# img = cv2.imread('assets/AS.jpg', -1) # Read the image in color mod

img = cv2.imread('assets/AS.jpg', 0) # Read / load  the image in img variable

# Resize the image to a specific size
# img = cv2.resize(img, (500, 500)) # Resize the image to 500x500 pixels
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # Resize the image to half of its original size 

#Rotate the image 
img = cv2.rotate(img, cv2.ROTATE_180) # Rotate the image 90 degrees clockwise
# likewise you can use cv2.ROTATE_90_COUNTERCLOCKWISE, cv2.ROTATE_180 and so on

# Save the image to a file

cv2.imwrite('assets/AS_resized.jpg', img) # Save the resized image to a file

cv2.imshow('Logo', img) # Show the image in a window named 'Logo'
cv2.waitKey(0) # wait for a key press infinietly bcz of 0, if ther any other number such as 10 its wait 10 second and move on next line
cv2.destroyAllWindows() # Destroy all the windows created by OpenCV