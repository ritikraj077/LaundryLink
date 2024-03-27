from flask import Flask,request,jsonify,session,redirect, Blueprint
from machines import machine_model as user_models
from machines.machines_services import add_machine_db, search_machine,remove_machine_db





machine_app = Blueprint('machine_app', __name__)


@machine_app.route("/add_machine", methods=["POST"])
def add_machine():
    data = request.json
    
    try:
        cred = user_models.add(**data)
    except Exception as e:
        return jsonify({'massage':"Data input is not of correct datatype plezz enter the data in correct datatype"})

    result = add_machine_db(cred)
    return result 




@machine_app.route("/search_machine", methods = ["POST"])
def machine_details():
    data = request.json
    try:
        cred = user_models.machine_dtl(**data)
    except Exception as e :
        return jsonify({'massage':"Data input is not of correct datatype plezz enter the data in correct datatype"})

    result = search_machine(cred)
    return result




@machine_app.route("/remove_machine",methods = ["DELETE"]) 
def remove_machine():
    data = request.json
    try:
        cred = user_models.remove_machine(**data)
    except Exception as e :
        jsonify({"massage":  "data input is not of correct datatype plezz enter the datatype in correct datatype"})
        
    result = remove_machine_db(cred)
    return result