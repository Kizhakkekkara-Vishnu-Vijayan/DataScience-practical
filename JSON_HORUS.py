import pandas as pd
#Input Agreement
sInputFileName='E:/MSCIT/DS/Country_Code.json'
InputData=pd.read_json(sInputFileName,
 orient='index',
 encoding="latin-1")
print('Input Data Values =========')
print(InputData)
print('=======================')
# Processing Rules
ProcessData=InputData
# Remove columns ISO-2-Code and ISO-3-CODE
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)
# Rename Country and ISO-M49
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
# Set new Index
ProcessData.set_index('CountryNumber', inplace=True)
# Sort data by CurrencyNumber
ProcessData.sort_values('CountryName', axis=0, ascending=False, 
inplace=True)
print('Process Data Values ===============')
print(ProcessData)
print('========================')
# Output Agreement
OutputData=ProcessData
sOutputFileName='E:/MSCIT/DS/HORUS-JSON-Country.csv'
OutputData.to_csv(sOutputFileName, index = False)
print('JSON to HORUS - Done')
# Utility done
