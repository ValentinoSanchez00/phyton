import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Bigotes.csv",delimiter=";")
print(df)
sns.boxplot(x="categoria",y="valor",data=df, palette="colorblind")
plt.show()
