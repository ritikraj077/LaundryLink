from  database.database_db import BaseModel, Session
import sqlalchemy
from sqlalchemy import Column, String, Integer, Enum,Delete
from flask import jsonify
from user.user_services import api_response
from sqlalchemy.orm.exc import NoResultFound


session = Session()
class Machine(BaseModel):
    __tablename__ = 'machine'
    __table_args__ = {'extend_existing': True}  # Add this line that if the table is already created than this will not create an another table or will not raise an error 

    id =  Column(Integer, primary_key=True, autoincrement=True)
    location =   Column(String(255), nullable=False)
    type =   Column(Enum('washer', 'dryer'), nullable=False)
    status =   Column(Enum('available', 'out_of_order'), nullable=False, default='available')
    def __repr__(self):
        return '<Machine %r>' % self.name
    
    
    
    
def add_machine_db(cred):
    try:
        new_machine = Machine(
                location = cred.location,
                type = cred.type, 
                status = cred.status
        )
        session.add(new_machine)
        session.commit()
        return jsonify({"message": "New machine added sucessfully"}), 200
    except Exception as e:
       
        
        print(f"An error occurred while adding a new machine: {e}")

        print("error:",e)
        session.rollback()
        return api_response("Internal Server Error", None , 500)
    
    finally:
        session.close()
    
    
    
    
def search_machine(cred):
    # try:
    machines = session.query(Machine).filter(Machine.location == cred.location,Machine.type == cred.type).all()
        
    # except NoResultFound:
    #     return api_response(message="User not found!",data= None, status_code=404)
    
    if not machines:
            return api_response(message="Machines not found!", data=None, status_code=404)
        
    machine_data = []
    for machine in machines:
        machine_info = {
            "location": machine.location,
            "type": machine.type,
            "status": machine.status
        }
        machine_data.append(machine_info)
    
    return jsonify(machine_data)


def machine_id(cred):
        machines = session.query(Machine).filter(Machine.location == cred.location,Machine.type == cred.type).one()
        if not machines:
            return api_response(message="Machines not found!", data=None, status_code=404)
        
        




# 

def remove_machine_db(cred):
    try:
        if cred.status not in ["available", "out_of_order"]:
            return jsonify({"message": "Enter a valid entry in the status section."})
        

        else:
            delete_count = session.query(Machine).filter(Machine.id == cred.id, Machine.status == cred.status).delete()
            session.commit()
            
            #if the delete count result zero the this massage will be displayed
            if delete_count == 0:
                return jsonify({"message": "Machine not found."}), 404
            response = jsonify({"message": "Machine removed successfully"})
            return response, 200
    except Exception as e:
        session.rollback()
        response = jsonify({"message": "Internal server error"})
        return response, 500
    finally:
        session.close()

        
