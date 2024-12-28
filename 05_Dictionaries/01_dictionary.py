# Dictionaries is a collection of a key-value pairs

a={
    "key":"value",
    "soham":"code",
    "marks":"100",
    "list":[1,2,3,4]
    
}

print(a["key"])
print(a["list"])


########################  properties #########################

# it is unordered
#it is mutable
# it is indexed
# cannot contain duplicate values




########################################dictionary methods #######################################

#print(a.items())  # return a list of (key,value) tuples

#print(a.keys())  # return  a list containing dictionary only keys

a.update({"colour":"white"})  # update by inserting the new key value pair or item
#print(a.items())


#print(a.get("soham"))   # return the value of the specified keys

#print(a.values())      # return the list of the only the values 

#a.pop("soham")         # delete the key value from the dictionary
#print(a.items())


#a.popitem();              # delete last item from the key-value pair
#print(a.items())

#a.clear();     # clear all the key-value pairs
#print(a.items())