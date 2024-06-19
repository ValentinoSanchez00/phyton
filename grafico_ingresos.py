import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Ingresos.csv",delimiter=";")
print(df)
sns.barplot(x="fuente",y="ingreso",data=df, palette="colorblind")
total_ingresos=df["ingreso"].sum()
print(f"Total de ingresos es ${total_ingresos} USD")
plt.show()
