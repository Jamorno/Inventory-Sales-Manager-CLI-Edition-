from inventory_manager import InventoryManager

manager = InventoryManager()
manager.load_report()

while True:
    user_option = input("Enter option\n1.Add product\n2.Show stock\n3.Remove product\n4.Show sales report\n5.End\n")

    if user_option == "1":
        product_name = input("Enter product name: ")
        stock = int(input("Enter stock product: "))
        manager.add_Product(product_name, stock)
    elif user_option == "2":
        manager.show_stock()
    elif user_option == "3":
        product_name = input("Enter product name to remove: ")
        amount = int(input("Enter amount to remove: "))
        manager.remove_product(product_name, amount)
    elif user_option == "4":
        manager.show_sales_report()
    elif user_option == "5":
        manager.save_report()
        print("Save report complete")
        break