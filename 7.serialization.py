# used to export the data of a model to a different format like json, dict, etc. It is used to export the data of a model to a different format like json, dict, etc.

from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)

temp = patient1.model_dump(exclude_unset=True) # for dictionary format
print(temp)
print(type(temp))


# temp1 = patient1.model_dump_json(exclude_unset=True)

# print(temp1)
# print(type(temp1))