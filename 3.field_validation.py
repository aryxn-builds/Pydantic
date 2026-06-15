# Field validation is used to data validation in a single field of a model or It is used to validate the data of a single field in a model.

from pydantic import BaseModel , EmailStr , Field , field_validator
from typing import Optional , List ,Dict

class Patient(BaseModel):
    
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool = False 
    allergies : Optional[List[str]] = None  
    contact_details : Dict[str, str] 
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        
        valid_domains =['hdfc.com','icici.com']
        
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError("Not valid domain ")
        
        return value
    
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    
    @field_validator('age')
    @classmethod
    def age_validator(cls, value):
        if value < 0 or value > 200:
            raise ValueError("Age must be between 0 and 200")
        return value

def update_patient_data(patient: Patient ):
    
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("updated patient data successfully")
    
Patient_info = {
    "name" : "John Doe",
    "email" : "john.doe@hdfc.com",
    "age" : 30,
    "weight" : 70.5,
    "married" : True,
    "allergies" : ["Peanuts", "Shellfish"],
    "contact_details" : {"email" : "john.doe@example.com", "phone" : "123-456-7890"}
}

patient = Patient(**Patient_info)
update_patient_data(patient)
