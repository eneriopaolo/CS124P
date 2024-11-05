import ImageHandler as IH
import FileHandler as FH
import FRecog as FR
import os
from notepad import noteApp

term_size = 30

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
    os.system('cls')
    print('=' * 30)
    print(f"Successly registered user {username}.")


def main() -> None:
    while True:
        print('=' * term_size)
        print("Note Taking App")
        print("[1] Register")
        print("[2] Login")
        print("[3] Exit Program")
        print('-' * term_size)
        user_input = input("Enter number: ")

        if user_input == "1":
            os.system('cls')
            print('=' * term_size)
            register()
        elif user_input == "2":
            IH.take_and_save_pictureV2()
            if not FR.check_for_multiple_faces("AnonUser.png"):
                print("Login failed. Ensure only one face is present and try again.")
                continue  # Retry registration

            username = FR.GetUser()
            #username = input("Enter username: ")
            if (username == "None"):
                print ("User not Found.")
                continue
            os.system('cls')
            print('=' * term_size)
            print (f"Welcome {username.title()}!")
            noteApp(username)   

        elif user_input == "3":
            break
        else:
            print("Invalid Input.")


if __name__ == "__main__":
    main()