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

                        complete_name = name_shortener.NameProcessor(
                            original_name
                        ).preprocess_name()

                        short_name = name_shortener.NameProcessor(
                            original_name
                        ).get_short_name()

                        very_short_name = name_shortener.NameProcessor(
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

                    if (
                        random.randint(1, 700) == 1
                    ):  # Affichage d'un enregistrement au hasard sur 700
                        print(
                            complete_name.ljust(38),
                            short_name.ljust(23),
                            very_short_name.ljust(15),
                        )


# ------------------------------------------------------------------------------


@click.group()
def csv_file():
    pass


@csv_file.command()
@click.argument("input", type=click.Path(exists=True))
@click.argument("output", type=click.Path(exists=False))
def run_csv(input, output):
    """Command on cli1"""

    input_file_path = click.format_filename(input, shorten=False)
    print("Le fichier csv à traiter est :", input_file_path)
    output_file_path = click.format_filename(output, shorten=False)
    print("Le résultat est stocké dans :", output_file_path)

    print("")
    print("--------- Lancement du script ---------")
    print("")

    simplifier = NameShortenerCSV(input_file_path, output_file_path)
    simplifier.run()

    print("")
    print("--------- Script achevé avec succès ---------")
    print("")


@click.group()
def one_name():
    pass


@one_name.command()
@click.argument("originalname")
def run_one_name(originalname):
    """Command on cli2"""

    click.echo(f"Nom saisi : {originalname}")
    complete_name = name_shortener.NameProcessor(originalname).preprocess_name()
    click.echo(f"Nom complet : {complete_name}")
    short_name = name_shortener.NameProcessor(originalname).get_short_name()
    click.echo(f"Nom court : {short_name}")
    very_short_name = name_shortener.NameProcessor(originalname).get_very_short_name()
    click.echo(f"Nom très court : {very_short_name}")


cli = click.CommandCollection(sources=[csv_file, one_name])

# ------------------------------------------------------------------------------
if __name__ == "__main__":
    cli()
