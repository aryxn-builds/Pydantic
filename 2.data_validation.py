from pydantic import BaseModel , EmailStr , Field , AnyUrl
from typing import Optional , List ,Dict ,Annotated

class Patient(BaseModel):
    
    name : Annotated[str, Field(max_length=50 , title="Name of the patient" , description="The name of the patient", json_schema_extra={"example": "John Doe"})]  # This is used for setting validation for name field to have maximum length of 50 and title as "Name of the patient"
    
    email : EmailStr
    linkedin_url : AnyUrl
    
    age : int = Field(gt=0,lt=200)  # This is used for setting validation for age field to be greater than 0 and less than 200
    
    weight : Annotated[float , Field(gt=0, strict= True )]  # This is used for setting validation for weight field to be greater than 0 and strict mode is enabled to ensure that the value is of type float
    
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
