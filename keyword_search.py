import csv
from operator import contains
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
 

def findMovies():
  while True:
    searchTerm=input("searching for ( exit to exit )?") #user input as to which movie they want to search
   
    if searchTerm == 'exit': # if user wants to exit search
       break
    
    for row in rows:# searching rows in csv
      
      if searchTerm in row[0]:# checks if the search term is in any of the rows , is character case bound so uppercase
         print("movie found ")
         print(" Name: " + row[0])
         print(" Year: " + row[1])
         print(" Genre: " + row[2])
         print(" Run_Time: " + row[3]) 
         print(" Rating: " + row[4])                  #displays all the infor abou the searched movie
         print(" Meta_Score: " + row[5])
         print(" Votes: " + row[6])
         print(" Director: " + row[7])
         print(" Cast: " + row[8])
         print(" Gross: " +  row[9])
     
         
      
   

findMovies() # calls function