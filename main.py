import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import Flask, request
from flask_cors import CORS, cross_origin
from werkzeug import generate_password_hash, check_password_hash
import simplejson as json
import numpy as np
from datetime import datetime
import pickle
#import model

cors = CORS(app)
app = Flask(__name__)
#model = pickle.load(open('model.pkl','rb'))
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
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sql, data)
			conn.commit()
			sql = """SELECT * FROM tbl_user WHERE user_email=%s"""
			data=_email
			cursor.execute(sql, data)
			rv = cursor.fetchall()
			print(rv)
			print(rv[0])
			resp = jsonify({'userId':rv[0]["user_id"]})
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)

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
			print(_email)
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = """SELECT * FROM tbl_user WHERE user_email=%s"""
			data = (_email)
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sql, data)
			rv = cursor.fetchall()
			print(rv)
			print(rv[0])
			# print(rv[1])
			# print(rv[0]["user_id"])
			resp = jsonify('Login !')
			
			if rv:

				if check_password_hash(rv[0]["user_password"],_password):
					resp = jsonify({'userId':rv[0]["user_id"]})
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
		print("hit the method")
		_json = request.json
		_txnType = _json['txntype']
		_category = _json['category']
		_amt= _json['amt']
		_date= datetime.date(datetime.now())
		print(_date)
		_qty=_json['qty']

        
		
		if _txnType and _category and _date and request.method == 'POST':
			if not _amt:
				_amt=0.00
			print("Reached query")
			# Query to add transaction
			sql = "INSERT INTO tbl_transaction(user_id, txntype, category,amt,date,qty) VALUES(%s, %s, %s,%s,%s,%s)"
			data = (userid,_txnType,_category,_amt,_date,_qty)
			conn = mysql.connect()
			cursor = conn.cursor()
			print(cursor.execute(sql, data))
			conn.commit()
			print("Last inserted record has id ",cursor.lastrowid)
			return transactions(userid)
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
		print(userid)
		print(txnId)
		cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s AND txn_id=%s", (userid,txnId))
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
		_qty=_json['qty']
		# validate the received values
		if userid and txnId and _txnType and _category and _date and request.method == 'PUT':
			
			sql = "UPDATE tbl_transaction SET txntype=%s, category=%s, amt=%s,date=%s,qty=%s WHERE user_id=%s and txn_id=%s"
			data = (_txnType,_category,_amt,_date,_qty,userid,txnId)
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
@app.route('/<userid>/transactions')
@cross_origin()
def transactions(userid):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_transaction where user_id=%s",(userid))
		rows = cursor.fetchall()

		resp = json.dumps(rows)
		print(rows)
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()	
#Calculate Tax
@app.route('/<userid>/tax', methods=['GET'])
@cross_origin()
def get_tax(userid):
	a=10
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		print(userid)
		cursor.execute("SELECT txntype,sum(amt) as sum FROM test.tbl_transaction  where user_id=%s group by txntype;", userid)
		row = cursor.fetchall()
		print("tax output")
		#txntype -1 Expense
		#txntype -0 Income
		income=expense=0
		if row[0]["txntype"] == 0:
		   income=row[0]["sum"]
		else :
		   expense=row[0]["sum"]
		if row[1]["txntype"] == 0:
		   income=row[1]["sum"]
		else :
		   expense=row[1]["sum"]
		cursor.execute("SELECT tax_limit,tax_percentage FROM tbl_statetax s join tbl_user u on s.state_id=u.state where u.user_id=%s;",userid)
		row=cursor.fetchall()
		tax_limit=row[0]["tax_limit"]
		tax_percent=row[0]["tax_percentage"]
		tax_payable=calc_tax(income,expense,tax_limit,tax_percent)
		print("tax payable")
		print(tax_payable)
		resp = jsonify({"tax":tax_payable})
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

def calc_tax(income,expense,tax_limit,tax_percent):
	profit = income-expense
	tax = 0
	if profit > tax_limit:
		tax=tax_percent/100*profit
	return tax
	
	   
# Get
@app.route('/<userid>/predict', methods=['GET'])
@cross_origin()
def predict_tax(userid):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		# Make prediction using model loaded from disk as per the data.
		print("Reached near prediction")
		prediction = model.predict([[1.8]])
        # Take the first value of prediction
        
		output = prediction[0]
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
    app.run(port=5000,debug=True)