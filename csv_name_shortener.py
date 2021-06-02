import one_name_shortener

import random
import csv

# Classe gérant le traitement d'un fichier csv
class NameShortenerCSV:
    """Classe gérant le traitement d'un fichier csv."""

    # Constructeur
    def __init__(self, input_file, output_file):
        # Initialisation de la liste des étapes
        self.input_file = input_file
        self.output_file = output_file
        self.column_insee = 0
        self.column_original_name = 3

    def run(self):
        """Méthode du traitement d'un fichier csv"""

        with open(self.input_file, "r", encoding="utf-8", newline="") as input_csv_file:
            with open(
                self.output_file, "w", encoding="utf-8", newline=""
            ) as output_csv_file:

                csv_reader = csv.reader(input_csv_file)
                csv_writer = csv.writer(output_csv_file)

                num_line = 0

                for row in csv_reader:

                    if num_line == 0:
                        csv_writer.writerow(
                            ["COM", "NOM_COMPLET", "NOM_COURT", "NOM_TRES_COURT"]
                        )

                        num_line += 1

                    else:
                        original_name = row[self.column_original_name]
                        insee_code = row[self.column_insee]

                        complete_name = one_name_shortener.NameProcessor(
                            original_name
                        ).preprocess_name()

                        short_name = one_name_shortener.NameProcessor(
                            original_name
                        ).get_short_name()

                        very_short_name = one_name_shortener.NameProcessor(
                            original_name
                        ).get_very_short_name()

                        csv_writer.writerow(
                            [
                                insee_code,
                                complete_name,
                                short_name,
                                very_short_name,
                            ]
                        )

                        num_line += 1

                    # Affichage d'un enregistrement au hasard sur 700
                    if random.randint(1, 700) == 1:
                        print(
                            complete_name.ljust(38),
                            short_name.ljust(23),
                            very_short_name.ljust(15),
                        )
