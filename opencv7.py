# Here we have done a Template Matching i.e. Ibject Finding or can say matching a template image with in a source image simply by comarung the pixel values of the template image with the source image and finding the best match using correlation method.
# for performing this we have many algorithms which we used 
# note try to match the pixel values of base and template image like the piels which tamplate image have the area in base image have that tamplate also be around that size so its easie instead like base image of 500 by 500 px and the tamplate is 1000ox by 1000px
import cv2
import numpy as np

img = cv2.imread("assets/socerPlay.jpg", 0) # load in gray scale asits easyfor algorithms to work with
template = cv2.imread("assets/socerBall.png", 0)
# template = cv2.imread("assets/shose.png", 0)

h, w = template.shape # .shape returns the dimensions of the image like (height, width, channels) but for grayscale we take only height and width

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, 
           cv2.TM_CCORR, cv2.TM_CCORR_NORMED, 
           cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]  # these are 6 methods used for template matching we try each one by one its best to try all and then choose one gives best result\

for method in methods:
    img2 = img.copy() # each time we run loop get a copy for drawing a rectangle wehre we get template if not do that so till the end of the loop get multiple rectangles on main images so but due to this each time new copy cretae so previous rectangle will not be there

    result = cv2.matchTemplate(img2, template, method) # passthe base image template and method and gives array of matcheing image as we disscussed in the below explanation and so other
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) # its gives location of inimum and maximum value in image array o we use it to make rectangle
    # print(min_loc,max_loc)

    # some time min_loc is best and some time max_loc based on method so we used accordingly
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: ## best for minimum location
        location = min_loc # we location co_ordinate for top right corner of template image
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h) # we simply add the both x and y direction of templateheight so get bottom co ordinates it simple
    cv2.rectangle(img2, location, bottom_right, 255, 5) # pass image , start_codnt, end_codnt, color black, thicknees
    cv2.imshow("Matching template", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# RESULT --> When i run the code get the only one method gives correct matching and its different for both images so ased on that we can choose the method and apply in projects
# few method may be not recoginsing due to image size issue or may be as my template and base image have different extension or may be other reason

# explanation of matchTemplate() function

    # (W-w+1, H-h+1) is a dimention of return array(img) size if W,H=4 & w,h=2 then we get (3,3) array as it return array with 0 and 1 where 1 shows its match here i and 0 says not match and based on that by applying soe calculation we get location of the template image in base image
    # [[125,222,255,255],     [[255,255], 4by and 2by hence we get 3by3                                 [[0,0,1],    and based onthis do some calculation and find coordinates on nbase image 
    #  [125,255,255,255],      [255,255]]                                                                [0,1,0],    we take that and draw a rectangle there.
    #  [255,255,255,980],     here this is a template and base image its check and return 1 if match     [1,0,0],
    #  [255,255,109,809]]     and 0 if not match and give this


# min and max loc values
    # (334, 459) (481, 320)
    # (277, 391) (254, 493)
    # (199, 336) (390, 376)
    # (277, 389) (251, 494)
    # (671, 509) (276, 388)
    # (409, 399) (0, 0)