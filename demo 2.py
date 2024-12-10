# demo 2

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











        
       
        


    
