import pandas as pd

table = pd.read_csv("data/INSEE_data/commune2021.csv")


# corriger le type de la colonne "REG"
table["REG"] = pd.to_numeric(table["REG"], "coerce").fillna(0).astype(int)


# villes
header_cities_names = ["COM", "REG", "DEP", "TNCC", "NCC", "NCCENR", "LIBELLE"]
cities_names = table[header_cities_names]


# regions
regions_names = pd.read_csv("data/INSEE_data/region2021.csv")
header_regions_names = ["REG", "LIBELLE"]
regions_names = regions_names[header_regions_names]
regions_names = regions_names.rename(columns={"LIBELLE": "REG_LIBELLE"})


# departements
departments_names = pd.read_csv("data/INSEE_data/departement2021.csv")
header_departments_names = ["DEP", "LIBELLE"]
departments_names = departments_names[header_departments_names]
departments_names = departments_names.rename(columns={"LIBELLE": "DEP_LIBELLE"})


# Jointures
cities_names = cities_names.join(regions_names.set_index("REG"), on="REG")
cities_names = cities_names.join(departments_names.set_index("DEP"), on="DEP")


# ordonner les colonnes
header_cities_names = [
    "COM",
    "REG",
    "REG_LIBELLE",
    "DEP",
    "DEP_LIBELLE",
    "TNCC",
    "NCC",
    "NCCENR",
    "LIBELLE",
]
cities_names = cities_names[header_cities_names]


# supprimer les anciennes communes donc celles avec le numéro de région à 0 et remettre l'index à zéro
former_municipalities = cities_names.loc[cities_names["REG"] == 0]
cities_names = cities_names.drop(former_municipalities.index)
cities_names = cities_names.reset_index(drop=True)


# dataframe avec le minimum de colonnes nécessaires pour les noms abrégés
header_most_important_columns = ["COM", "NCC", "NCCENR", "LIBELLE"]
csv_test_input = cities_names[header_most_important_columns]


# création du nouveau CSV
cities_names.to_csv("data/INSEE_data/noms_villes.csv", index=False)
csv_test_input.to_csv("data/csv_test_input.csv", index=False)
