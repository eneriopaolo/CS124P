import cv2 as cv

#Takes and save pictures to the Images Directory.
#Images directory should first be checked if it exists.
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
            cv.imwrite(('Images/' + file_name), image)
            break

def take_and_save_pictureV2():
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
            file_name = f"AnonUser.png"
            cv.imwrite((file_name), image)
            break


