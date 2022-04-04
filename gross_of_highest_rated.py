import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
warnings.simplefilter("ignore")
from IPython.display import display

def gross_of_highest_rated():
    pass

df=pd.read_csv("regex_imdb.csv")

df.head(2)
bb=df[["Name","Rating","Gross"]].sort_values("Rating").reset_index()[-10:]
print(bb)

