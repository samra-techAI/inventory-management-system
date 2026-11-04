
import json
import os

FILE_NAME = "inventory.json"


def load_inventory():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_inventory(inventory):
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)


def add_product(inventory):
    product_id = input("Enter product ID: ")

    if product_id in inventory:
        print("Product already exists!")
        return

    name = input("Enter product name: ")
    
    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            return

        inventory[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        save_inventory(inventory)
        print("Product added successfully!")

    except ValueError:
        print("Please enter valid numbers.")


def view_products(inventory):
    if not inventory:
        print("No products available.")
        return

    for product_id, product in inventory.items():
        print("\nProduct ID:", product_id)
        print("Name:", product["name"])
        print("Price:", product["price"])
        print("Stock:", product["quantity"])


def search_product(inventory):
    product_id = input("Enter product ID: ")

    if product_id in inventory:
        print(inventory[product_id])
    else:
        print("Product not found!")


def update_stock(inventory):
    product_id = input("Enter product ID: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter new stock quantity: "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        inventory[product_id]["quantity"] = quantity
        save_inventory(inventory)

        print("Stock updated successfully!")

    except ValueError:
        print("Please enter a valid quantity.")


def record_sale(inventory):
    product_id = input("Enter product ID: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter quantity sold: "))

        if quantity <= 0:
            print("Enter a quantity greater than zero.")
            return

        product = inventory[product_id]

        if quantity > product["quantity"]:
            print("Not enough stock available!")
            return

        total = quantity * product["price"]
        product["quantity"] -= quantity

        save_inventory(inventory)

        print("Sale completed!")
        print("Total amount:", total)

    except ValueError:
        print("Please enter a valid quantity.")


def low_stock_alert(inventory):
    print("\nProducts with low stock:")

    found = False

    for product_id, product in inventory.items():
        if product["quantity"] <= 5:
            print(product["name"], "-", product["quantity"])
            found = True

    if not found:
        print("No low-stock products!")


def main():
    inventory = load_inventory()

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Record Sale")
        print("6. Low Stock Alert")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product(inventory)

        elif choice == "2":
            view_products(inventory)

        elif choice == "3":
            search_product(inventory)

        elif choice == "4":
            update_stock(inventory)

        elif choice == "5":
            record_sale(inventory)

        elif choice == "6":
            low_stock_alert(inventory)

        elif choice == "7":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
