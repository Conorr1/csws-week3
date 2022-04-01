import csv
import sys
from average_movie_votes import average_movie_votes
from average_runtime_by_year import average_runtime_by_year
from basic_info import basicInfo
from gross_of_highest_rated import gross_of_highest_rated
from highest_grossed_movies import highest_grossed_movies
from keyword_search import findMovies
from top_10_film_director import top10


def Option1():
    findMovies

def Option2():
  average_movie_votes

def Option3():
 average_runtime_by_year

def Option4():
  gross_of_highest_rated

def Option5():
  highest_grossed_movies

def Option6():
  basicInfo

def Option7():
  top10
   
menu_options = {
  1:'Keyword Search',
  2:'Average Movie Votes',
  3:'Average Runtime per Year',
  4:'Gross of Highest Rated Movies',
  5:'Highest Grossed movies',
  6:'Basic Info On dataset',
  7:'Top 10 Movie Directors',
  8:'exit!',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


    option=int(input("What would you like to do? "))
    if option==1: 
      Option1
    elif option==2:
      Option2
    elif option==3:
      Option3
    elif option==4:
      Option4
    elif option==5:
      Option5
    elif option==6:
      Option6
    elif option==7:
      Option7
    elif option==8:
      sys.exit
    else:
      print('Invalid option. Please enter a number between 1 and 8.')
    
      

