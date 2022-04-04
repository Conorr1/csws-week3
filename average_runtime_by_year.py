import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
warnings.simplefilter("ignore")
from IPython.display import display

def average_runtime_by_year():
    pass
df=pd.read_csv("regex_imdb.csv")

df.head(2)

print(pd.crosstab (df["Run_time"],df["Year"]).mean())
avg=df["Run_time"].groupby(df["Year"]).describe()
print(avg)

avg_runtime=avg["mean"]
avg_runtime_min=avg["mean"]-avg["std"]
avg_runtime_max=avg["mean"]+avg["std"]

