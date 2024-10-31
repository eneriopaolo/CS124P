import os

#Creates 'Images' folder if it does not exist
def check_or_create_dir():
    dir = "Images"
    if os.path.exists(dir) == False:
        try:
            os.makedirs(dir)
        except PermissionError:
            print("Permission denied: Unable to create directory.")
        except Exception as e:
            print(f"An error occurred: {e}")