from pydantic import BaseModel

class Registration(BaseModel):
    username: str
    email: str  # Corrected type from int to str
    password_hash: str  # Corrected type from ptr to str
   
       
       
##oject for login   
class LoginModel(BaseModel):
    ##taking input from the use and validating using base model
    username : str
    password_hash : str
    

  ##object to delete user  
      ##taking input from the use and validating using base model
class Delete_user(BaseModel):
    username : str
    
    
    
##object to forgrt pass   
##taking input from the use and validating using base model

class Forget(BaseModel):
    username : str
    password_hash : str
    
    
    
    