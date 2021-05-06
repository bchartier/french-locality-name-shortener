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
                    (complete_name, short_name, very_short_name) = self.processLine(
                        num_line, original_name
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

    # --------------------------------------------------------------------
    # Traitement d'une ligne : Calcul du nom court et du nom très court à partir du nom complet
    def processLine(self, num_line, original_name):

        short_name_parts = []
        very_short_name_parts = []

        # Suppression des espaces multiples
        complete_name = " ".join(original_name.split())

        # Suppression des espaces situés après une apostrophe
        complete_name = complete_name.replace("' ", "'")

        # Suppression des contenus des parenthèses
        # et des espaces de début et fin
        complete_name = complete_name.split("(")[0].strip()

        # Découpage du nom en mots
        # les séparateurs des mots sont des " " ou des "-"
        name_parts = []
        name_parts = divide_string_with_mutiple_seps(complete_name, [" ", "-"])

        # Chaines de caractères à conserver dans le nom court
        parts_to_keep = (
            " ",
            "-",
            "et",
            "en",
            "dit",
            "le",
            "la",
            "les",
            "l'",
            "lès",
            "en",
            "sur",
            "du",
            "de",
            "des",
            "d'",
            "sous",
            "aux",
            "à",
            "au",
            "aux",
        )

        parts_to_keep_2 = (
            "Grand",
            "Grande",
            "Grands",
            "Grandes",
            "Petit",
            "Petits",
            "Petite",
            "Petites",
            "Haute",
            "Hautes",
            "Hauts",
            "Haut",
            "Basse",
            "Basses",
            "Bas",
            "Vieux",
            "Vieille",
            "Vieilles",
            "Neuf",
            "Neufs",
            "Neuve",
            "Neuves",
            "Jeune",
            "Jeunes",
            "Gros",
            "Grosse",
            "Grosses",
            "Beau",
            "Beaux",
            "Belle",
            "Belles",
            "Un",
            "Deux",
            "Trois",
            "Quatre",
            "Cinq",
            "Six",
            "Sept",
            "Treize",
            "Vingt",
            "Cent",
            "Mille",
            "Entre",
        )

        parts_to_keep_3 = "Notre"

        # Première abréviation
        if "-" not in name_parts and "Arrondissement" not in name_parts:
            short_name_parts = copy.copy(name_parts)
        else:

            # Indicateurs utilisés pour orienter le traitement des mots suivants
            seen_first_dash = False
            seen_second_dash = False
            begin_with_saint = False
            keep_next_word = False

            # Traitement de chaque mot du nom original
            for i in range(len(name_parts)):
                part = name_parts[i]

                if part.lower() == "saint":
                    short_name_parts.append("St")
                    if i == 0:
                        begin_with_saint = True
                elif part.lower() == "sainte":
                    short_name_parts.append("Ste")
                    if i == 0:
                        begin_with_saint = True
                elif part.lower() == "saintes":
                    short_name_parts.append("Stes")
                    if i == 0:
                        begin_with_saint = True
                elif part.lower() == "saints":
                    short_name_parts.append("Sts")
                    if i == 0:
                        begin_with_saint = True
                elif part.lower() == "arrondissement":
                    short_name_parts.append("arr.")
                elif i == 0:
                    short_name_parts.append(part)
                elif part in parts_to_keep:
                    short_name_parts.append(part)
                elif part.upper().lower() == part:
                    short_name_parts.append(part)
                elif part in parts_to_keep_3:
                    short_name_parts.append(part)
                elif keep_next_word:
                    short_name_parts.append(part)
                    keep_next_word = False
                elif part.upper().lower()[0:2] in ("l'", "d'"):
                    short_name_parts.append("{0}.".format(part[0:3]))
                elif seen_first_dash and not begin_with_saint:
                    short_name_parts.append("{0}.".format(part[0]))
                elif seen_second_dash:
                    short_name_parts.append("{0}.".format(part[0]))
                else:
                    short_name_parts.append(part)

                if part in parts_to_keep_2 and not seen_first_dash:
                    keep_next_word = True

                if part in parts_to_keep_3 and not seen_first_dash:
                    keep_next_word = True

                if part == "-":
                    if seen_first_dash:
                        seen_second_dash = True
                    else:
                        seen_first_dash = True

        # Deuxième abréviation
        very_short_name_parts = copy.copy(short_name_parts)
        last_part_removed = True

        # Traitement de chaque mot du nom court (on ne repart pas du nom complet)
        for i in range(len(short_name_parts) - 1, -1, -1):
            part = short_name_parts[i]

            if not last_part_removed:
                pass
            elif "." in part:
                very_short_name_parts.pop()
            elif part in parts_to_keep:
                very_short_name_parts.pop()
            elif part != " " and part.upper().lower() == part and not part[0].isdigit():
                very_short_name_parts.pop()
            elif part in ("St", "Sts", "Ste", "Stes"):
                very_short_name_parts.pop()
            elif part == "Notre":
                very_short_name_parts.pop()
            else:
                last_part_removed = False

        return (
            complete_name,
            "".join(short_name_parts),
            "".join(very_short_name_parts),
        )


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
