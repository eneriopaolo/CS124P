import os
img_dir = "Images"


#Creates 'Images' folder if it does not exist
def check_or_create_dir():
    if os.path.exists(img_dir) == False:
        try:
            os.makedirs(img_dir)
        except PermissionError:
            print("Permission denied: Unable to create directory.")
        except Exception as e:
            print(f"An error occurred: {e}")


#Checks if a picture with a specific file name already exists.
#This is used for disallowing same username in Registration.
def check_for_duplicates(username: str) -> bool:
    return (os.path.exists(f"{img_dir}/{username}.png"))