import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
warnings.simplefilter("ignore")
from IPython.display import display

def top10():
    pass
df=pd.read_csv("regex_imdb.csv")

x=df.groupby(by=df["Director"])["Gross"].max().sort_values(ascending=False).head(10)

print(x)

plt.title("DIRECTORS WHO HAVE DIRECTED THE TOP  GROSS MOVIES")
y=sns.barplot(x.index,x.values)
y.set_xlabel("DIRECTORS")
plt.xticks(rotation=45)
plt.show()