from pydantic import BaseModel

class Registration(BaseModel):
    username: str
    email: str  # Corrected type from int to str
    password_hash: str  # Corrected type from ptr to str
    role: str
       
       
       
       
class LoginModel(BaseModel):
    username : str
    password_hash : str
    

    
class Delete_user(BaseModel):
    username : str
    
    
    
    
class Forget(BaseModel):
    username : str
    password_hash : str
    
    
    
    