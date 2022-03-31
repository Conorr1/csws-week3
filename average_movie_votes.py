import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
warnings.simplefilter("ignore")
from IPython.display import display

df=pd.read_csv("regex_imdb.csv")
v=df.groupby(df["Year"])["Votes"].mean().reset_index()
print(v)
plt.figure(figsize=(10,5))
sns.lineplot(x="Year",y="Votes",data=v)
plt.title("Average movie votes over the years",fontsize=20)
plt.show()
   

