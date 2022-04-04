import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
warnings.simplefilter("ignore")
from IPython.display import display

def average_movie_votes():
      pass    

df=pd.read_csv("regex_imdb.csv")
v=df.groupby(df["Year"])["Votes"].mean().reset_index()
print(v)

   

