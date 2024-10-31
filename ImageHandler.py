import cv2 as cv
import FileHandler as FH

def take_and_save_picture(username: str):
    while True: 
        cam = cv.VideoCapture(0) 
        result, image = cam.read() 

        if result: 
            cv.imshow("Camera", image)
            cv.waitKey(0)
            cv.destroyWindow("Camera")         
        else: 
            print("Error: Image Detected.")
        
        user_input = input("Take another picture? (Yes/No): ").lower()

        if user_input == "no":
            file_name = f"{username}.png"
            FH.check_or_create_dir()
            cv.imwrite(('Images/' + file_name), image)
            break

