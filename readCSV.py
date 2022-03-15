
import csv
# csv file name
filename = 'regex_imdb.csv'
 
# initializing the titles and rows list
fields = []
rows = []
 
#reading csv file
with open(filename, 'r', encoding='utf-8') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
     #extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
        if
 
     #get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
    print(len(rows))
 #printing the field names
print('Field names are:' + ', '.join(field for field in fields))
 


  