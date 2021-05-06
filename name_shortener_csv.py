from name_shortener import *

# Classe gérant le traitement d'un fichier csv
class NameShortener:
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
    _complete_name_field_num = 7
    _code_insee_field_num = 6
    _pop_field_num = 10

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

        new_lines = []

        # Lecture et traitement du fichier en entrée
        input_file_object = open(self._input_file)
        try:
            num_line = 0
            for line in input_file_object:

                # Est-ce que le séparateur ne devrait pas plutôt être un point-virgule ?
                # On regarde combien de virgules et de points-virgules sont présents dans
                # la première ligne du fichier en entrée. On utilsie le séparateur présent
                # le plus grand nombre de fois
                if num_line == 0:
                    if line.count(",") < line.count(";"):
                        self._csv_sep = ";"

                    new_lines.append(
                        self._out_sep.join(
                            ["code_insee", "pop", "nom", "nom_court", "nom_tres_court"]
                        )
                        + "\n"
                    )

                if num_line > 0:
                    fields = line.split(self._csv_sep)
                    original_name = fields[self._complete_name_field_num]
                    pop = "".join(fields[self._pop_field_num].split())
                    code_insee = fields[self._code_insee_field_num]

                    # Cas particulier des communes des DOM pour lesquelles on retire le troisième caractère
                    # du code INSEE
                    if len(code_insee) == 6:
                        code_insee = code_insee[:3] + code_insee[4:]

                    # Calcul du nom court et du nom très court à partir du nom complet
                    (complete_name, short_name, very_short_name) = processName(
                        original_name
                    )

                    # On ajoute un nouvel enregistrement dans le tableau qui servira à écrire le fichier en sortie
                    # Chaque enregistrement comprend le code INSEE, la population, le nom complet,
                    # le nom un peu plus court, et le nom très court
                    new_lines.append(
                        self._out_sep.join(
                            [
                                code_insee.rjust(5, "0"),
                                pop,
                                complete_name,
                                short_name,
                                very_short_name,
                            ]
                        )
                        + "\n"
                    )

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

                num_line += 1
        finally:
            input_file_object.close()

        # Ecriture du fichier en sortie
        output_file_object = codecs.open(self._output_file, "w", "utf-8")
        output_file_object.writelines(new_lines)
        output_file_object.close()


# ------------------------------------------------------------------------------
# entrées :
# - le répertoire des fichiers à traiter
# - le répertoire de destination des nouveaux fichiers


def main():
    """Fonction principale du script"""

    root_dir = os.getcwd()
    print(root_dir)
    input_file_path = "input.csv"
    output_file_path = "output.csv"

    # Récupération des paramètres et des options de la ligne de commande
    args = None
    opts = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["input=", "output="])
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

    simplifier = NameShortener(input_file_path, output_file_path)
    simplifier.run()

    print("")
    print("--------- Script achevé avec succès ---------")
    print("")


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
