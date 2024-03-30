from  database.database_db import BaseModel, Session
import sqlalchemy
from sqlalchemy import Column, String, Integer, Enum,Delete
from flask import jsonify
import bcrypt
import datetime
from sqlalchemy.orm.exc import NoResultFound

import jwt
session = Session()
SECRET_KEY= 'Secret_key1234'

def api_response(message,data, status_code):
     return jsonify({"message":message, "data":data, "status_code":status_code}), status_code
    

class User(BaseModel):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}  # Add this line that if the table is already created than this will not create an another table or will not raise an error 
    
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum('student', 'staff', 'admin'), nullable=False)
    

    
    def __repr__(self):
        return '<User %r>' % self.username
    


def sign_up_db(user_data): 
    try:
        salt = bcrypt.gensalt()
        hashed_password =  bcrypt.hashpw(user_data.password_hash.encode('utf-8'), salt) ##encrypting the password
        print(hashed_password)
        
        new_user = User(
            username= user_data.username,
            email=user_data.email,
            password_hash=hashed_password,  # Make sure to hash passwords securely
            role=user_data.role  # Assuming 'student' is a valid role
        )

        session = Session()
        session.add(new_user)
        session.commit()
        message = f"{new_user.username} registered successfully!"
        user_resp = {"username":new_user.username, "email":new_user.email}
        return api_response(message, user_resp, 201)

    except sqlalchemy.exc.IntegrityError:
        session.rollback()
        print(f"Error occurred dublicate keys")
        message= "Already signup or dublicate entry"
        return api_response(message, None , 409)
    
    except Exception as e:
        session.rollback()
        print(e)
        return api_response("Internal Server Error", None , 500)
    
    finally:
        session.close()



def login_db(user_data):
    #create session 
    
    session = Session()
    
    try:
        #query to filter one row based on the username 
        user = session.query(User).filter(User.username == user_data.username).one()
    except NoResultFound:
        return api_response(message="User not found!",data={"username": None}, status_code=404)
    ##password enterd by the user converted to pybits 
    
    user_entered_password = user_data.password_hash.encode('utf-8')
    ##password fetched from the database
    stored_password = user.password_hash.encode('utf-8')
    #check function which checks and compare the password that they are same or not 
    
    if bcrypt.checkpw(user_entered_password, stored_password):
        token = generate_jwt_token(user_data.username, SECRET_KEY)
        return api_response(message="Logged In successfully!", data={"id": user.id,"username": user.username, "token": token}, status_code=200)
    else:
        return api_response(message="Unauthorized Access!", data=user, status_code=401)
    
      
    

def generate_jwt_token(username_t,SECRET_KEY): 
    
        # Generate JWT token with user's username and expiration time
        
        token_payload = {
            'Username': username_t,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)  # Token expiration time
        }
        token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')
    
        return token

def delete_user_db(delete_cred):
    session = Session()
    try:
        user_to_delete = session.query(User).filter_by(username=delete_cred.username).one()

        #delete_user = session.delete(User).where(User.username== data.username)
        session.delete(user_to_delete)
        ##commit chnages to database 
        
        session.commit()
        return jsonify({'success': 'User deleted successfully'})
    except Exception as e :
         session.rollback()
         return jsonify({'error':e})
    finally:
        session.close()
        from sqlalchemy.exc import SQLAlchemyError


def forget_password_db(cred):
    try:
        # Query the user whose password you want to change
        try:
            password_change = session.query(User).filter(User.username == cred.username).one()
        except NoResultFound:
            return jsonify({'error': "User not found!"}), 404

        # Update the password hash with the new password
        password_change.password_hash = cred.password_hash

        # Commit the changes to the database
        session.commit()

        return jsonify({'success': 'Password updated successfully'})
    except Exception as e:
        # Rollback the session in case of error
        session.rollback()
        return jsonify({'error': str(e)})



def userid_from_username(username):
    try:
        user = session.query(User).filter(User.username == username).one()
    except NoResultFound:
        return jsonify({'error': "User not found!"}), 404
    
    user_id = user.id
    return user_id