import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
warnings.simplefilter("ignore")
from IPython.display import display

df=pd.read_csv("regex_imdb.csv")

df.head(2)

print(pd.crosstab (df["Run_time"],df["Year"]).mean())
avg=df["Run_time"].groupby(df["Year"]).describe()
print(avg)

avg_runtime=avg["mean"]
avg_runtime_min=avg["mean"]-avg["std"]
avg_runtime_max=avg["mean"]+avg["std"]

fig, x=plt.subplots(figsize=(10,5))
x.plot(avg_runtime,color='red')
x.plot(avg_runtime_min,color='cyan')
x.plot(avg_runtime_max,color='green')
x.fill_between(avg.index,avg_runtime_min,avg_runtime_max,color="white")
plt.legend(['Runtime', 'Min Runtime', 'Max Runtime'], loc='upper left')
x.set_title("Average run-time over the years",fontsize=20,)
x.set_xlabel("Year of release",fontsize=15)
x.set_ylabel("Time Played in Minutes",fontsize=15)
x.set_xlim(1960)
plt.show()