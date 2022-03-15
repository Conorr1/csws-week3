import csv
import pandas as pd
column_names = ['Name', 'Year', 'Genre', 'Run_time', 'Rating', 'Meta_score', 'Votes', 'Director', 'cast', 'Gross']
movie_list = pd.read_csv('regex_imdb.csv', names=column_names )      
def findMovies(movieList):
  while True:
    searchTerm=input("searching for ( exit to exit )?")
    if searchTerm == 'exit':
       break
    movieList = movieList[movieList.movie_Name.str.contains(searchTerm)].to_numpy()
    if len(movieList) == 0:
       print("No Movie found ")
       continue
    for movies in movieList:
            print("-----------------------")
            print("Name: " + movies[0])
            print("Year: " + movies[1])
            print("Genre: " + movies[2])
            print("Run_Time: " + movies[3]) 
            print("Rating: " + movies[4])
            print("Meta_Score: " + movies[5])
            print("Votes: " + movies[6])
            print("Director: " + movies[7])
            print("Cast: " + movies[8])
            print("Gross: " + str(movies[9]))