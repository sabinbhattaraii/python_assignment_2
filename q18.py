'''
Find a package in the Python standard library for dealing with JSON.
Import the library module and inspect the attributes of the module.
Use the help function to learn more about how to use the module.
Serialize a dictionary mapping 'name' to your name and 'age' to your
age, to a JSON string. Deserialize the JSON back into Python
'''


import json

data = {
    "First_name":"Sabin",
    "Last_name":"Bhattarai",
    "age":25
}

with open("info.json","w") as write:
    json.dump(data,write)

with open("info.json","r") as read:
    print(json.load(read))