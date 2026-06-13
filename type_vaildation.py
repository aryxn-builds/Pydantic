from pydantic import BaseModel
from typing import Optional , List ,Dict

class Patient(BaseModel):
    
    name : str 
    age : int
    weight : float
    married : bool = False  # This is used for setting default value for married field
    allergies : Optional[List[str]] = None  # This is used for setting default value for allergies field but its value can be empty list or None
    contact_details : Dict[str, str] = {} 

def update_patient_data(patient: Patient ):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("updated patient data successfully")
    
Patient_info = {
    "name" : "John Doe",
    "age" : 30,
    "weight" : 70.5,
    "married" : True,
    "allergies" : ["Peanuts", "Shellfish"],
    "contact_details" : {"email" : "john.doe@example.com", "phone" : "123-456-7890"}
}

patient = Patient(**Patient_info)
update_patient_data(patient)