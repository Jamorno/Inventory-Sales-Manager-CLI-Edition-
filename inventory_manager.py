import json

class InventoryManager:
    def __init__(self):
        self.products = {}
        self.sales_total = {}

    def add_Product(self, product_name, stock):
        if product_name in self.products:
            self.products[product_name] += stock
        else:
            self.products[product_name] = stock

        print(f"Add - {product_name}: {stock}")

    def show_stock(self):
        if not self.products:
            print("No product in stock.")
            return

        print("Current stock:")
        for name, stock in self.products.items():
            print(f"{name}: {stock}")

    def remove_product(self, product_name, amount):
        if product_name not in self.products:
            print(f"{product_name} not found in stock")
            return

        if self.products[product_name] < amount:
            print(f"Not enough stock for {product_name}")
            return

        self.products[product_name] -= amount
        self.sales_total[product_name] = self.sales_total.get(product_name, 0) + amount
        print(f"Removed {amount} from {product_name}")

    def show_sales_report(self):
        if not self.sales_total:
            print("No sales data available.")
            return

        print("Sales report:")
        total_sales = 0
        for name, amount in self.sales_total.items():
            print(f"{name}: {amount}")
            total_sales += amount

        print(f"Total item sold: {total_sales}")

    def save_report(self):
        with open("inventory.json", "w") as file:
            json.dump(self.products, file)

    def load_report(self):
        try:
            with open("inventory.json", "r") as file:
                self.products = json.load(file)
        except FileNotFoundError:
            self.products = {}