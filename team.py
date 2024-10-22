def display_menu():
    print("Please choose an option from the list below:")
    print("1. Play a Game")
    print("2. Watch a Movie")
    print("3. Read a Book")
    print("4. Go for a Walk")
    print("5. Listen to Music")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("You chose to play a game!")
        elif choice == '2':
            print("You chose to watch a movie!")
        elif choice == '3':
            print("You chose to read a book!")
        elif choice == '4':
            print("You chose to go for a walk!")
        elif choice == '5':
            print("You chose to listen to music!")
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    