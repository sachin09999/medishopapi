import sqlite3


def createTable():

    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()


    cursor.execute('''

CREATE TABLE IF NOT EXISTS Users(
                  
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id VARCHAR(255),
                  password VARCHAR(255),
                  date_of_account_creation DATE,
                  isApproved BOOLEAN,
                  block BOOLEAN,
                  name VARCHAR(255),
                  address VARCHAR(255),
                  email VARCHAR(255),
                  phone_number VARCHAR(255),
                  pin_code VARCHAR(255)
                  )

''')
    
    # Create the table for products

    cursor.execute('''

           CREATE TABLE IF NOT EXISTS Products(
                  
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  product_id VARCHAR(255),
                  product_name VARCHAR(255),
                  product_price FLOAT,
                  category VARCHAR(255),
                  stock_quantity INTEGER

                  )
                  
                  '''
)
    
    # Create the table for orders
    cursor.execute('''

CREATE TABLE IF NOT EXISTS Order_details(
                  
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  order_id VARCHAR(255),
                  user_id VARCHAR(255),
                  product_id VARCHAR(255),
                  order_date DATE,
                  isApproved BOOLEAN,
                  price FLOAT,
                  product_name VARCHAR(255),    
                  quantity INTEGER,
                  total_amount FLOAT,
                  user_name VARCHAR(255),
                  message VARCHAR(1000),
                  category VARCHAR(255)

                  )
                  
                  '''
)
    
    # Create the table for sell history

    cursor.execute('''

CREATE TABLE IF NOT EXISTS Sell_history(
                  
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  sell_id VARCHAR(255),
                    product_id VARCHAR(255),
                  quantity INTEGER,
                  remaining_quantity INTEGER,
                  date_of_sell DATE,
                  total_amount FLOAT,
                  price FLOAT,
                    product_name VARCHAR(255),
                  user_id VARCHAR(255),
                  user_name VARCHAR(255)

                  )
                  
                 '''
)
    
    conn.commit()
    conn.close()

