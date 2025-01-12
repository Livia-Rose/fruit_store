# fruit store

import mysql.connector as mpc
con = mpc.connect(host="localhost", user="root", password="naeva", database="ms")
cursor = con.cursor()



insert_query = "Insert Into items (SI_no, Name, Quantity, Price) Values (%s, %s, %s, %s)"
def restock():
        
        SI_no = int(input("Enter no: "))
        Name = input("Enter the name of the item: ")
        Price = float(input("Enter the price of the item: "))
        Quantity = int(input("Enter the quantity of the item: "))

        cursor.execute(insert_query, (SI_no, Name, Quantity, Price))
        con.commit()

        print(f"Item '{Name}' added successfully!")

        more = input("Do you want to add another item? (yes/no): ").strip().lower()
        if more == 'yes':
                restock()
            

from prettytable import PrettyTable

def view():
    view_query = "select*from items;"
    cursor.execute(view_query)
    rows = cursor.fetchall()
    if rows:
        table = PrettyTable()
        column_names = [description[0] for description in cursor.description]
        table.field_names = column_names
        for row in rows:
            table.add_row(row)
        print("\n======== Goods Table ========")
        print(table)
    else:
        print("The table is empty.")


from prettytable import PrettyTable

def buying():
    items_bought = []
    bill_total = 0.0
    view()
    ch = input('Would you like something? (y/n): ')
    while ch == 'y':
        SI_no = int(input("Enter the item number (SI_no): "))
        purchase = int(input("Enter the quantity to buy: "))

        cursor.execute("SELECT Name, Quantity, Price FROM items WHERE SI_no = %s", (SI_no,))
        result = cursor.fetchone()

        if result is None:
            print("Item not found!")
            continue  

        name, current_quantity, price = result
        if current_quantity < purchase:
            print(f"Not enough quantity! Current quantity is {current_quantity}.")
            continue

        new_quantity = current_quantity - purchase
        cursor.execute("UPDATE items SET Quantity = %s WHERE SI_no = %s", (new_quantity, SI_no))
        con.commit()

        total_price = purchase * price
        items_bought.append((SI_no, name, purchase, price, total_price))
        bill_total += total_price

        ch = input('Anything else? (y/n): ')

    if items_bought:
        print("\n========== BILL ==========")
        table = PrettyTable()
        table.field_names = ["SI_no", "Name", "Quantity", "Price (Each)", "Total Price"]
        for item in items_bought:
            table.add_row(item)
        print(table)
        print(f"\nGrand Total: {bill_total:.2f}")
    else:
        print("No items were bought.")


        
while True:
    print("\nOptions:")
    print("1. Restock items")
    print("2. buy")
    print("3. browse items")
    print("4. Exit")
    p=1234
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        s=int(input('enter password '))
        if s==p:
            restock()
    elif choice == "2":
        buying()
    elif choice == "3":
        view()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")








        
       
        


    
