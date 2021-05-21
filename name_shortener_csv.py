import sys
import getopt
import os
import random
import name_shortener
import csv

# Classe gérant le traitement d'un fichier csv
class NameShortenerCSV:
    # Description
    """Classe gérant le traitement du fichier csv"""

    # Fichiers
    _input_file = None
    _output_file = None

    # Paramètres de lecture du fichier CSV
    # Séparateur utilisé pour séparer chaque champ dans le fichier CSV
    # Par défaut c'est la virgule. Plus bas, le code essaye de détecter si
    # c'est un ";"
    _csv_sep = ","

    # Séparateur utilisé pour le fichier en sortie
    _out_sep = ","

    # Numéro d'ordre du champ contenant le nom de la commune
    _complete_name_field_num = 3
    _code_insee_field_num = 0

    # Résultat
    _outputLines = []

    # --------------------------------------------------------------------
    # Constructeur
    def __init__(self, input_file, output_file):
        # Initialisation de la liste des étapes
        self._input_file = input_file
        self._output_file = output_file

    # --------------------------------------------------------------------
    # Exécution du processus traitant l'intégralité d'un fichier csv en entrée
    def run(self):

        with open(self._input_file, encoding="utf-8", newline="") as input_csv_file:
            csv_reader = csv.reader(input_csv_file)

            num_line = 0

            for row in csv_reader:

                if num_line == 0:

                    with open(
                        self._output_file, "w", encoding="utf-8", newline=""
                    ) as output_csv_file:
                        csv_writer = csv.writer(output_csv_file)
                        csv_writer.writerow(
                            ["COM", "NOM_COMPLET", "NOM_COURT", "NOM_TRES_COURT"]
                        )

                    num_line += 1

                else:
                    original_name = row[3]
                    complete_name = name_shortener.NameProcessor(
                        original_name
                    ).preprocess_name()
                    short_name = name_shortener.NameProcessor(
                        original_name
                    ).get_short_name()
                    very_short_name = name_shortener.NameProcessor(
                        original_name
                    ).get_very_short_name()

                    with open(
                        self._output_file, "a", encoding="utf-8", newline=""
                    ) as output_csv_file:
                        csv_writer = csv.writer(output_csv_file)
                        csv_writer.writerow(
                            [row[0], complete_name, short_name, very_short_name]
                        )

                    num_line += 1

                    # Les lignes qui suivent servent juste à afficher quelques enregistrement pour
                    # contrôler visuellement le résultat sur un échantillon
                #    if len(name_parts) > 4 and num_line % 3 == 0:
                #    if len(name_parts) > 2 and num_line < 50:
                #    if "Saint" in complete_name:
                #    if "Arrondissement" in complete_name:
                #    if "L'" in complete_name:
                #    if "(" in original_complete_name:
                #    if "Vieille" in complete_name:
                #    if "Notre" in original_complete_name:
                #    if len(name_parts) > 1 and "y" in original_complete_name:
                if (
                    random.randint(1, 700) == 1
                ):  # Affichage d'un enregistrement au hasard sur 700
                    print(
                        complete_name.ljust(38),
                        short_name.ljust(23),
                        very_short_name.ljust(15),
                    )


# ------------------------------------------------------------------------------
# entrées :
# - le répertoire des fichiers à traiter
# - le répertoire de destination des nouveaux fichiers


def main():
    """Fonction principale du script"""

    root_dir = os.getcwd()  # dossier courant
    print(root_dir)
    input_file_path = "input.csv"
    output_file_path = "output.csv"

    # Récupération des paramètres et des options de la ligne de commande
    args = None
    opts = None
    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "", ["input=", "output="]
        )  # récup commande
        print(opts)
        print(args)
    except getopt.GetoptError:
        print("Pas bon")
        sys.exit(1)

    # Traitement des options
    for (o, a) in opts:
        if o in ("--input"):
            input_file_path = a
        elif o in ("--output"):
            output_file_path = a

    # Calcul des différents répertoires
    root_dir = os.getcwd()
    print(input_file_path)
    print(output_file_path)

    simplifier = NameShortenerCSV(input_file_path, output_file_path)
    simplifier.run()

    print("")
    print("--------- Script achevé avec succès ---------")
    print("")


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
