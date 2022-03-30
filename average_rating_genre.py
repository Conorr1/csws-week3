import csv
import statistics

from statistics import mean
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



filename = open('regex_imdb.csv', 'r', encoding="utf-8")
file = csv.DictReader(filename)

ratings = []
genre = []
delete_empty = [ele for ele in genre if ele.strip()]


for col in file:
    ratings.append(col['Rating'])
    genre.append(col['Genre'])


y = ''.join(ratings)
z = int(y)
results = [z]
# results = [int(item) for item in results]
print(results)
# print("Ratings: ", type(ratings))
# list_avg = mean(ratings)
# print(type(ratings))



# print("genre", genre)
# print(k)
 
 # with open('regex_imdb.csv', 'r') as f:
#     reader = csv.reader(f)
#     if row[4]:
#         next(reader)
#     the_numbers = [float(row[4]) for row in rows]
#     average = sum(the_numbers) / len(the_numbers)

# rating_list = []
# # with open("regex_imdb.csv", "r") as f:
# #     for row in rows:
# #         rating = row[4]
# #         if rating is not None and rating is not "--":
# #             rating_list.append(float(row[rating]))
# # avg_rating = sum(rating_list) / len(rating_list)
# # print ("avg of rating: ", avg_rating)

   

