import ImageHandler as IH

def main() -> None:
    while True:
        print("Note Taking App")
        print("1) Register")
        print("2) Login")
        print("3) Exit Program")
        user_input = input("Enter number: ")

        if user_input == "1":
            username = input("Enter username: ")
            IH.take_picture(username)
        elif user_input == "2":
            print("Login")   
        elif user_input == "3":
            break
        else:
            print("Invalid Input.")


if __name__ == "__main__":
    main()