import cv2 as cv
import os

#Takes and save pictures to the Images Directory.
#Images directory should first be checked if it exists.
def take_and_save_picture(username: str):
    confirm = True
    while confirm: 
        cam = cv.VideoCapture(0) 
        result, image = cam.read() 

        if result: 
            cv.imshow("Camera", image)
            cv.waitKey(0)
            cv.destroyWindow("Camera")         
        else: 
            print("Error: Image Detected.")
        
        os.system('cls')

        while True:
            print('=' * 30)
            user_input = input("Take another picture? (Yes/No): ").lower()
            if user_input == "no":
                file_name = f"{username}.png"
                print("Please wait for the system to save the image...")
                cv.imwrite(('Images/' + file_name), image)
                confirm = False
                break
            elif user_input == "yes":
                break
            elif user_input == "":
                print("Ignore this message, this is an enter bug when using console when exiting the image taken.")
            else:
                print("Invalid Input.")

def take_and_save_pictureV2():
    confirm = True
    while confirm: 
        cam = cv.VideoCapture(0) 
        result, image = cam.read() 

        if result: 
            cv.imshow("Camera", image)
            cv.waitKey(0)
            cv.destroyWindow("Camera")         
        else: 
            print("Error: Image Detected.")
        
        os.system('cls')
        while True:
            print('=' * 30)
            user_input = input("Take another picture? (Yes/No): ").lower()
            if user_input == "no":
                file_name = f"AnonUser.png"
                print("Please wait for the system to load...")
                cv.imwrite((file_name), image)
                confirm = False
                break
            elif user_input == "yes":
                break
            elif user_input == "":
                print("Ignore this message, this is an enter bug when using console when exiting the image taken.")
            else:
                print("Invalid Input.")



