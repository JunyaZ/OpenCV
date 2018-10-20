'''
Find lines in an image by looking for specific colors
'''
import cv2
import numpy as np

image_path = "Images//emptyroad.jpg"  #Images dir must be in current working dir

def find_color(img, ref_color, thr):
    '''Returns an image with only colors close to ref_color'''
    #Make a blank img so original isn't changed
    #--Use np.zeros so blank img is black
    #print(img.shape)
    copy = np.zeros(img.shape, dtype = "uint8")
    #Get the height and width of the image
    height, width = img.shape[:2]
    for row in range(height):  #For each row in the image
        for col in range(width):#  For each column in the image
            p = img[row,col]    #    Get the pixel at row, column
    #    Use color_dist() to get the distance between the pixel and ref_color
            d = color_dist(p, ref_color)
            #    If the distance is <= thr, copy to pixel into the blank image
            if d < thr:
                copy[row,col] = p
                
    #    Otherwise, leave that pixel black in the blank image
    #Return the blank image (which may no longer be blank)
    return copy

def color_dist(c1, c2):
    '''c1 and c2 are colors in BGR format'''
    #Calculate and return the Euclidean distance between c1 and c2
    d = np.sqrt(sum((c2 - c1) ** 2))
    return d
    

def add_images(img1, img2):
    '''Returns the addition of two images; avoids pixel overflow'''
    #h1, w1 = img1.shape[:2]
    #h2, w2 = img2.shape[:2]
    #vis[:h1, :w1,:3] = img1
    #vis[:h2, w1:w1+w2,:3] = img2
    img=  img1 + img2
    return img 

    #Do not change img1 or img2
    #Perhaps you would rather take a list of images as an argument
    #so you can add any number of them

def main():
    ref_white = (255, 255, 255)
    ref_yellow = (126, 217, 244)
    white_thr = 100  #Experiment to find the best value
    yellow_thr = 50 #Experiment to find the best value
    #Read the image
    img = cv2.imread(image_path)
    #Display the image
    cv2.imshow("Roda", img)
    #Use find_color() to create an image showing only the white lines
    white_lines = find_color(img, ref_white, white_thr)
    #Display the white lines image in its own window
    cv2.imshow("White lines", white_lines)
    #Use find_color() to create an image showing only the yellow lines
    yellow_lines = find_color(img, ref_yellow, yellow_thr)
    #Display the yellow lines image in its own window
    cv2.imshow("Yellow lines", yellow_lines)
    #Use add_images() to create an image with both white and yellow lines
    together = add_images(yellow_lines, white_lines)
    #Display the image with both white and yellow lines
    cv2.imshow("Together", together)
    while True:
        key = cv2.waitKey(1)  #wait for 1 ms
        if key == 27:         #ASCII code for ESC
            break
    cv2.destroyAllWindows()

main()

