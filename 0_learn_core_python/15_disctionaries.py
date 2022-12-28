#Dictionaries are also know as map in java
#Dictionary can contain lists or dictionaries

my_dist = {1:"K Kumar", 'address':'UK', 'door':13, 'book':'cookbook'}
print(my_dist)

#An empty dictionary
eDist = {}

#Add an item to dictionary
eDist['first name'] = 'kishor'
eDist['last name'] = 'kumar'
eDist['contact'] = 7777777777
eDist['info'] = 'No match fund'
print(eDist)

#Update value in a dictionary
eDist['contact'] = 9876543210
print(eDist)

#Delete from an dictionary
del eDist['info']
print(eDist)

#get an item from dictionary - 1. using key, but will error if key not found
result = eDist['contact']
print(result)

#result = eDist['nonkey']        #KeyError:

#get an item from dictionary - 2. using get method, but will return boolean 'None' if key not found
result = eDist.get('first name')
print(result)

result = eDist.get('forename name')
print(result)                       #output - None

if result:
    print(result)
else:
    print("not found !")