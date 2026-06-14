from pydantic import BaseModel , EmailStr , AnyUrl
from typing import Optional , List ,Dict

class Patient(BaseModel):
    
    name : str
    email : EmailStr
    linkedin_url : AnyUrl
    
    age : int
    
    weight : float
    
    married : bool = False 
    
    allergies : Optional[List[str]] = None  
    
    contact_details : Dict[str, str] 

def update_patient_data(patient: Patient ):
    
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("updated patient data successfully")
    
Patient_info = {
    "name" : "John Doe",
    "email" : "john.doe@example.com",
    "linkedin_url" : "https://www.linkedin.com/in/johndoe",
    "age" : 30,
    "weight" : 70.5,
    "married" : True,
    "allergies" : ["Peanuts", "Shellfish"],
    "contact_details" : {"email" : "john.doe@example.com", "phone" : "123-456-7890"}
}

patient = Patient(**Patient_info)
update_patient_data(patient)
