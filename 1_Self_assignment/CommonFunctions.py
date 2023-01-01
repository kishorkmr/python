import base64
import hashlib

def Encode_to_Base64(decodedString):
    b = base64.b64encode(bytes(decodedString, 'utf-8')) # bytes
    base64_str = b.decode('utf-8') # convert bytes to string
    return base64_str

def Encode_to_SHA256(decodedString):
    sha256_str = hashlib.sha256(decodedString.encode('utf-8')).hexdigest() 
    return sha256_str

def Get_Table_Names(fileTableNames):
    tableNames = []
    fileDataRead = open(fileTableNames,'r')
    for line in fileDataRead:
        tableNames.append(line.strip())
    return tableNames

def Create_File_and_write_Header(HeaderFile, DataFile):
    Read_HeaderFile = open(HeaderFile,'r')
    ColumnNames = Read_HeaderFile.readline().strip()
    ColumnNames_list = ColumnNames.split(',')

    Write_DataFile = open(DataFile,'w')
    Write_DataFile.write(ColumnNames + "\n")
    Write_DataFile.close()

    return ColumnNames_list

def Append_File(fileName):
    AppendFileObj = open(fileName, 'a')
    return AppendFileObj
    
def Close_File(fileObject):
    fileObject.close()

def Reopen_File(fileObject,fileName):
    Close_File(fileObject)
    return Append_File(fileName)





def main():
    decoded_str = '06-Dec-22 08:00:01.000000'
    encoded_base64_str = Encode_to_Base64(decoded_str)
    print('Base64 encoded string:', encoded_base64_str)

    encoded_sha256_str = Encode_to_SHA256(decoded_str)
    print('Sha256 encoded string:', encoded_sha256_str)

#main()