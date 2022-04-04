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
   
sns.countplot(x="Genre", data=xx,order=xx["Genre"].value_counts().index[0:10])
plt.ylabel("Number of films")
plt.title('Number of films per Genre')
plt.xticks(rotation=45)
plt.show()

