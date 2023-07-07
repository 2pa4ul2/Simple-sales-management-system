from MenuFunction import *
def Menu_selection():
    while True:
        print("+=================================================+")
        print("|            1. Add Product                       |")
        print("|            2. Display Products                  |")
        print("|            3. Update Product                    |")
        print("|            4. Analytics                         |")
        print("|            5. Change Key                         |")
        print("|            6. Quit                              |")
        print("+=================================================+")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            analytics()
        #elif choice == "5":
            #change_key()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
            Menu_selection()