from datetime import date
from datetime import datetime
from datetime import timedelta
import time

def Get_CurrentTimeStamp_int():
    timestamp_ns = time.time_ns();
    print('Current time stamp in nanoseconds is:', timestamp_ns)
    return timestamp_ns

def Get_CurrentDate_date():
    date_dt = date.today();
    print('Current date is:', date_dt)
    return date_dt

def Get_Formatted_CurrentDateTime_str(format):
    dt = datetime.now().strftime(format)
    return dt

def Convert_Timestamp_to_Formatted_Datetime_str(timestamp,format):
    #timestamp - nanoseconds
    dt = datetime.fromtimestamp(timestamp / 1000000000 )
    dt_formatted = dt.strftime(format)
    return dt_formatted

def Convert_Formatted_Datetime_to_Timestamp_timestamp(formatted_datetime, format):
    dt = datetime.strptime(formatted_datetime,format)
    return dt

def Convert_Datetime_to_Formatted_str(dt,format):
    dt_str = dt.strftime(format)
    return dt_str

def Convert_Formatted_Datetime_to_Timestamp_int(formatted_datetime, format):
    dt = datetime.strptime(formatted_datetime,format)
    timestamp_ns = round(dt.timestamp() * 1000000000)
    return timestamp_ns

def Get_Elapsed_NanoSec_Time_int(StartTime, EndTime, format):
        start_ts_ns = Convert_Formatted_Datetime_to_Timestamp_int(StartTime,format)
        end_ts_ns = Convert_Formatted_Datetime_to_Timestamp_int(EndTime,format)
        et_ns = end_ts_ns - start_ts_ns
        return et_ns
   


def main():
    # Get_CurrentTimeStamp_int
    curr_ts_ns = Get_CurrentTimeStamp_int()

    # Get_CurrentDate_date
    curr_date = Get_CurrentDate_date()

    # Get_Formatted_CurrentDateTime_str
    format = '%d-%b-%y %H:%M:%S.%f'
    curr_datetime = Get_Formatted_CurrentDateTime_str(format)
    print('Current formatted Datetime is:', curr_datetime)

    # convert timestamp nanpseconds to datetime formatted string
    dt_formatted = Convert_Timestamp_to_Formatted_Datetime_str(curr_ts_ns,format)
    print("Timestamp to formatted datetime with ms is:", dt_formatted)

    # convert string to datetime
    dt = Convert_Formatted_Datetime_to_Timestamp_timestamp(dt_formatted,format)
    print("Formatted datetime to datetime: =", dt)

    # Convert date time to formatted string
    dt_str = Convert_Datetime_to_Formatted_str(dt,format)
    print('Datetime to formatted string', dt_str)

    # convert string to time nano seconds
    ts_ns = Convert_Formatted_Datetime_to_Timestamp_int(dt_formatted,format)
    print("Formatted datetime to timestamp(in ns) is", ts_ns)

    # convert timestamp nanpseconds to datetime formatted string again
    dt_formatted = Convert_Timestamp_to_Formatted_Datetime_str(ts_ns,format)
    print("Timestamp to formatted datetime with ms is:", dt_formatted)

    # Get elapsed time in nano seconds between two times
    print('Elapsed time in int:', Get_Elapsed_NanoSec_Time_int('01-Dec-22 08:00:00.000000', '01-Dec-22 23:00:00.000000', format))
    

#main()

