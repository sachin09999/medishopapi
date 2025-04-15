from datetime import date
import sqlite3
import uuid

def createUser(name, password, phoneNumber, email, pinCode, address):
    conn = sqlite3.connect('my_medicalShop.db')
    c = conn.cursor()

    userID = str(uuid.uuid4())  # Generate unique user ID
    dateOfAccountCreation = date.today()  # Get today's date

    # Corrected SQL query (removed extra comma before `)`)
    c.execute("""
        INSERT INTO users (user_id, password, date_of_account_creation, isApproved, block, name, address, email, phone_number, pin_code) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (userID, password, dateOfAccountCreation, 0, 0, name, address, email, phoneNumber, pinCode))

    conn.commit()
    conn.close()
