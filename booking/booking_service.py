from  database.database_db import BaseModel, Session
import sqlalchemy
from sqlalchemy import Column, String, Integer, Enum,Delete,ForeignKey, DateTime
from flask import jsonify
from datetime import datetime, timedelta


from user.user_services import userid_from_username

SECRET_KEY= 'Secret_key1234'
from authenticaton.authrntication_jwt import check_bearer_token


session = Session()

class Booking(BaseModel):
    __tablename__ = 'booking'
    __table_args__ = {'extend_existing': True}  # Add this line that if the table is already created than this will not create an another table or will not raise an error 

    id =   Column(Integer, primary_key=True, autoincrement=True)
    user_id =   Column(Integer,  ForeignKey('user.id'), nullable=False)
    machine_id =   Column(Integer, ForeignKey('machine.id'), nullable=False)
    start_time =   Column(DateTime, nullable=False)
    end_time =   Column(DateTime, nullable=False)
    status =   Column(Enum('pending', 'confirmed', 'cancelled'), nullable=False, default='pending')
    def __repr__(self):
        return '<Booking %r>' % self.id








def book_machine_db(cred,username):
    try:
        user_id_u = userid_from_username(username)
        print(user_id_u)
        
        
        start_time = datetime.now()

    # Calculate the end time as half an hour after the start time
        end_time = start_time + timedelta(minutes=30)

    # Create the new booking with the calculated start and end times
        new_booking = Booking(
        user_id=user_id_u,  
        machine_id=cred.machine_id,  
        start_time=start_time,  
        end_time=end_time,
        status='pending')
        

        session.add(new_booking)

# Commit the transaction to save the changes to the database
        session.commit()
        
        added_booking = session.query(Booking).filter_by(id=new_booking.id).first()
        booking_dict = {
            'id': added_booking.id,
            'user_id': added_booking.user_id,
            'machine_id': added_booking.machine_id,
            'start_time': added_booking.start_time.isoformat(),  # Convert to ISO format for JSON serialization
            'end_time': added_booking.end_time.isoformat(),
            'status': added_booking.status
        }

        return jsonify({'success': 'Booking added successfully', 'booking': booking_dict})

        
        

    except Exception as e:
        session.rollback()
        return jsonify({'error': 'An error occurred - ' + str(e)})

    finally:
        session.close()

   