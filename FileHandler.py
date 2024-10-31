import os

def check_or_create_dir():
    if os.path.exists("Images") == False:
        try:
            os.makedirs("Images")
        except PermissionError:
            print("Permission denied: Unable to create directory.")
        except Exception as e:
            print(f"An error occurred: {e}")