from Computation import *
import os

def cls():
    print("\n"*50)
def load_key():
    if os.path.exists("textkey.txt"):
        with open("textkey.txt", "r") as file:
            try:
                key = int(file.read())
            except ValueError:
                print("Invalid key format in the key file.")
                key = int(input("Enter the encryption/decryption key: "))
                with open("textkey.txt", "w") as file:
                    file.write(str(key))
    else:
        key = int(input("Enter the encryption/decryption key: "))
        with open("textkey.txt", "w") as file:
            file.write(str(key))
    return key

def change_key():
    old_key = load_key()
    print("Old Key:", old_key)
    new_key = int(input("Enter the new encryption/decryption key: "))

    products = retrieve_products(old_key)
    save_products(products, new_key)

    with open("textkey.txt", "w") as file:
        file.write(str(new_key))

    print("Key changed successfully!")
# Caesar cipher encryption
def encrypt(text, key):
    encrypted_text = bytearray()
    for char in text:
        encrypted_char = (char + key) % 256  # Modulus 256 to encrypt with ascii value
        encrypted_text.append(encrypted_char)
    return encrypted_text

# Caesar cipher decryption
def decrypt(encrypted_text, key):
    decrypted_text = bytearray()
    for char in encrypted_text:
        decrypted_char = (char - key) % 256
        decrypted_text.append(decrypted_char)
    return decrypted_text

def save_products(products, key):
    with open("products.txt", "wb") as file:
        for product in products:
            encrypted_product = encrypt(",".join(map(str, product)).encode(), key)
            file.write(encrypted_product + b"\n")

def retrieve_products(key):
    if not os.path.exists("products.txt"):
        return []

    with open("products.txt", "rb") as file:
        lines = file.readlines()

    products = []
    for line in lines:
        decrypted_product = decrypt(line.strip(), key).decode().split(",")
        products.append(decrypted_product)

    return products

def add_product():
    cls()
    print(" ▄▀▄ █▀▄ █▀▄   █▀▄ █▀▄ ▄▀▄ █▀▄ █ █ ▄▀▀ ▀█▀")
    print(" █▀█ █▄▀ █▄▀   █▀  █▀▄ ▀▄▀ █▄▀ ▀▄█ ▀▄▄  █ ")
    print("███████████████████████████████████████████████████")
    product_name = input("|\tEnter product name: ")
    brand = input("|\tEnter brand: ")
    product_cost = float(input("|\tEnter product cost: "))
    selling_price = float(input("|\tEnter selling price: "))

    if selling_price < product_cost:
        print("Selling price cannot be lower than the cost.")
        return

    quantity = int(input("|\tEnter quantity: "))
    sold = int(input("|\tEnter sold: "))
    print("███████████████████████████████████████████████████")
    key = load_key()
    products = retrieve_products(key)

    for product_data in products:
        if product_data[0] == product_name:
            print("Product already exists.")
            return

    if sold > quantity:
        print("Sold quantity cannot exceed the available quantity.")
        return

    product_info = [product_name, brand, product_cost, selling_price, quantity, sold]
    products.append(product_info)

    save_products(products, key)

    print("Product added successfully!")
    cls()

def display_products():
    cls()
    key = load_key()
    products = retrieve_products(key)
    choice = 0
    print("███████████████████████████████████████████████████")
    print(" \t\t\t█▀▄ █ ▄▀▀ █▀▄ █   ▄▀▄ ▀▄▀")
    print(" \t\t\t█▄▀ █ ▄██ █▀  █▄▄ █▀█  █ ")
    if not products:
        print("No products found.")
    else:
            print("███████████████████████████████████████████████████")
            print("█            1. Ascending                         █")
            print("█            2. Descending                        █")
            print("█            3. Quit                              █")
            print("███████████████████████████████████████████████████")
            choice = input("Enter your choice (1-6): ")
            if choice == '1':
                sorted_products = sorted(products, key=lambda x: x[0].lower())  # Sort by product name (x[0])
                print("============================================================================")
                print("{:<20} {:<15} {:<10} {:<10} {:<10} {:<10}".format("Product Name", "Brand", "Cost", "Price",
                                                                         "Quantity", "Sold"))
                print("----------------------------------------------------------------------------")
                for product_data in sorted_products:
                    print("{:<20} {:<15} {:<10.2f} {:<10.2f} {:<10} {:<10}".format(product_data[0], product_data[1],
                                                                                   float(product_data[2]),
                                                                                   float(product_data[3]),
                                                                                   product_data[4], product_data[5]))
                print("=============================================================================")
            elif choice == '2':
                sorted_products = sorted(products, key=lambda x: x[0].lower(),
                                         reverse=True)  # Sort by product name (x[0])
                print("============================================================================")
                print("{:<20} {:<15} {:<10} {:<10} {:<10} {:<10}".format("Product Name", "Brand", "Cost", "Price",
                                                                         "Quantity", "Sold"))
                print("----------------------------------------------------------------------------")
                for product_data in sorted_products:
                    print("{:<20} {:<15} {:<10.2f} {:<10.2f} {:<10} {:<10}".format(product_data[0], product_data[1],
                                                                                   float(product_data[2]),
                                                                                   float(product_data[3]),
                                                                                   product_data[4], product_data[5]))
                print("=============================================================================")
            elif choice == '3':
                exit()
            else:
                return


def update_product():
    key = load_key()
    display_products()
    print("██████████████████████████████████████████████████████")
    print(" █ █ █▀▄ █▀▄ ▄▀▄ ▀█▀ ██▀   █▀▄ █▀▄ ▄▀▄ █▀▄ █ █ ▄▀▀ ▀█▀")
    print(" ▀▄█ █▀  █▄▀ █▀█  █  █▄▄   █▀  █▀▄ ▀▄▀ █▄▀ ▀▄█ ▀▄▄  █ ")
    print("██████████████████████████████████████████████████████")
    product_name = input("Enter the product name to update: ")

    products = retrieve_products(key)

    found = False

    for product_data in products:
        if product_data[0] == product_name:
            found = True
            quantity = int(product_data[4])
            new_quantity = int(input("Enter the new quantity: "))
            new_sold = int(input("Enter the new sold quantity: "))
            new_cost = float(input("Enter the new cost: "))
            new_price = float(input("Enter the new selling price: "))

            if new_sold > new_quantity or new_sold > quantity:
                print("Sold quantity cannot exceed the available quantity.")
                return

            if new_price < new_cost:
                print("Selling price cannot be lower than the cost.")
                return
            product_data[2] = str(new_cost)
            product_data[3] = str(new_price)
            product_data[4] = str(new_quantity)
            product_data[5] = str(new_sold)


            save_products(products, key)

            print("Product updated successfully!")
            cls()
            break

    if not found:
        print("Product not found.")
        new_product_name = input("Enter the name of the product to update: ")
        if new_product_name != "":
            update_product(new_product_name)
    cls()

def analytics():
    cls()
    key = load_key()
    products = retrieve_products(key)

    if not products:
        print("No products found.")
        return

    total_revenue = compute_total_revenue(products)
    total_profit = compute_profit(products)
    best_selling_product = compute_best_selling_product(products)
    total_sold = compute_total_sold(products)
    profit_percentage = compute_profit_percentage(products)
    average_price = compute_average_price(products)
    total_expenses = compute_total_expenses(products)
    average_margin = compute_average_profit_margin(products)
    print("███████████████████████████████████████████████████")
    print(" ▄▀▄ █▄ █ ▄▀▄ █   ▀▄▀ ▀█▀ █ ▄▀▀ ▄▀▀")
    print(" █▀█ █ ▀█ █▀█ █▄▄  █   █  █ ▀▄▄ ▄██")
    print("███████████████████████████████████████████████████")
    print("Total Revenue:", total_revenue)
    print("Total expenses:", total_expenses)
    print("Total Profit:", total_profit)
    print("Total sold:", total_sold)
    print("Average Price: {:.2f}%".format(average_price))
    print(f"Profit percentage:", round(profit_percentage, 2), "%")
    print("Average Profit Margin: {:.2f}%".format(average_margin))
    print("███████████████████████████████████████████████████")
    if best_selling_product:
        print("Best Selling Product:", best_selling_product[0])
        print("███████████████████████████████████████████████████")
    else:
        print("Best Selling Product: None")
        print("███████████████████████████████████████████████████")
    cls()


def Menu_selection():
    while True:
        print("███████╗███████╗██╗     ██╗     ██╗███████╗██╗   ██╗    ")
        print("██╔════╝██╔════╝██║     ██║     ██║██╔════╝╚██╗ ██╔╝    ")
        print("███████╗█████╗  ██║     ██║     ██║█████╗   ╚████╔╝     ")
        print("╚════██║██╔══╝  ██║     ██║     ██║██╔══╝    ╚██╔╝      ")
        print("███████║███████╗███████╗███████╗██║██║        ██║       ")
        print("╚══════╝╚══════╝╚══════╝╚══════╝╚═╝╚═╝        ╚═╝       ")
        print("███████████████████████████████████████████████████")
        print("█            1. Add Product                       █")
        print("█            2. Display Products                  █")
        print("█            3. Update Product                    █")
        print("█            4. Analytics                         █")
        print("█            5. Change Key                        █")
        print("█            6. Quit                              █")
        print("███████████████████████████████████████████████████")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_product()

        elif choice == "2":
            display_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            analytics()
        elif choice == "5":
            change_key()
        elif choice == "6":
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Menu_selection()
