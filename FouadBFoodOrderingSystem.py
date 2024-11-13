import tkinter as tk
from tkinter import messagebox

dishes_menu = [
    ["Couscous with Vegetables", 7.50],
    ["Chicken Tagine", 8.00],
    ["Lamb Tagine", 9.00],
    ["Harira Soup", 4.00],
    ["Pastilla (Chicken)", 6.50],
    ["Mechoui (Roast Lamb)", 10.00],
    ["Zaalouk (Eggplant Salad)", 5.50],
    ["Bissara (Fava Bean Soup)", 4.50],
    ["Rfissa (Chicken and Lentils)", 7.00],
    ["Tajine of Fish", 8.50]
]

drinks_menu = [
    ["Moroccan Coffee", 2.50],
    ["Moroccan Mint Tea", 2.00],
    ["Mango Juice", 3.00],
    ["Fresh Orange Juice", 2.50],
    ["Hawai Tropical", 1.50],
    ["Poms Apple", 1.50]
]

desserts_menu = [
    ["Msemen with Honey", 2.50],
    ["Briwat (Pastry with Almonds)", 3.00],
    ["Chebakia (Sesame Pastry)", 2.80],
    ["Sellou (Sweet Flour Mix)", 3.20]
]

order = []

def add_to_order(item, category):
    order.append(item)
    messagebox.showinfo("Added", f"Added {item[0]} to your order.")

def display_bill():
    if not order:
        messagebox.showinfo("Your Order", "Your order is empty.")
        return
    
    total_cost = 0
    bill = ""
    for item in order:
        bill += f"{item[0]} - £{item[1]:.2f}\n"
        total_cost += item[1]
    
    bill += f"\nTotal Cost: £{total_cost:.2f}"
    messagebox.showinfo("Final Bill", bill)
    order.clear()

def create_buttons(menu, category):
    for index, item in enumerate(menu, start=1):
        button = tk.Button(menu_frame, text=f"{item[0]} - £{item[1]:.2f}", 
                           width=30, height=2, 
                           command=lambda item=item, category=category: add_to_order(item, category))
        button.pack(pady=5)

def show_menu(category):
    for widget in menu_frame.winfo_children():
        widget.destroy()  
    
    if category == "Dishes":
        create_buttons(dishes_menu, category)
    elif category == "Drinks":
        create_buttons(drinks_menu, category)
    elif category == "Desserts":
        create_buttons(desserts_menu, category)

def category_selection(category):
    show_menu(category)

root = tk.Tk()
root.title("Food Ordering System")

label = tk.Label(root, text="Welcome to QuickBite Food Ordering!", font=("Arial", 16))
label.pack(pady=10)

menu_buttons_frame = tk.Frame(root)
menu_buttons_frame.pack(pady=10)

dishes_button = tk.Button(menu_buttons_frame, text="Dishes", width=15, height=2, 
                          command=lambda: category_selection("Dishes"))
dishes_button.grid(row=0, column=0, padx=10)

drinks_button = tk.Button(menu_buttons_frame, text="Drinks", width=15, height=2, 
                          command=lambda: category_selection("Drinks"))
drinks_button.grid(row=0, column=1, padx=10)

desserts_button = tk.Button(menu_buttons_frame, text="Desserts", width=15, height=2, 
                            command=lambda: category_selection("Desserts"))
desserts_button.grid(row=0, column=2, padx=10)

menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

bill_button = tk.Button(root, text="Display Bill", width=20, height=2, command=display_bill)
bill_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", width=20, height=2, command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
