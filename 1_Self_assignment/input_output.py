def input_outputs():
    input_outputs  = {}
    #Read line by line
    fileDataRead = open("1_input_output.txt",'r')
    for line in fileDataRead:
        if line.startswith('p_'):
            vals = line.split('=')
            input_outputs[vals[0].strip()] = vals[1].strip()
    fileDataRead.close()
    return input_outputs

#print(input_outputs())

def IP_Get_StartDate():
    return input_outputs().get('p_StartDate')

def IP_Get_EndDate():
    return input_outputs().get('p_EndDate')

def IP_Get_CountAvgDay():
    return input_outputs().get('p_CountAvgDay')

def IP_Get_CountMaxDay():
    return input_outputs().get('p_CountMaxDay')

def IP_Get_StartTime():
    return input_outputs().get('p_StartTime')

def IP_Get_EndTime():
    return input_outputs().get('p_EndTime')

def IP_Get_File_TableNames():
    return input_outputs().get('p_File_TableNames')

#Input GET HeaderFile for Tables
def IP_Get_HeaderFile_Table(tableName):
    return input_outputs().get('p_HeaderFile_Table_' + tableName)

#Output GET DataFile for Tables
def OP_Get_DataFile_Table(tableName):
    return input_outputs().get('p_DataFile_Table_' + tableName)
    