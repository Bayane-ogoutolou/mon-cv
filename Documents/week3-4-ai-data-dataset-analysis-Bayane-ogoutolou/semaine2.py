import pandas as pd

# Spécifie bien le chemin avec l'extension .data
df = pd.read_csv(r"C:\Users\LENOVO T450s\Downloads\Python\Porjet de pratique\iris\iris.data", header=None)

# Affiche les premières lignes pour vérifier
print("Colonnes initiales :", df.columns)

#  Nettoyer les valeurs manquantes dans sepal_length
median_sepal_length = df["sepal_length"].median()
df["sepal_length"].fillna(median_sepal_length, inplace=True)

# Supprimer les doublons
df = df.drop_duplicates()

# Ajouter la colonne petal_ratio
df["petal_ratio"] = df["petal_length"] / df["petal_width"]

# Filtrer selon sepal_width > 2.3
df = df[df["sepal_width"] > 2.3]

# Sauvegarder le fichier nettoyé
df.to_csv("cleaned_iris.csv", index=False)
print("Fichier nettoyé enregistré sous 'cleaned_iris.csv'")


