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

xx=pd.DataFrame()
xx["Genre"]=np.hstack([np.array(x.split(",")) for x in df.Genre])
xx["Genre"]=xx["Genre"].str.strip()
xx["Genre"].value_counts()
   

