from flask import Flask,request,jsonify,session,redirect, Blueprint
from cleaning_and_ironing.cln_services import calculate_cleaning_rate, cleaning_and_iron_rates
from authenticaton.authrntication_jwt import check_bearer_token
SECRET_KEY= 'Secret_key1234'




cln_ion  = Blueprint('cln_ion', __name__)

@cln_ion.route("/clean" , methods= ["GET"])
def cleaning():
    cheak = check_bearer_token(request, SECRET_KEY)
    print(cheak)
   
    if 'error' in cheak and 'Bearer token has expired' in cheak['error']:
        error_message = cheak['error']
        
        return jsonify ({"Error": error_message})
    else:
        username = cheak['Username']
        print(username )
       
    data = request.json
    
    
    cleaning_rate = calculate_cleaning_rate(data, username)
    
    return jsonify({"Total price of washing clothes is Rs": cleaning_rate})



@cln_ion.route("/cleaning_rates" , methods= ["GET"])
def cleaning_rates():
    
    rates = cleaning_and_iron_rates()
    return rates




