import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
warnings.simplefilter("ignore")
from IPython.display import display

def highest_rating_by_year():
    pass

df=pd.read_csv("regex_imdb.csv")
   
print(pd.crosstab (df["Rating"],df["Year"]).mean())
avg=df["Rating"].groupby(df["Year"]).describe()
print(avg)

max_rating=avg["mean"]+avg["std"]


