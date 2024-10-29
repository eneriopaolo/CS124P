import cv2 as cv

def take_picture(username: str):  
    cam = cv.VideoCapture(0) 
    result, image = cam.read() 
    print("name: " + username)
    if result: 
        cv.imshow("Camera", image)
        cv.waitKey(0) 
        cv.destroyWindow("Camera") 
        cv.imwrite(f"{username}.png", image)
    else: 
        print("Error: Image Detected.")
