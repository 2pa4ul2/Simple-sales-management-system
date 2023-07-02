def compute_total_revenue(products):
    total_revenue = 0
    for product in products:
        selling_price = float(product[3])
        sold = int(product[5])
        total_revenue += selling_price * sold
    return total_revenue

def compute_profit(products):
    total_profit = 0
    for product in products:
        product_cost = float(product[2])
        selling_price = float(product[3])
        sold = int(product[5])
        total_profit += (selling_price - product_cost) * sold
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