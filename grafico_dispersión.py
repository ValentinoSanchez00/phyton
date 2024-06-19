import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Ingresos.csv",delimiter=";")
print(df)
sns.catplot(x="fuente",y="ingreso",data=df, palette="colorblind")
plt.show()
