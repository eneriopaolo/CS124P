import cv2 as cv
import FileHandler as FH

def take_and_save_picture(username: str):  
    cam = cv.VideoCapture(0) 
    result, image = cam.read() 
    file_name = f"{username}.png"
    if result: 
        cv.imshow("Camera", image)
        cv.waitKey(0)
        cv.destroyWindow("Camera")
        FH.check_or_create_dir()
        cv.imwrite(('Images/' + file_name), image)
    else: 
        print("Error: Image Detected.")
