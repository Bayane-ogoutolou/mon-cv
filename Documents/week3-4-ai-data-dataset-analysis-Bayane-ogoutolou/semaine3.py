import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px 
# Charger les données
df = sns.load_dataset("iris")
df.head() 
#Créer un pairplot montrant les relatons entre toutes les variables
sns.pairplot(df, hue="species")
plt.title("Pairplot des variables d'Iris")
plt.show()
# Génerer un boxplot comparant les "sepal_length" par espèce
sns.boxplot(x="species", y="sepal_length", data=df)
plt.title("Comparaison de sepal_length par espèce")
plt.show()
# Produire un scatterplot interactif (Plotly) de "petal_length" vs "petal_width" coloré par espèce
fig = px.scatter(df, x="petal_length", y="petal_width", color="species",
                 title="Scatterplot interactif de petal_length vs petal_width")
fig.show()





