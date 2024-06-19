import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Ejemplocsv.csv",delimiter=";")
print(df)
plt.plot("04/05/2016",85,"o")

sns.lineplot(x="fecha",y="cantidad",data=df)
plt.show()
