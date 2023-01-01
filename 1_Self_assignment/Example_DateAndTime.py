from datetime import date
from datetime import datetime
import time
from datetime import timedelta

today = date.today()
print("Today's date:", today)

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# dd-mmm-YY H:M:S.f
dt_string_with_ms = now.strftime("%d-%b-%y %H:%M:%S.%f")
print("date and time with ms =", dt_string_with_ms)

# current time in ns nanoseconds
time_nanoseconds = time.time_ns()
print('currenct ns:', time_nanoseconds)

# current time in ns milliseconds
print('currenct ms:', round(time.time()*1000))


#convert nanpseconds to datetime 1
dt = datetime.fromtimestamp(time_nanoseconds / 1000000000 )
dt_string_with_ms1 = dt.strftime("%d-%b-%y %H:%M:%S.%f")
print("date and time with ms1 =", dt_string_with_ms1)

#convert string to datetime
datetime1 = datetime.strptime(dt_string_with_ms1,"%d-%b-%y %H:%M:%S.%f")
print("string to datetime: =", datetime1)

#convert string to time
time1 = time.strptime(dt_string_with_ms1,"%d-%b-%y %H:%M:%S.%f")
print("string to datetime: =", time1)

# time to ns
print('Time to ns', time.time_ns())

# returns the elapsed milliseconds since the start of the program
start_time = datetime.now()
def millis():
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms

print('Delta ms:',millis())