# fruit_store
Overview
The Fruit Store Management System is a Python-based console application designed to manage inventory, facilitate customer purchases, and generate bills. It uses a MySQL database for data storage and provides an interactive interface for both store administrators and customers.

Features
Restock Inventory:

Add new items to the inventory with details like:
Serial Number (SI_no)
Item Name
Quantity
Price
Secured with a password to prevent unauthorized access.
Browse Inventory:

View the complete list of items in stock in a tabular format.
Organized display of item details such as Serial Number, Name, Quantity, and Price.
Buying Items:

Customers can purchase items by:
Selecting the item by Serial Number.
Specifying the quantity.
Validates stock availability before completing the purchase.
Updates inventory automatically after a transaction.
Generates a detailed bill including:
Items bought
Quantity
Price per unit
Total cost
Grand total for all items purchased.
Exit Option:

Allows users to safely exit the application.
Prerequisites
1. Python Libraries:
mysql.connector: For database connectivity.
prettytable: For displaying inventory and bill in a tabular format.
Install these libraries using:

bash
Copy code
pip install mysql-connector-python prettytable
2. MySQL Setup:
Ensure MySQL server is installed and running.
Create a database named ms with a table items using the following schema:
sql
Copy code
CREATE DATABASE ms;

USE ms;

CREATE TABLE items (
    SI_no INT PRIMARY KEY,
    Name VARCHAR(255),
    Quantity INT,
    Price FLOAT
);
How to Run
Clone the repository or download the Fruit store.py file.
Set up the MySQL database as described above.
Update the connection parameters in the code to match your MySQL credentials:
python
Copy code
con = mpc.connect(host="localhost", user="root", password="your_password", database="ms")
Run the script:
bash
Copy code
python Fruit store.py
Follow the on-screen prompts to perform various operations.
Usage Instructions
Menu Options:
Restock Items:
Enter the administrator password to access this option.
Input the details of the items to add to the inventory.
Browse Items:
View all the items currently available in the store.
Buy Items:
Browse the inventory, select items by Serial Number, and specify the quantity to purchase.
Review the generated bill at the end of the transaction.
Exit:
Close the application.
Security
The restocking option is protected by a password. Ensure you update the password (p=1234) in the code as needed.
Potential Enhancements
Add data validation for inputs (e.g., prevent negative values).
Implement password hashing for improved security.
Introduce a graphical user interface (GUI).
Add features like sales reports and low-stock alerts.
License
This project is open-source and free to use.
