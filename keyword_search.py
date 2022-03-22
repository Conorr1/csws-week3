#import csv
#import pandas as pd
import numpy

import csv
import pandas as pd
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
        
 
     #get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
    print(len(rows))
 #printing the field names
print('Field names are:' + ', '.join(field for field in fields))
 


  

#column_names = ['movie_Name', 'Year', 'Genre', 'Run_time', 'Rating', 'Meta_score', 'Votes', 'Director', 'cast', 'Gross']
#movie_list = pd.read_csv("regex_imdb.csv", names=column_names,  )
df = pd.read_csv('regex_imdb.csv')
def findMovies():
  while True:
    searchTerm=input("searching for ( exit to exit )?")
   
    if searchTerm == 'exit':
       break
    
    for row in rows:
      
      if(df.row[0].str.contains(searchTerm)):
         print("movie found ")
      
      
    #for row in rows:
     #     print('-----------------------')
      #    print('Name: ' + row[0])
       #   print('Year: ' + row[1])
       #   print('Genre: ' + row[2])
       #   print('Run_Time: ' + row[3]) 
       #   print('Rating: ' + row[4])
       #   print('Meta_Score: ' + row[5])
       #   print('Votes: ' + row[6])
       #   print('Director: ' + row[7])
       #   print('Cast: ' + row[8])
       #   print('SGross: ' + str ([9]))

findMovies()