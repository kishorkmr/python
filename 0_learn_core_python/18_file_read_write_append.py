# w - write to file (override)
# r - read file
# a - append file

#fileDataRead = open("c:\\Users\\Kishor Kumar\\Kishor_Learning\\python\\0_learn_core_python\\pip.info",'r')

fileDataWrite = open("write.info",'w')
fileDataWrite.write("line1\n")
fileDataWrite.write("line 2")
fileDataWrite.write("line 3")
fileDataWrite.close()

fileDataAppend = open("write.info",'a')
fileDataAppend.write('\nline 4')
fileDataAppend.write('\nline 5')
fileDataAppend.close()

fileDataRead = open("pip.info",'r')
print(fileDataRead.read())          #print all files contents as single string
fileDataRead.close()

fileDataRead = open("write.info",'r')
print('Line1: ', fileDataRead.readline())          #print line 1
print('Line2: ', fileDataRead.readline())          #print line 2
fileDataRead.close()

#Read line by line
fileDataRead = open("write.info",'r')

for line in fileDataRead:
    print(line)
fileDataRead.close()


