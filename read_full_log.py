import json
  
#Opening files
file = open('data.txt', 'r')
outFile = open('parsed_data.txt','w')


Lines = file.readlines()

# Reads every line, takes the "full_log" field, replaces the needed characters and writes it to the output file
for line in Lines:
    data = json.loads(line)
    tempvar = (data['full_log'])
    tempvar = tempvar.replace("\\'", "'") 
    tempvar = tempvar.replace('\\"', '"')
    tempvar = tempvar.replace('\\\\', '\\')
    outFile.write(tempvar)
    outFile.write("\n")


# Closing files
file.close()
outFile.close()
