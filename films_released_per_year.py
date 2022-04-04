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
   
plt.figure(figsize=(20,10))
sns.countplot(df["Year"], color = 'purple')
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y')
plt.title("Number of films released per year",fontsize=20)
plt.xlabel("Year")
plt.ylabel("Number of films")
plt.xticks(rotation=90)
plt.show()

