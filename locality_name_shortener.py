import one_name_shortener
import csv_name_shortener

import click


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

    simplifier = csv_name_shortener.NameShortenerCSV(input_file_path, output_file_path)
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
    complete_name = one_name_shortener.NameProcessor(originalname).preprocess_name()
    click.echo(f"Nom complet : {complete_name}")
    short_name = one_name_shortener.NameProcessor(originalname).get_short_name()
    click.echo(f"Nom court : {short_name}")
    very_short_name = one_name_shortener.NameProcessor(
        originalname
    ).get_very_short_name()
    click.echo(f"Nom très court : {very_short_name}")


cli = click.CommandCollection(sources=[csv_file, one_name])


if __name__ == "__main__":
    cli()
