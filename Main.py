import ImageHandler as IH
import FileHandler as FH
from notepad import noteApp

def register():
    while True:
        username = input("Enter username: ").lower()
        if FH.check_for_duplicates(username) == False:
            IH.take_and_save_picture(username)
            break
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
            username = input("Enter username: ")
            noteApp(username) 
        elif user_input == "3":
            break
        else:
            print("Invalid Input.")


if __name__ == "__main__":
    main()