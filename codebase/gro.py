
# Grocery Store Management System
# Python 3 Project

# Inventory using Dictionary
inventory = {
    "Rice": {"price": 50, "stock": 100},
    "Sugar": {"price": 45, "stock": 50},
    "Milk": {"price": 30, "stock": 40},
    "Oil": {"price": 150, "stock": 20}
}


# Function to display inventory
def view_stock():
    print("\n------ AVAILABLE STOCK ------")

    for item in inventory:
        print(item, "- Price:", inventory[item]["price"],
              "- Stock:", inventory[item]["stock"])

    print("-----------------------------")


# Function to generate new bill
def new_bill():

    cart = []
    bill_valid = True

    print("\n------ NEW BILL ------")
    print("Enter 'done' when all items are added.")

    while True:

        item = input("\nEnter item name: ").strip().title()

        if item == "Done":
            break

        # Check whether item exists
        if item not in inventory:
            print("Item", item, "not found in inventory.")
            bill_valid = False
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                bill_valid = False
                continue

        except ValueError:
            print("Invalid quantity. Enter a whole number.")
            bill_valid = False
            continue

        # Calculate already added quantity
        added_quantity = 0

        for product in cart:
            if product["name"] == item:
                added_quantity += product["quantity"]

        available = inventory[item]["stock"] - added_quantity

        # Check stock availability
        if quantity > available:
            print("Insufficient stock for", item,
                  ". Available:", available)
            bill_valid = False
            continue

        # Add item to cart
        cart.append({
            "name": item,
            "quantity": quantity,
            "price": inventory[item]["price"]
        })

        print(item, "added to cart successfully.")

    # Check whether cart is empty
    if len(cart) == 0:
        print("\nNo items added to cart.")
        return

    # Stop billing if any invalid input occurred
    if bill_valid == False:
        print("\nBill not generated due to invalid input.")
        print("Stock has not been changed.")
        return

    # Calculate subtotal
    subtotal = 0

    for product in cart:
        subtotal += product["price"] * product["quantity"]

    # Calculate discount
    discount = 0

    if subtotal >= 1000:
        discount = subtotal * 10 / 100

    # Calculate GST after discount
    amount = subtotal - discount
    gst = amount * 5 / 100

    # Calculate final total
    total = amount + gst

    # Display bill
    print("\n========== GROCERY BILL ==========")

    for product in cart:
        print(product["name"],
              "x", product["quantity"],
              "=", product["price"] * product["quantity"])

    print("----------------------------------")
    print("Subtotal: Rs.", format(subtotal, ".2f"))
    print("Discount:", format(discount, ".2f"))
    print("GST (5%):", format(gst, ".2f"))
    print("Total: Rs.", format(total, ".2f"))
    print("==================================")

    # Reduce stock after successful billing
    for product in cart:
        item = product["name"]
        quantity = product["quantity"]

        inventory[item]["stock"] -= quantity

    print("\nStock updated successfully.")

    # Save bill in text file
    with open("bills.txt", "a") as file:

        file.write("\n========== GROCERY BILL ==========\n")

        for product in cart:
            file.write(
                product["name"] + " x " +
                str(product["quantity"]) + " = Rs. " +
                str(product["price"] * product["quantity"]) + "\n"
            )

        file.write("Subtotal: Rs. " + str(round(subtotal, 2)) + "\n")
        file.write("Discount: Rs. " + str(round(discount, 2)) + "\n")
        file.write("GST: Rs. " + str(round(gst, 2)) + "\n")
        file.write("Total: Rs. " + str(round(total, 2)) + "\n")
        file.write("==================================\n")

    print("Bill saved in bills.txt")


# Main program
while True:

    print("\n===== GROCERY STORE MANAGEMENT =====")
    print("1. New Bill")
    print("2. View Stock")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_bill()

    elif choice == "2":
        view_stock()

    elif choice == "3":
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice. Please try again.")
