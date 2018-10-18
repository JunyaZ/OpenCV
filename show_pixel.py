'''
Prints pixel value when clicked on by mouse
'''
import cv2
import numpy as np

row, col = None, None

image_path = "hot_air.jpg"

def read_img(fname):
    #img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    img = cv2.imread(fname)
    return img

def mouse_location(event, x, y, flags, params):
    #Register row, col location of mouse click
    global row, col
    if event == cv2.EVENT_LBUTTONDOWN:
        row = y
        col = x

def main():
    global row, col
    img = cv2.imread(image_path)
    if img is None:
        print("Mayday - image not found!")
        return
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouse_location)
    while True:
        if row is not None and col is not None:
            print(img[row, col])
            row, col = None, None
        key = cv2.waitKey(1)  #wait for 1 ms
        if key == 27:         #ASCII code for ESC
            break
    cv2.destroyAllWindows()

main()

