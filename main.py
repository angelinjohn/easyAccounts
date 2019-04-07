import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from flask_cors import CORS, cross_origin
from werkzeug import generate_password_hash, check_password_hash
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
		
@app.route('/register', methods=['POST'])
@cross_origin()
def add_user():
	try:
		_json = request.json
		_name = _json['name']
		_email = _json['email']
		_password = _json['password']
		# validate the received values
		if _name and _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
			data = (_name, _email, _hashed_password,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/login', methods=['POST'])
@cross_origin()
def login_user():
	try:
		_json = request.json
		_email = _json['email']
		_password = _json['password']
		# validate the received values
		if _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = """SELECT * FROM tbl_user WHERE user_email=%s"""
			data = (_email)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sql, data)
			rv = cursor.fetchall()
			resp = jsonify('Login !')
			
			if rv:

				if check_password_hash(rv[1]["user_password"],_password):
					resp = jsonify('Login successful!')
					resp.status_code = 200
				else:
					resp = jsonify('Unauthorized Login')
					resp.status_code = 204
			else:
				resp = jsonify('Username does not exist')
				resp.status_code = 210
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
				
@app.route('/users')
@cross_origin()
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user where user_email=%s",('angelin@gmail.com',))
		rows = cursor.fetchall()

		resp = jsonify(rows)
		print(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/user/<id>')
def user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['POST'])
def update_user():
	try:
		_json = request.json
		_id = _json['id']
		_name = _json['name']
		_email = _json['email']
		_password = _json['pwd']		
		# validate the received values
		if _name and _email and _password and _id and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
			data = (_name, _email, _hashed_password, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
#All transaction related APIs will follow

#Add Transaction
@app.route('/<userid>/transaction', methods=['POST'])
@cross_origin()
def add_transaction(userid):
	try:
		_json = request.json
		_txnType = _json['txnType']
		_category = _json['category']
		_amt= _json['amt']
		_date=_json['date']

		if _txnType and _category and _date and request.method == 'POST':
			if not _amt:
				_amt=0.00
			
			# Query to add transaction
			sql = "INSERT INTO tbl_transaction(user_id, txntype, category,amt,date) VALUES(%s, %s, %s,%s,%s)"
			data = (userid,_txnType,_category,_amt,_date)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			print("Last inserted record has id ", cursor.lastrowid())
			resp = jsonify('Transaction added successfully!')
			resp.status_code = 200
			return resp
			#return get_transaction(userid,cursor.lastrowid())
		else:
			return not_found()
	except Exception as e:
		print(e)

# Get Transaction
@app.route('/<userid>/transaction/<txnId>', methods=['GET'])
@cross_origin()
def get_transaction(userid,txnId):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s AND txn_id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Update transaction
@app.route('/<userid>/transaction/<txnId>', methods=['PUT'])
@cross_origin()
def update_txn(userid,txnId):
	try:
		_json = request.json
		_txnType = _json['txnType']
		_category = _json['category']
		_amt= _json['amt']
		_date=_json['date']	
		# validate the received values
		if userid and txnId and _txnType and _category and _date and request.method == 'PUT':
			
			sql = "UPDATE tbl_transaction SET txntype=%s, category=%s, amt=%s,date=%s WHERE user_id=%s and txn_id=%s"
			data = (_txnType,_category,_amt,_date,userid,txnId)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Transaction updated successfully!')
			resp.status_code = 200
			return resp
			#return get_transaction(userid,txnId)
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Delete Transaction
@app.route('/<userid>/transaction/<txnId>',methods=['DELETE'])
def delete_txn(userid,txnId):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		data=(userid,txnId)
		cursor.execute("DELETE FROM tbl_transaction WHERE user_id=%s AND txn_id=%s",data)
		conn.commit()
		resp = jsonify('Transaction deleted successfully!')
		resp.status_code = 204
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
#Fetch All Transactions
@app.route('<userid>/transactions')
@cross_origin()
def transactions(userid):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_transaction where user_id=%s",(userid))
		rows = cursor.fetchall()

		resp = jsonify(rows)
		print(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()	

		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run()