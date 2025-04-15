import sqlite3
from flask import jsonify

def getSpecificUser(userId):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id = ?", (userId,))
    user = cursor.fetchone()
    conn.close()

    if user is None:
        return jsonify({'message': 'User not found', 'status': 404})

    tempUser = {
        "id": user[0],
        "user_id": user[1],
        "password": user[2],
        "date_of_account_creation": user[3],
        "isApproved": user[4],
        "block": user[5],
        "name": user[6],
        "address": user[7],
        "email": user[8],
        "phone_number": user[9],
        "pin_code": user[10]
    }

    return jsonify(tempUser)