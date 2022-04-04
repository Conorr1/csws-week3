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

fig, x=plt.subplots(figsize=(10,5))
x.plot(max_rating,color='royalblue')
x.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y')

x.set_title("Highest rating for each year",fontsize=20,)
x.set_xlabel("Year",fontsize=15)
x.set_ylabel("Rating",fontsize=15)
x.set_xlim(1960)
plt.show()

