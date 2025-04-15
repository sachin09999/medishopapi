import sqlite3

def authUser(email,password):
    conn = sqlite3.connect('my_medical_shop.db')
    curor = conn.cursor()

    cursor.execute("SELECT * FROM users where email = ? AND password = ?",(email,password))
    user = cursor.fetchone()
    conn.close()