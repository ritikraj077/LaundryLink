from  database.database_db import BaseModel, Session
import sqlalchemy
from sqlalchemy import Column, String, Integer, Enum,Delete , ForeignKey
from flask import Flask , jsonify

session = Session()
class ClothesData(BaseModel):
    __tablename__ = 'clothes_data'
    __table_args__ = {'extend_existing': True}  # Add this line that if the table is already created than this will not create an another table or will not raise an error 


    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    shirt = Column(Integer)
    pant = Column(Integer)
    dress = Column(Integer)
    iron = Column(Integer)
    charges = Column(Integer)


    def __repr__(self):
            return '<ClothesData %r>' % self.username

def calculate_cleaning_rate(data ,username):
    if 'shirt' in data:
        shirt = data['shirt']
    else: 
        shirt = 0
    
    if 'pants' in data:
        pants = data['pants']
    else:
        pants = 0
    
    if 'dress' in data:
        dress = data['dress']
    else:
        dress = 0
    
    if 'iron' in data:
        iron = data["iron"]
    else:
        iron = 0

    Rate_of_shirts = shirt * 10
    Rate_of_pants = pants * 15
    Rate_of_dress = dress * 20
    Rate_of_iron = iron * 15

    Total_price = Rate_of_shirts + Rate_of_pants + Rate_of_dress
    clothesdata_to_db(shirt, pants, dress, iron , username, Total_price)
    
    return Total_price

def clothesdata_to_db(shirt, pants, dress, iron, username ,Total_price):
    
    new_booking = ClothesData(
    username = username,
    shirt = shirt,
    pant = pants,
    dress = dress,
    iron = iron,
    charges= Total_price)

    session.add(new_booking)
    session.commit()



def cleaning_and_iron_rates():
    rates = {
        'shirt': '10rs per shirt',
        'pants': '15rs per pant',
        'dress': '20rs per dress',
        'iron': '15rs per cloth'
    }
    return jsonify(rates)