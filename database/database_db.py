
import pymysql
from sqlalchemy.orm import create_session, session, sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum, ForeignKey
 
 
    
database_url = 'mysql+pymysql://ritik:Ritik%401234@localhost/laundrylink'

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

BaseModel = declarative_base()

    
class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username =  Column(String(255), nullable=False, unique=True)
    email =  Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role =  Column(Enum('student', 'staff', 'admin'), nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username


# Define Machine model
class Machine(BaseModel):
    __tablename__ = 'machine'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    location =   Column(String(255), nullable=False)
    type =   Column(Enum('washer', 'dryer'), nullable=False)
    status =   Column(Enum('available', 'out_of_order'), nullable=False, default='available')
    def __repr__(self):
        return '<Machine %r>' % self.name

# Define Booking model
class Booking(BaseModel):
    __tablename__ = 'booking'
    id =   Column(Integer, primary_key=True, autoincrement=True)
    user_id =   Column(Integer,  ForeignKey('user Id'), nullable=False)
    machine_id =   Column(Integer, ForeignKey('machine Id'), nullable=False)
    start_time =   Column(DateTime, nullable=False)
    end_time =   Column(DateTime, nullable=False)
    status =   Column(Enum('pending', 'confirmed', 'cancelled'), nullable=False, default='pending')
    def __repr__(self):
        return '<Booking %r>' % self.id
