from MenuFunction import *
def Menu():
    while True:
        print("===================================================")
        print("|        1. Add a product                          |")
        print("|        2. Display products                       |")
        print("|        3. Update a product                       |")
        print("|        4. Analytics                              |")
        print("|        5. Quit                                   |")
        print("===================================================")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            analytics()
        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
            Menu()