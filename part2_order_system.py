

#Part 2: Data Structures

# Task 1


# given data

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

# making category list manually
category_names = ["Starters", "Mains", "Desserts"]

# printing menu

for cat in category_names:

    print("\n===== " + cat + " =====")

    # checking each item in menu
    for item in menu:

        # checking category match
        if menu[item]["category"] == cat:

            price_val = menu[item]["price"]
            is_available = menu[item]["available"]

            # checking availability
            if is_available == True:
                text_status = "Available"
            else:
                text_status = "Unavailable"

            # printing details
            print(item, "₹" + str(price_val), "[" + text_status + "]")


#  total items

total_items = len(menu)
print("\nTotal items in menu:", total_items)


#  count available items

available_items = 0

for item in menu:
    if menu[item]["available"] == True:
        available_items = available_items + 1

print("Total available items:", available_items)


# most expensive item
max_price = 0
max_item_name = ""

for item in menu:

    current_price = menu[item]["price"]

    if current_price > max_price:
        max_price = current_price
        max_item_name = item

print("Most expensive item:", max_item_name, "₹" + str(max_price))


# items under 150

print("\nItems under ₹150:")

for item in menu:

    current_price = menu[item]["price"]

    if current_price < 150:
        print(item, "₹" + str(current_price))

     
===== Starters =====
Paneer Tikka ₹180.0 [Available]
Chicken Wings ₹220.0 [Unavailable]
Veg Soup ₹120.0 [Available]

===== Mains =====
Butter Chicken ₹320.0 [Available]
Dal Tadka ₹180.0 [Available]
Veg Biryani ₹250.0 [Available]
Garlic Naan ₹40.0 [Available]

===== Desserts =====
Gulab Jamun ₹90.0 [Available]
Rasgulla ₹80.0 [Available]
Ice Cream ₹110.0 [Unavailable]

Total items in menu: 10
Total available items: 8
Most expensive item: Butter Chicken ₹320.0

Items under ₹150:
Veg Soup ₹120.0
Garlic Naan ₹40.0
Gulab Jamun ₹90.0
Rasgulla ₹80.0
Ice Cream ₹110.0

#  Task 2

# given menu
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

# cart (given)
cart = []


# function to add item
def add_item(item_name, qty):

    # check if item exists
    if item_name not in menu:
        print("Item not found in menu")
        print_cart()
        return

    # check if available
    if menu[item_name]["available"] == False:
        print("Item is not available")
        print_cart()
        return

    # check if already in cart
    found_flag = False

    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = entry["quantity"] + qty
            found_flag = True

    # if not found, add new item
    if found_flag == False:
        cart.append({
            "item": item_name,
            "quantity": qty,
            "price": menu[item_name]["price"]
        })

    print("Item added or updated")
    print_cart()


# function to remove item
def remove_item(item_name):

    found_flag = False

    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            found_flag = True
            print("Item removed")

    if found_flag == False:
        print("Item not in cart")

    print_cart()


# ---------- function to print cart ----------
def print_cart():

     # simple readable format
    for entry in cart:
        print(entry["item"], "x", entry["quantity"])

    # dictionary format (important for marks)

    for entry in cart:
        print(entry)

    print()


# SIMULATION

add_item("Paneer Tikka", 2)
add_item("Gulab Jamun", 1)
add_item("Paneer Tikka", 1)
add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)
remove_item("Gulab Jamun")


# FINAL BILL

print("========== Order Summary ==========")

total_bill = 0

for entry in cart:

    item_total = entry["quantity"] * entry["price"]
    total_bill = total_bill + item_total

    print(entry["item"], "x" + str(entry["quantity"]), "₹" + str(item_total))

print("------------------------------------")

gst_amount = total_bill * 0.05
final_amount = total_bill + gst_amount

print("Subtotal: ₹", total_bill)
print("GST (5%): ₹", round(gst_amount, 2))
print("Total Payable: ₹", round(final_amount, 2))
print("====================================")
     
Item added or updated
Paneer Tikka x 2
{'item': 'Paneer Tikka', 'quantity': 2, 'price': 180.0}

Item added or updated
Paneer Tikka x 2
Gulab Jamun x 1
{'item': 'Paneer Tikka', 'quantity': 2, 'price': 180.0}
{'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}

Item added or updated
Paneer Tikka x 3
Gulab Jamun x 1
{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}
{'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}

Item not found in menu
Paneer Tikka x 3
Gulab Jamun x 1
{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}
{'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}

Item is not available
Paneer Tikka x 3
Gulab Jamun x 1
{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}
{'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}

Item removed
Paneer Tikka x 3
{'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}

========== Order Summary ==========
Paneer Tikka x3 ₹540.0
------------------------------------
Subtotal: ₹ 540.0
GST (5%): ₹ 27.0
Total Payable: ₹ 567.0
====================================

# Task 3

import copy   # used for deep copy

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0}
]

# Step 1: make backup
inventory_backup = copy.deepcopy(inventory)

print("\nBackup created successfully")


# Step 2: check deep copy

# changing one value in original inventory
inventory["Paneer Tikka"]["stock"] = 5

print("\nAfter changing original inventory:")
print("Original:", inventory["Paneer Tikka"])
print("Backup  :", inventory_backup["Paneer Tikka"])

# restoring original value manually
inventory["Paneer Tikka"]["stock"] = 10


# Step 3: deduct items from cart

print("\nUpdating inventory based on cart...")

for cart_item in cart:

    item_name = cart_item["item"]
    qty_needed = cart_item["quantity"]

    available_stock = inventory[item_name]["stock"]

    # check if enough stock
    if available_stock >= qty_needed:
        inventory[item_name]["stock"] = available_stock - qty_needed

    else:
        print("Warning:", item_name, "has less stock!")

        # reduce only available amount
        inventory[item_name]["stock"] = 0


# Step 4: reorder alert

print("\nChecking for low stock items...")

for item in inventory:

    current_stock = inventory[item]["stock"]
    reorder_level = inventory[item]["reorder_level"]

    if current_stock <= reorder_level:
        print("⚠ Reorder Alert:", item,
              "— Only", current_stock,
              "unit(s) left (reorder level:", reorder_level, ")")



# Step 5: print final comparison

print("\nFinal Inventory (after changes):")
print(inventory)

print("\nBackup Inventory (should be unchanged):")
print(inventory_backup)
     
Backup created successfully

After changing original inventory:
Original: {'stock': 5, 'reorder_level': 3}
Backup  : {'stock': 10, 'reorder_level': 3}

Updating inventory based on cart...

Checking for low stock items...

Final Inventory (after changes):
{'Paneer Tikka': {'stock': 7, 'reorder_level': 3}, 'Chicken Wings': {'stock': 8, 'reorder_level': 2}, 'Veg Soup': {'stock': 15, 'reorder_level': 5}, 'Butter Chicken': {'stock': 12, 'reorder_level': 4}, 'Dal Tadka': {'stock': 20, 'reorder_level': 5}, 'Veg Biryani': {'stock': 6, 'reorder_level': 3}, 'Garlic Naan': {'stock': 30, 'reorder_level': 10}, 'Gulab Jamun': {'stock': 5, 'reorder_level': 2}, 'Rasgulla': {'stock': 4, 'reorder_level': 3}, 'Ice Cream': {'stock': 7, 'reorder_level': 4}}

Backup Inventory (should be unchanged):
{'Paneer Tikka': {'stock': 10, 'reorder_level': 3}, 'Chicken Wings': {'stock': 8, 'reorder_level': 2}, 'Veg Soup': {'stock': 15, 'reorder_level': 5}, 'Butter Chicken': {'stock': 12, 'reorder_level': 4}, 'Dal Tadka': {'stock': 20, 'reorder_level': 5}, 'Veg Biryani': {'stock': 6, 'reorder_level': 3}, 'Garlic Naan': {'stock': 30, 'reorder_level': 10}, 'Gulab Jamun': {'stock': 5, 'reorder_level': 2}, 'Rasgulla': {'stock': 4, 'reorder_level': 3}, 'Ice Cream': {'stock': 7, 'reorder_level': 4}}

# TASK 4

# given data (must include)
sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# STEP 1-revenue per day

print("Revenue per day:\n")

day_wise_total = {}

for each_date in sales_log:
    money_sum = 0

    for each_order in sales_log[each_date]:
        money_sum = money_sum + each_order["total"]

    day_wise_total[each_date] = money_sum

    print(each_date, "→ ₹", money_sum)


# STEP 2- best day

highest_money = 0
top_day = ""

for each_date in day_wise_total:
    if day_wise_total[each_date] > highest_money:
        highest_money = day_wise_total[each_date]
        top_day = each_date

print("\nBest Day:", top_day, "₹", highest_money)


#  STEP 3- most ordered item

item_counter = {}

for each_date in sales_log:
    for each_order in sales_log[each_date]:
        for each_food in each_order["items"]:

            if each_food in item_counter:
                item_counter[each_food] = item_counter[each_food] + 1
            else:
                item_counter[each_food] = 1


highest_count = 0
most_item = ""

for each_food in item_counter:
    if item_counter[each_food] > highest_count:
        highest_count = item_counter[each_food]
        most_item = each_food

print("\nMost Ordered Item:", most_item, "(", highest_count, "times )")


# STEP 4- add new day

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print("\nNew day added!")


#  STEP 5- updated revenue

print("\nUpdated Revenue:\n")

for each_date in sales_log:
    money_sum = 0

    for each_order in sales_log[each_date]:
        money_sum = money_sum + each_order["total"]

    print(each_date, "→ ₹", money_sum)


# STEP 6- best day again

highest_money = 0
top_day = ""

for each_date in sales_log:
    money_sum = 0

    for each_order in sales_log[each_date]:
        money_sum = money_sum + each_order["total"]

    if money_sum > highest_money:
        highest_money = money_sum
        top_day = each_date

print("\nNew Best Day:", top_day, "₹", highest_money)


# STEP 7- print all orders

print("\nAll Orders:\n")

counter = 1

for each_date in sales_log:
    for each_order in sales_log[each_date]:

        print(str(counter) + ". [" + each_date + "] Order #" + str(each_order["order_id"]),
              "— ₹" + str(each_order["total"]),
              "— Items:", ", ".join(each_order["items"]))

        counter = counter + 1
     
Revenue per day:

2025-01-01 → ₹ 790.0
2025-01-02 → ₹ 560.0
2025-01-03 → ₹ 960.0
2025-01-04 → ₹ 570.0

Best Day: 2025-01-03 ₹ 960.0

Most Ordered Item: Garlic Naan ( 5 times )

New day added!

Updated Revenue:

2025-01-01 → ₹ 790.0
2025-01-02 → ₹ 560.0
2025-01-03 → ₹ 960.0
2025-01-04 → ₹ 570.0
2025-01-05 → ₹ 750.0

New Best Day: 2025-01-03 ₹ 960.0

All Orders:

1. [2025-01-01] Order #1 — ₹220.0 — Items: Paneer Tikka, Garlic Naan
2. [2025-01-01] Order #2 — ₹210.0 — Items: Gulab Jamun, Veg Soup
3. [2025-01-01] Order #3 — ₹360.0 — Items: Butter Chicken, Garlic Naan
4. [2025-01-02] Order #4 — ₹220.0 — Items: Dal Tadka, Garlic Naan
5. [2025-01-02] Order #5 — ₹340.0 — Items: Veg Biryani, Gulab Jamun
6. [2025-01-03] Order #6 — ₹260.0 — Items: Paneer Tikka, Rasgulla
7. [2025-01-03] Order #7 — ₹570.0 — Items: Butter Chicken, Veg Biryani
8. [2025-01-03] Order #8 — ₹130.0 — Items: Garlic Naan, Gulab Jamun
9. [2025-01-04] Order #9 — ₹300.0 — Items: Dal Tadka, Garlic Naan, Rasgulla
10. [2025-01-04] Order #10 — ₹270.0 — Items: Paneer Tikka, Gulab Jamun
11. [2025-01-05] Order #11 — ₹490.0 — Items: Butter Chicken, Gulab Jamun, Garlic Naan
12. [2025-01-05] Order #12 — ₹260.0 — Items: Paneer Tikka, Rasgulla
