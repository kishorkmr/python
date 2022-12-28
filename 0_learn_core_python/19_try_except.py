try:
    fileDataRead = open("write.info",'r')
    print(fileDataRead.read())
except:
    print("File doesn't exist")

#Exceptions
#FileNotFoundError
#IndexError
#KeyError
#NameError
#ValueError

try:
    array = [0,1,2]
    print(array[3])
except IndexError as err:
    print('Index Error!')
    print(err)