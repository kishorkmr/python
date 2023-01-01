import WorkingDates, DateAndTime, CommonFunctions, input_output

def main():    

    # Global inputs
    #Enter dates in DD-MMM-YY format
    p_StartDate = input_output.IP_Get_StartDate()              #'07-DEC-22'
    p_EndDate = input_output.IP_Get_EndDate()                  #'07-DEC-22'
    p_CountAvgDay = int(input_output.IP_Get_CountAvgDay())     #600000
    p_CountMaxDay = int(input_output.IP_Get_CountMaxDay())     #1200000
    p_StartTime = input_output.IP_Get_StartTime()              #'08:00:00.000000'
    p_EndTime = input_output.IP_Get_EndTime()                  #'20:00:00.000000'
 
    File_TableNames = input_output.IP_Get_File_TableNames()
    print('File_TableNames', File_TableNames)
    TableNames = CommonFunctions.Get_Table_Names(File_TableNames)
    print('TableNames', TableNames)

    Table_Columns = []
    Table_Append_Objs = []
    DataFiles = []

    for i in range(len(TableNames)):
        tableName = TableNames[i].strip()
        print('Table name:', tableName)
        HeaderFile = input_output.IP_Get_HeaderFile_Table(tableName)
        DataFile = input_output.OP_Get_DataFile_Table(tableName)
        print('HeaderFile:', HeaderFile)
        print('DataFile:', DataFile)
        ColumnNames_list = CommonFunctions.Create_File_and_write_Header(HeaderFile, DataFile)
        print('ColumnNames_list:',ColumnNames_list)
        Table_Columns.append(ColumnNames_list)

        AppendFileObj = CommonFunctions.Append_File(DataFile)
        Table_Append_Objs.append(AppendFileObj)
        DataFiles.append(DataFile)


    # Get working days between start and end dates
    Working_DayDates = WorkingDates.get_WorkingDates(p_StartDate, p_EndDate)

    # Loop through each working day 
    for  DayDate in Working_DayDates:
        Day = DayDate.get('Working_Day')
        Date = DayDate.get('Working_Date')
        formatDate = '%d-%b-%y'
        formatDateTime = '%d-%b-%y %H:%M:%S.%f'
        formatted_date = DateAndTime.Convert_Datetime_to_Formatted_str(Date,formatDate)
        countPerDay = 0
        if Day == 2:
            countPerDay = p_CountMaxDay
        else:
            countPerDay = p_CountAvgDay
        
        startDateTime = formatted_date + ' ' + p_StartTime
        endDateTime = formatted_date + ' ' + p_EndTime
        elapsedNanoSec = DateAndTime.Get_Elapsed_NanoSec_Time_int(startDateTime, endDateTime, formatDateTime)
        delta = round(elapsedNanoSec / countPerDay)
        print('Date:', formatted_date, ', Message Count:', countPerDay, ', Delta in ns', delta)

        timestamp_ns = DateAndTime.Convert_Formatted_Datetime_to_Timestamp_int(startDateTime, formatDateTime)

        Append_Data_Table_Test1 = Table_Append_Objs[0]
        print('************************************* Start Time:', DateAndTime.Get_Formatted_CurrentDateTime_str(formatDateTime))

        for i in range(countPerDay):
            timestamp_ns = timestamp_ns + delta
            
            # Timestamp
            timestamp_formatted = DateAndTime.Convert_Timestamp_to_Formatted_Datetime_str(timestamp_ns, formatDateTime)
            #print(timestamp_formatted)

            # Correlation_Id
            correlation_id = CommonFunctions.Encode_to_SHA256(timestamp_formatted)
            #print(correlation_id)

            Append_Data_Table_Test1.write(timestamp_formatted + ',' + correlation_id + ',qwertyuioplkmjnhbgvfcdxsza123456789' +"\n")
        
        print('************************************* End Time  :', DateAndTime.Get_Formatted_CurrentDateTime_str(formatDateTime))
        Table_Append_Objs[0] = CommonFunctions.Reopen_File(Append_Data_Table_Test1, DataFiles[0])

    for i in range(len(Table_Append_Objs)):
        CommonFunctions.Close_File(Table_Append_Objs[i])

main()