import sys
import getopt
import os
import random
import name_shortener
import csv

import click

# Classe gérant le traitement d'un fichier csv
class NameShortenerCSV:
    # Description
    """Classe gérant le traitement du fichier csv"""

    # Fichiers
    # _input_file = None
    # _output_file = None

    # Colonne des numéros INSEE qu'on veut garder dans le fichier de sortie
    # column_insee = 0
    # column_original_name = 3

    # --------------------------------------------------------------------
    # Constructeur
    def __init__(self, input_file, output_file):
        # Initialisation de la liste des étapes
        self.input_file = input_file
        self.output_file = output_file
        self.column_insee = 0
        self.column_original_name = 3

    # --------------------------------------------------------------------
    # Exécution du processus traitant l'intégralité d'un fichier csv en entrée
    def run(self):

        with open(self.input_file, encoding="utf-8", newline="") as input_csv_file:
            csv_reader = csv.reader(input_csv_file)

            num_line = 0

            for row in csv_reader:

                if num_line == 0:

                    with open(
                        self.output_file, "w", encoding="utf-8", newline=""
                    ) as output_csv_file:
                        csv_writer = csv.writer(output_csv_file)
                        csv_writer.writerow(
                            ["COM", "NOM_COMPLET", "NOM_COURT", "NOM_TRES_COURT"]
                        )

                    num_line += 1

                else:
                    original_name = row[self.column_original_name]
                    insee_code = row[self.column_insee]

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
                        self.output_file, "a", encoding="utf-8", newline=""
                    ) as output_csv_file:
                        csv_writer = csv.writer(output_csv_file)
                        csv_writer.writerow(
                            [
                                insee_code,
                                complete_name,
                                short_name,
                                very_short_name,
                            ]
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


@click.command()
@click.argument("input", type=click.Path(exists=True))
@click.argument("output", type=click.Path(exists=False))
def main(input, output):
    """Fonction principale du script"""

    print("")
    print("--------- Lancement du script ---------")
    print("")

    input_file_path = click.format_filename(input, shorten=False)
    print("Le fichier csv à traiter est :", input_file_path)
    output_file_path = click.format_filename(output, shorten=False)
    print("Le résultat est stocké dans :", output_file_path)

    simplifier = NameShortenerCSV(input_file_path, output_file_path)
    simplifier.run()

    print("")
    print("--------- Script achevé avec succès ---------")
    print("")


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
