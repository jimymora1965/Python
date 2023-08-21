import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cofla_ingresos.csv")
sns.barplot(x="fuente",y ="ingresos", data = df)

total_ingresos = df["ingresos"].sum()

print(f"El total de ingresos es: {total_ingresos} dolares mensuales ")


plt.show()