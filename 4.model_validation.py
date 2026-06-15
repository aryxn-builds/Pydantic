from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    
    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if  model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60")
        return model
    
    
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
    "age" : 70,
    "weight" : 70.5,
    "married" : True,
    "allergies" : ["Peanuts", "Shellfish"],
    "contact_details" : {"email" : "john.doe@example.com", "phone" : "123-456-7890", "emergency" : "987-654-3210"}
}

patient = Patient(**Patient_info)
update_patient_data(patient)