from Computation import *
import os

def add_product():
    product_name = input("Enter product name: ")
    brand = input("Enter brand: ")
    product_cost = float(input("Enter product cost: "))
    selling_price = float(input("Enter selling price: "))

    if selling_price < product_cost:
        print("Selling price cannot be lower than the cost.")
        return

    quantity = int(input("Enter quantity: "))
    sold = int(input("Enter sold: "))

    if not os.path.exists("products.txt"):
        with open("products.txt", "w"):
            pass

    with open("products.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        product_data = line.strip().split(",")
        if product_data[0] == product_name:
            print("Product already exists.")
            return

    if sold > quantity:
        print("Sold quantity cannot exceed the available quantity.")
        return

    product_info = f"{product_name},{brand},{product_cost},{selling_price},{quantity},{sold}\n"

    with open("products.txt", "a") as file:
        file.write(product_info)

    print("Product added successfully!")


def display_products():
    with open("products.txt", "r") as file:
        products = file.readlines()
        print("===================================================")
        print("DISPLAY PRODUCT")
        if not products:
            print("No products found.")
        else:
            print("============================================================================")
            print("{:<20} {:<15} {:<10} {:<10} {:<10} {:<10}".format("Product Name", "Brand", "Cost", "Price", "Quantity", "Sold"))
            print("----------------------------------------------------------------------------")
            for product in products:
                product_data = product.strip().split(",")
                print("{:<20} {:<15} {:<10.2f} {:<10.2f} {:<10} {:<10}".format(product_data[0], product_data[1], float(product_data[2]), float(product_data[3]), product_data[4], product_data[5]))
            print("=============================================================================")


def update_product():
    display_products()
    print("===================================================")
    product_name = input("Enter the product name to update: ")

    with open("products.txt", "r") as file:
        lines = file.readlines()

    found = False

    for line in lines:
        product_data = line.strip().split(",")
        if product_data[0] == product_name:
            found = True
            quantity = int(product_data[4])
            new_quantity = int(input("Enter the new quantity: "))
            new_sold = int(input("Enter the new sold quantity: "))

            if new_sold > new_quantity:
                print("Sold quantity cannot exceed the available quantity.")
                return
            elif new_sold > quantity:
                print("Sold quantity cannot exceed the available quantity.")
                return

            product_cost = float(product_data[2])
            selling_price = float(product_data[3])

            if selling_price < product_cost:
                print("Selling price cannot be lower than the cost.")
                return

            product_data[4] = str(new_quantity)
            product_data[5] = str(new_sold)

            updated_line = ",".join(product_data)
            updated_lines = [updated_line + "\n" if l == line else l for l in lines]

            with open("products.txt", "w") as file:
                file.writelines(updated_lines)

            print("Product updated successfully!")
            break

    if not found:
        print("Product not found.")
        new_product_name = input("Enter the name of the product to update: ")
        if new_product_name != "":
            update_product(new_product_name)

def analytics():
    display_products()
    with open("products.txt", "r") as file:
        products = [line.strip().split(",") for line in file.readlines()]

    if not products:
        print("No products found.")
        return

    total_revenue = compute_total_revenue(products)
    total_profit = compute_profit(products)
    best_selling_product = compute_best_selling_product(products)

    print("===================================================")
    print("Analytics:")
    print("Total Revenue:", total_revenue)
    print("Total Profit:", total_profit)
    print("===================================================")
    if best_selling_product:
        print("Best Selling Product:", best_selling_product[0])
    else:
        print("Best Selling Product: None")

