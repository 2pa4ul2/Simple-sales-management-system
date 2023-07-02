from Computation import *

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

        if not products:
            print("No products found.")
        else:
            print("Product Name\tBrand\tCost\tPrice\tQuantity\tSold")
            for product in products:
                product_data = product.strip().split(",")
                print(
                    f"{product_data[0]}\t{product_data[1]}\t{product_data[2]}\t{product_data[3]}\t{product_data[4]}\t{product_data[5]}"
                )


def update_product():
    product_name = input("Enter the product name to update: ")
    new_quantity = int(input("Enter the new quantity: "))
    new_sold = int(input("Enter the new sold quantity: "))

    with open("products.txt", "r") as file:
        lines = file.readlines()

    updated_lines = []
    found = False

    for line in lines:
        product_data = line.strip().split(",")
        if product_data[0] == product_name:
            quantity = int(product_data[4])
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
            found = True
        updated_line = ",".join(product_data)
        updated_lines.append(updated_line + "\n")

    if found:
        with open("products.txt", "w") as file:
            file.writelines(updated_lines)
        print("Product updated successfully!")
    else:
        print("Product not found.")

def analytics():
    with open("products.txt", "r") as file:
        products = [line.strip().split(",") for line in file.readlines()]

    if not products:
        print("No products found.")
        return

    total_revenue = compute_total_revenue(products)
    total_profit = compute_profit(products)
    best_selling_product = compute_best_selling_product(products)

    print("Analytics:")
    print("Total Revenue:", total_revenue)
    print("Total Profit:", total_profit)
    if best_selling_product:
        print("Best Selling Product:", best_selling_product[0])
    else:
        print("Best Selling Product: None")