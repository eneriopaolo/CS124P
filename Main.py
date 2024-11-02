import ImageHandler as IH
import FileHandler as FH
import FRecog as FR
import os
from notepad import noteApp

def register():
    FH.check_or_create_dir()
    while True:
        username = input("Enter username: ").lower()
        
        if not FH.check_for_duplicates(username):
            # Capture the picture
            IH.take_and_save_picture(username)
            image_path = f"Images/{username}.png"
            
            # Check for multiple or no faces
            if not FR.check_for_multiple_faces(image_path):
                # Delete the saved image if invalid
                if os.path.exists(image_path):
                    os.remove(image_path)
                print("Registration failed. Ensure only one face is present and try again.")
                continue  # Retry registration

            break  # Exit loop if face detection is valid
        else:
            print("Username is already taken.")


def main() -> None:
    while True:
        print("Note Taking App")
        print("1) Register")
        print("2) Login")
        print("3) Exit Program")
        user_input = input("Enter number: ")

        if user_input == "1":
            register()
        elif user_input == "2":
            IH.take_and_save_pictureV2()
            username = FR.GetUser()
            #username = input("Enter username: ")
            if (username == "None"):
                print ("User not Found.")
                continue
            print (f"Welcome {username}")
            noteApp(username)   

        elif user_input == "3":
            break
        else:
            print("Invalid Input.")


if __name__ == "__main__":
    main()