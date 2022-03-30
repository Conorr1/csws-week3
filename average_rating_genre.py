import csv
from lib2to3.pgen2.token import EQUAL
import statistics
# csv file name
filename = 'C:/Users/csmclunt/OneDrive - Liverpool John Moores University/csws(Team 4)/csws-week3/regex_imdb.csv'
 
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
        
 
     #get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
    print(len(rows))
 #printing the field names
print('Field names are:' + ', '.join(field for field in fields))
 
rating_list = []
with open("C:/Users/csmclunt/OneDrive - Liverpool John Moores University/csws(Team 4)/csws-week3/regex_imdb.csv", "r") as f:
    for row in rows:
        rating = row[4]
        if rating is not None and rating is not "--":
            rating_list.append(float(row[rating]))
avg_rating = sum(rating_list) / len(rating_list)
print ("avg of rating: ", avg_rating)

   

