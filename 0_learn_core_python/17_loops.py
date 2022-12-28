#loops (for & while) and range, loops length, format

#loop Number list and get average
nList = [12,15,1.09,100,70000000000000000]
print(nList)

sum = 0
for i in nList:
    print('value is',i)
    sum = sum + i
    print('sum', sum)

#get length of list
lenList = len(nList)
print(lenList)

avg = sum / lenList
print('Average:',avg)

print('formatted Average:',format(avg,'.2f'))

#loop through n mumber
n = 13
for number in range(n):     # 0 to n-1
    print(number)

#loop through a range after some interval
min = 100
max = 200
interval = 3
for number in range(min, max, interval):     # 0 to n-1
    print(format(number,'.2f'))           # format to 2 place after decomal



