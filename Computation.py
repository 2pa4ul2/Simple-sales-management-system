def compute_total_revenue(products):
    total_revenue = 0
    for product in products:
        selling_price = float(product[3])
        sold = int(product[5])
        total_revenue += selling_price * sold
    return total_revenue

def compute_profit(products):
    total_profit = 0
    total_expenses = 0
    for product in products:
        product_cost = float(product[2])
        quantity = int(product[4])
        total_expenses += product_cost * quantity

    total_revenue = 0
    for product in products:
        selling_price = float(product[3])
        sold = int(product[5])
        total_revenue += selling_price * sold

    for product in products:
        product_cost = float(product[2])
        selling_price = float(product[3])
        sold = int(product[5])
        total_profit = total_revenue - total_expenses
    return total_profit

def compute_best_selling_product(products):
    best_selling_product = None
    max_sold = 0
    for product in products:
        sold = int(product[5])
        if sold > max_sold:
            best_selling_product = product
            max_sold = sold
    return best_selling_product

def compute_total_sold(products):
    total_sold = 0
    for product in products:
        sold = int(product[5])
        total_sold += sold
    return total_sold

def compute_profit_percentage(products):
    total_revenue = compute_total_revenue(products)
    total_profit = compute_profit(products)
    if total_revenue != 0:
        profit_percentage = (total_profit / total_revenue) * 100
    else:
        profit_percentage = 0
    return profit_percentage

def compute_average_price(products):
    total_price = 0
    total_sold = 0
    for product in products:
        price = float(product[3])
        sold = int(product[5])
        total_price += price * sold
        total_sold += sold
    if total_sold != 0:
        average_price = total_price / total_sold
    else:
        average_price = 0
    return average_price
def compute_total_expenses(products):
    total_expenses = 0
    for product in products:
        product_cost = float(product[2])
        quantity = int(product[4])
        total_expenses += product_cost * quantity
    return total_expenses

def compute_average_profit_margin(products):
    total_margin = 0
    for product in products:
        product_cost = float(product[2])
        selling_price = float(product[3])
        sold = int(product[5])
        profit = (selling_price - product_cost) * sold
        profit_margin = (profit / selling_price) * 100
        total_margin += profit_margin
    if len(products) != 0:
        average_margin = total_margin / len(products)
    else:
        average_margin = 0
    return average_margin



