# myDict.keys() returns all keys
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student.keys()) #output = dict_keys(['name', 'subjects'])



# myDict.values() returns all values
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student.values()) #output = dict_values(['rahul kumar', {'phy': 97, 'chem': 98, 'math': 95}])




# myDict.items() returns all(key,val) pairs as tuples
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student.items()) #output = dict_items([('name', 'rahul kumar'), ('subjects', {'phy': 97, 'chem': 98, 'math': 95})])



# myDict("key") returns the key according to value
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

# print(student["name2"]) # error
print(student.get("name2")) # no error




# myDict.update(newDict) insert the specified items to the dictionary
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
new_dict = {"name" : "neha kumar", "age": 16}
student.update(new_dict)
print(student) #output = {'name': 'neha kumar', 'subjects': {'phy': 97, 'chem': 98, 'math': 95}, 'age': 16}