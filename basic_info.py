import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
warnings.simplefilter("ignore")
from IPython.display import display
def basicInfo():
    pass
df=pd.read_csv("regex_imdb.csv")
df["Meta_score"]=df["Meta_score"].fillna(df["Meta_score"].median())
df["Meta_score"]=df["Meta_score"].apply(np.round)
df["Gross"]=df["Gross"].fillna(df["Gross"].median())  #impute missing values in meta-score, director etc 
df["Gross"]=df["Gross"].apply(np.round,decimals=2)     #to make analyzing more efficent
df["Director"]=df["Director"].fillna(df["Director"].mode()[0])
df.isna().sum()

df["Meta_score"]=df["Meta_score"].astype("int") #changes row meta_score to an int instead 
                                                 #  of a float for easier processing

df.head() #displays first 4 rows of data set
# display(df.head())

df.dtypes  #displays the data types 
print(df.dtypes)

df.info() # displays non-null count
print(df.info)


