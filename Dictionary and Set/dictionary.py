# dictionary are used to store data values in key:value pairs, they are unordered, mutable(changeable) & don't allow dupliacte keys 

info = {
    "key" : "value",
    "name" : "ankur yadav",
    "learning" : "python"
}
print(info) #output = {'key': 'value', 'name': 'ankur yadav', 'learning': 'python'}

# if we change the value
info = {
    "name" : "monu",
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict", "set"),
    "age" : 35,
    "is_adult" : True,
    12.99 : 94.4
}

info["name"] = "ankur"  #overwrite
info["surname"] = "yadav"
print(info) #output = {'name': 'ankur', 'subjects': ['python', 'C', 'Java'], 'topics': ('dict', 'set'), 'age': 35, 'is_adult': True, 12.99: 94.4, 'surname': 'yadav'}

# Empty dictionary
null_dict = {}
null_dict["name"] = "ankur yadav"
print(null_dict) #output = {}, {'name': 'ankur yadav'}


# nested dictionary
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student) #output = {'name': 'rahul kumar', 'subjects': {'phy': 97, 'chem': 98, 'math': 95}}