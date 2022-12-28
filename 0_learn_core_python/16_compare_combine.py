#compare lists
list_1 = [1,2,3,4]
list_2 = [2,1,4,2]
list_3 = [1,2,3,4]

print(list_1 == list_2)             #output - False
print(list_1 == list_3)             #output - True

#compare dictionaries
dict_1 = {1:5,2:6,3:7,4:8}
dict_2 = {4:8,2:6,3:7,1:5}

print(dict_1 == dict_2)             #output - False

#list of lists
cList = [['egg','hash brown','milk'],['roti','sabji','salad'],['biryani','lassi','papad']]
print('Breakfast',cList[0])
print('Lunch',cList[1])
print('Dinner',cList[2])

#distionary of lists
dDict = {'Breakfast':['egg','hash brown','milk'], 'Lunch':['roti','sabji','salad'], 'Dinner':['biryani','lassi','papad']}
print('Breakfast',dDict['Breakfast'])
print('Lunch',dDict['Lunch'])
print('Dinner',dDict['Dinner'])
