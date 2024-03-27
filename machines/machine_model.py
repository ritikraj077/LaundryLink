from pydantic import BaseModel



class add(BaseModel):
   location: str
   type: str
   status: str 

class machine_dtl(BaseModel):
   location: str
   type: str
   
class remove_machine(BaseModel):
   id: int
   status: str