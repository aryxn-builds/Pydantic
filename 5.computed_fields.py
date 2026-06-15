from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)


def update_patient_data(patient: Patient ):
    
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(f"Patient's BMI: {patient.bmi}")
    print("updated patient data successfully")
    
Patient_info = {
    "name" : "John Doe",
    "email" : "john.doe@hdfc.com",
    "age" : 70,
    "weight" : 70.5,
    'height': 1.72,
    "married" : True,
    "allergies" : ["Peanuts", "Shellfish"],
    "contact_details" : {"email" : "john.doe@example.com", "phone" : "123-456-7890", "emergency" : "987-654-3210"}
}

patient = Patient(**Patient_info)
update_patient_data(patient)