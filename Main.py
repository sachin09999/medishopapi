from flask import Flask,jsonify, request
from createTableOperation import createTable
from addOperation import createUser
from authUser import authUser
from readFunction import getSpecificUser
from updateOperation import approveUser, updateUserDetails, addProduct , deleteUser ,addOrder

app = Flask(__name__)

@app.route('/user',methods=['GET'])
def hello():
    return jsonify({'name' : 'Sachin' , 
            'phone' : '393939',
            'email' : 'sachin@gmail.com'})

@app.route('/createuser', methods=['POST'])
def create_user():
    
    name = request.form['name']
    password = request.form['password']
    phoneNumber = request.form['phoneNumber']
    email = request.form['email']
    pinCode = request.form['pinCode']
    address = request.form['address']

    createUser(name,password,phoneNumber,email,pinCode,address)


    return jsonify({'message' : 'User created Succesfully', "status" :200})

@app.route('/login', methods=['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']

        user = authUser(email,password)

        if user: 
            return jsonify({'message' : 'Login Succesfully', "status" :200})
        else:
            return jsonify({'message' : 'Invalid Credentials', "status" :400})
        
    except Exception as e:
        return jsonify({'message' : 'Invalid Request', "status" :400}) 


@app.route('/getspecificuser', methods=['POST'])
def get_Specific_user():
    try:
        userId = request.form['user_id']

        user = getSpecificUser(userId = userId)

        return user

    except Exception as e:
        return jsonify({'message' : str(e), "status" :400})

@app.route('/approveuser', methods=['PATCH'])
def approve_user():
    try:
        user_id = request.form['user_id']
        isApproved = request.form['isApproved']

        user = approveUser(userId = user_id, isApproved = isApproved)

        return jsonify({'message' : 'User Approved Succesfully', "status" :200})

    except Exception as e:
        return jsonify({'message' : 'Invalid Request', "status" :400})
    
@app.route('/updateuserprofile', methods=['PATCH'])
def update_user_profile():
    try:
        user_id = request.form['user_id']

        # Collect optional fields
        update_fields = {}
        for field in ['name', 'phoneNumber', 'email', 'address', 'pinCode']:
            if field in request.form:
                update_fields[field] = request.form[field]

        if not update_fields:
            return jsonify({'message': 'No fields to update', 'status': 400})

        result = updateUserDetails(user_id, **update_fields)
        return jsonify(result)

    except Exception as e:
        return jsonify({'message': str(e), 'status': 400})
    
@app.route('/deleteuser', methods=['DELETE'])
def delete_user():
    try:
        user_id = request.form['user_id']

        success = deleteUser(user_id)
        if success:
            return jsonify({'message': 'User deleted successfully', 'status': 200})
        else:
            return jsonify({'message': 'User not found or already deleted', 'status': 404})

    except Exception as e:
        return jsonify({'message': str(e), 'status': 400})   

@app.route('/addproduct', methods=['POST'])
def add_product():
    try:
        product_name = request.form['product_name']
        product_price = request.form['product_price']
        product_quantity = request.form['product_quantity']
        category = request.form['category']
        stock_quantity = request.form['stock_quantity']

        addProduct(product_name, product_price, product_quantity, category, stock_quantity)

        return jsonify({'message': 'Product added successfully', 'status': 200})

    except Exception as e:
        return jsonify({'message': str(e), 'status': 400})     

@app.route('/addorder', methods=['POST'])
def add_order():
    try:
        order_id = request.form['order_id']
        user_id = request.form['user_id']
        product_id = request.form['product_id']
        order_date = request.form['order_date']
        isApproved = request.form['isApproved']
        price = request.form['price']
        product_name = request.form['product_name']
        quantity = request.form['quantity']
        total_amount = request.form['total_amount']
        user_name = request.form['user_name']
        message = request.form['message']
        category = request.form['category']

        result = addOrder(
            order_id, user_id, product_id, order_date,
            isApproved, price, product_name, quantity, total_amount,
            user_name, message, category
        )

        return jsonify(result)

    except Exception as e:
        return jsonify({'message': str(e), 'status': 400})
    

@app.route('/addsellhistory', methods=['POST'])
def get_sell_history():
    try:
        # Assuming you have a function to fetch the sell history
        sell_id = request.form['sell_id']
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        remaining_quantity = request.form['remaining_quantity']
        date_of_sell = request.form['date_of_sell']
        total_amount = request.form['total_amount']
        price = request.form['price']
        product_name = request.form['product_name']
        user_id = request.form['user_id']
        user_name = request.form['user_name']

        result = sellhistory(
            sell_id, product_id, quantity,
            remaining_quantity, date_of_sell, total_amount,
            price, product_name, user_id, user_name
        )
        return jsonify({'message': 'sell history fetch', 'status': 200})

    except Exception as e:
        return jsonify({'message': str(e), 'status': 400})    

if __name__== '__main__':
    createTable() 
    app.run(debug=True)