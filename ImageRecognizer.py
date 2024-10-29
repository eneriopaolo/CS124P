import cv2 as cv

def take_picture():  
    cam = cv.VideoCapture(0) 
    result, image = cam.read() 

    if result: 
        cv.imshow("GeeksForGeeks", image) 
        cv.waitKey(0) 
        cv.destroyWindow("GeeksForGeeks") 
    else: 
        print("No image detected. Please! try again") 
