from flask import Flask, Blueprint,request,jsonify
from booking import booking_module as user_models
from booking.booking_service import book_machine_db
from authenticaton.authrntication_jwt import check_bearer_token
SECRET_KEY= 'Secret_key1234'





booking_app = Blueprint('booking_app',__name__)



@booking_app.route("/book_machine",methods = ["POST"])
def book_machine():
    cheak = check_bearer_token(request, SECRET_KEY)
   
    if 'error' in cheak and 'Bearer token has expired' in cheak['error']:
        error_message = cheak['error']
        
        return jsonify ({"Error": error_message})
    else:
    # Proceed with the decoded token or user information
    
        # Return a proper error response
       
        
        username = cheak["Username"]
        print(username)
    data = request.json
    print(data)
    try:
        cred = user_models.book_machine(**data)
        print(cred)
    except Exception as e :
        return jsonify({'massage':"Data input is not of correct datatype plezz enter the data in correct datatype"})
    result = book_machine_db(cred,username)
    return result 


