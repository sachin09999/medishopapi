import sqlite3

def approveUser(userId, isApproved):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    # Update the user's approval status
    cursor.execute("UPDATE users SET isApproved = ? WHERE user_id = ?", (isApproved, userId))

    conn.commit()
    conn.close()

    return {'message': 'User approval status updated successfully', 'status': 200}

def updateUserDetails(user_id, **kwargs):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    fields = []
    values = []

    for key, value in kwargs.items():
        fields.append(f"{key} = ?")
        values.append(value)

    if not fields:
        return {"message": "No data to update", "status": 400}

    values.append(user_id)
    query = f"UPDATE users SET {', '.join(fields)} WHERE user_id = ?"
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return {"message": "User updated successfully", "status": 200}


def deleteUser(user_id):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

    return True  # You can also check if a row was deleted with cursor.rowcount

def addProduct(product_id,product_name, product_price, product_quantity, category, stock_quantity):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO products (product_id, product_name, product_price, product_quantity, category, stock_quantity) VALUES (?, ?, ?, ?, ?, ?)",
                   (product_id, product_name, product_price, product_quantity, category, stock_quantity))
    conn.commit()
    conn.close()
    return {'message': 'Product added successfully', 'status': 200}


def addOrder(order_id, user_id, product_id, order_date, isApproved, price, product_name, quantity, total_amount,user_name,message,category):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO orders (
            order_id, user_id, product_id, order_date,
            isApproved, price, product_name, quantity, total_amount, user_name, message, category
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        order_id, user_id, product_id, order_date,
        isApproved, price, product_name, quantity, total_amount,user_name, message, category
    ))

    conn.commit()
    conn.close()

    return {'message': 'Order added successfully', 'status': 200}

def sellhistory(sell_id,product_id,quantity,remaining_quantity,date_of_sell,total_amount,price,product_name,user_id,username):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sellhistory (
            sell_id, product_id, quantity, remaining_quantity, date_of_sell,
            total_amount, price, product_name, user_id, username
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        sell_id, product_id, quantity, remaining_quantity, date_of_sell,
        total_amount, price, product_name, user_id, username
    ))

    conn.commit()
    conn.close()

    return {'message': 'Sell history added successfully', 'status': 200}