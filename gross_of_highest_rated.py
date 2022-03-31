import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
warnings.simplefilter("ignore")
from IPython.display import display

df=pd.read_csv("regex_imdb.csv")

df.head(2)
bb=df[["Name","Rating","Gross"]].sort_values("Rating").reset_index()[-10:]
print(bb)

plt.figure(figsize=(20,5))
sns.barplot(x="Name",y="Gross",hue="Rating",data=bb)
plt.title("GROSS OF THE TOP 10 HIGHEST RATING MOVIES",fontsize=15)
plt.xticks(rotation=90)
plt.show()