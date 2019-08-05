#Create DICTIONARIES
dict1={
    "name":"vasu",
    "age":5,
    "year":2018
    }
dict2={
    "name":"naddy",
    "age":5
    }
#Add a key to dictionary
dict1.update({"area":"chennai"})
print(dict1)
#Concatenate to create a new dictionary
dict3={}
for d in (dict1,dict2):dict3.update(d)
print(dict3)
#Iterate through for loops
d1={
    "red":100,
    "yellow":200
    }
d2={
    "black":300,
    "white":400
    }
for colors,values in d1.items():
    print(colors,"corresponds to",d1[colors])
#Merge two dictionaries
d=d1.copy()
d.update(d2)
print(d)
#Sum all the items in a dictionary
print(sum(d1.values()))
#Remove a key from a dictionary
del dict1["year"]
print(dict1)
#Check a dictionary is empty or not
dct={}
if not dct:
    print("Empty dictionary")
#Combine 2 dictionary adding values for common keys
from collections import Counter 
dict4 = {'a': 12, 'for': 25, 'c': 9} 
dict5 = {'Geeks': 100, 'geek': 200, 'for': 300} 
Cdict = Counter(dict4) + Counter(dict5) 
print(Cdict)
#Get the key,values and items in a dictionary
print(dict4.items()) #prints keys and values
print(dict4.keys()) #prints keys
print(dict4.values()) #prints values
    

    


