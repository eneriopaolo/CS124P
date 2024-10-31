import ImageHandler as IH

def register():
    username = input("Enter username: ").lower()
    IH.take_and_save_picture(username)

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
            print("Login")
        elif user_input == "3":
            break
        else:
            print("Invalid Input.")


if __name__ == "__main__":
    main()