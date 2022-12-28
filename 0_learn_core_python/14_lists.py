#lists are also know as array in java
#list can contain any data type or mis of data type

#An empty list
eList = []
print(eList)

#Number list
nList = [12,15,1.09,100,70000000000000000]
print(nList)

#Sring list
sList = ["cat", 'dog', "bull", "cow", "ant"]
print(sList)

#Mixed list
mList = [1,"asda", 'b', 1.11, 100000.98]
print(mList)

#getting from a list
#1 - get for an index
print(nList[0])

#2 - slice a list
print(sList[2:5])

#Adding to a list
eList.append("My")
eList.append("name is")
eList.append("Name")
print(eList)

#Remove item from list - 1. using value
eList.remove("Name")
print(eList)
eList.append("KK")
print(eList)
#Remove item from list - 2. using index
del eList[2]
print(eList)
eList.append("Kishor")
print(eList)

#Delete a slice of list
del eList[:2]       # it will delete from index 0 to 1
print(eList)

del nList[1:3]
print(nList)        # it will delete from index 1 to 2