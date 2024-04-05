from flask import Flask,request,jsonify,session,redirect, Blueprint
from user import user_model as user_models
from user.user_services import sign_up_db, login_db,delete_user_db,forget_password_db



user_app = Blueprint('user_app', __name__)


##api to sing up user to make new rgistration 
@user_app.route("/sign_up", methods=["POST"])
def sign_up():
    data = request.json
    try:
        user_model = user_models.Registration(**data)
    except Exception as e :
        return jsonify({'massage':"Data input is not of correct datatype plezz enter the data in correct datatype"})
    print(user_model)
    
    singup = sign_up_db(user_model)  
    return singup

  
  
 ##api to login user  
@user_app.route("/login", methods=["POST"])
def login():
    
    data = request.json
    try:
        login_cred = user_models.LoginModel(**data)
    except Exception as e :
        return jsonify({'massage':"Data input is not of correct datatype plezz enter the data in correct datatype"})
    user_login_resp = login_db(login_cred)
    return user_login_resp
        
    
   
 ##api to logout user  
@user_app.route("/logout",methods = ["POST"])
def Logout_user():

    session.pop('username',None)
    return redirect("url_for('index')") 



#api to delete the user details from the database     
@user_app.route("/delete_user",methods = ["POST"])
def delete_user():
    data = request.json
    delete_cred = user_models.Delete_user(**data)
    delete_user_db(delete_cred)
    return jsonify({'success': 'User deleted successfully'})  



    


##api to reset password using forget password 
@user_app.route("/Forget_pass",methods = ["POST"])
def forget_password():
    data = request.json
    try:
        cred = user_models.Forget(**data)
    except Exception as e:
        return jsonify({'massage':"Data input is not of correct datatype plezz enter the data in correct datatype"})

    result = forget_password_db(cred)
    return result


