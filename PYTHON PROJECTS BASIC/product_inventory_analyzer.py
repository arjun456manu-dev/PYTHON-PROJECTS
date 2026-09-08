inventory = {
    "Laptop": {"stock": 12, "price": 55000},
    "Mouse": {"stock": 45, "price": 800},
    "Keyboard": {"stock": 30, "price": 1500},
    "Monitor": {"stock": 8, "price": 12000},
    "Headphones": {"stock": 20, "price": 2500}
}

def inventory_report(inventory):
    total_products = sum(inventory["Laptop"]["stock"]["price"])
    print(total_products)
inventory_report(inventory)