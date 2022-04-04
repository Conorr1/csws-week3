import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
import plotly.graph_objects as go
warnings.simplefilter("ignore")
from IPython.display import display
def highest_grossed_movies():
    pass
df=pd.read_csv("regex_imdb.csv")

nam=df.groupby(df["Name"])["Gross"].max().sort_values(ascending=False).head(10).reset_index()
nam["Gross"]
print(nam)

x=df.groupby(df["Name"])["Gross"].max().sort_values(ascending=False).head(10)


