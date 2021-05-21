import copy
import re

# Chaines de caractères à conserver dans le nom court
linking_words = (
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

adjectives_and_numbers = (
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

other_parts_to_keep = ("Notre",)

parts_to_cut = {
    "saint": "St",
    "sainte": "Ste",
    "saints": "Sts",
    "saintes": "Stes",
    "arrondissement": "arr.",
}


class NameProcessor:
    def __init__(self, original_name):
        self.original_name = original_name

    def preprocess_name(self):
        # Suppression des espaces multiples, des espaces après apostrophes et des parenthèses avec leur contenu
        # print("Nom original : ", self.original_name)
        # print()
        complete_name = " ".join(self.original_name.split())
        complete_name = complete_name.replace("' ", "'")
        complete_name = complete_name.split("(")[0].strip()

        return complete_name

    def cut_name(self, name_to_cut):
        # Découpage du nom en mots
        # les séparateurs des mots sont des " " ou des "-"
        name_parts = []
        if " - " in name_to_cut:
            name_parts = name_to_cut.split(" - ")
        elif " -" in name_to_cut:
            name_parts = name_to_cut.split(" -")
        elif "- " in name_to_cut:
            name_parts = name_to_cut.split("- ")
        else:
            name_parts = re.split("( |-)", name_to_cut)
        return name_parts

    def get_short_name(self):
        short_name_parts = []
        complete_name = self.preprocess_name()
        complete_name_parts = self.cut_name(complete_name)

        # Les parties du nom ne comprennent pas '-' ou 'Arrondissement'
        if (
            "-" not in complete_name_parts
            and "Arrondissement" not in complete_name_parts
        ):
            short_name_parts = copy.copy(complete_name_parts)

        # Les parties du nom comprennent '-' ou 'Arrondissement'
        else:
            # Indicateurs utilisés pour orienter le traitement des mots suivants
            seen_first_dash = False
            seen_second_dash = False
            begin_with_saint = False
            keep_next_word = False

            # Traitement de chaque mot du nom original
            for i in range(len(complete_name_parts)):
                part = complete_name_parts[i]

                if part.lower() in parts_to_cut.keys():
                    # Remplacement de la partie par sa version raccourcie si elle est une des clés du dictionnaire parts_to_cut
                    short_name_parts.append(parts_to_cut[part.lower()])
                    if i == 0 and part.lower() != "arrondissement":
                        begin_with_saint = True
                elif i == 0:
                    # si on traite la première partie du nom et qu'elle ne contient ni saint ni Arrondissement, on ajoute la partie telle quelle
                    short_name_parts.append(part)
                elif part in linking_words:
                    # si la partie est un des mots de linking_words, on garde cette partie du nom telle quelle
                    short_name_parts.append(part)
                elif part.upper().lower() == part:
                    # si la partie du nom est en minuscules
                    short_name_parts.append(part)
                elif part in other_parts_to_keep:
                    # si la partie est un des mots de other_parts_to_keep (donc juste "Notre"). On garde cette partie du nom telle quelle
                    short_name_parts.append(part)
                elif keep_next_word:
                    # si keep_next_word = True, on ajoute la partie du nom telle quelle (et on passe keep_next_word à False)
                    short_name_parts.append(part)
                    keep_next_word = False
                elif part.upper().lower()[0:2] in ("l'", "d'"):
                    # si les deux premiers caractères de la partie sont "l'"" ou "d'", la partie prend la forme de la première lettre suivie d'un point.
                    short_name_parts.append("{0}.".format(part[0:3]))
                elif seen_first_dash and not begin_with_saint:
                    # La partie ne commence pas par 'saint' et seen_first_dash == True. Elle prend la forme de la première lettre suivie d'un point.
                    short_name_parts.append("{0}.".format(part[0]))
                elif seen_second_dash:
                    # seen_second_dash == True. Elle prend la forme de la première lettre suivie d'un point.
                    short_name_parts.append("{0}.".format(part[0]))
                else:
                    # si aucune modification au-dessus, on ajoute la partie du mot telle quelle
                    short_name_parts.append(part)

                if (
                    part in (adjectives_and_numbers or other_parts_to_keep)
                    and not seen_first_dash
                ):
                    keep_next_word = True

                if part == "-":
                    if seen_first_dash:
                        seen_second_dash = True
                    else:
                        seen_first_dash = True
        short_name = "".join(short_name_parts)
        return short_name

    def get_very_short_name(self):
        very_short_name_parts = []

        short_name = self.get_short_name()
        short_name_parts = self.cut_name(short_name)

        very_short_name_parts = copy.copy(short_name_parts)

        last_part_removed = True

        # todo: to be removed
        # print(self.original_name)

        # Traitement de chaque mot du nom court (on ne repart pas du nom complet)
        for i in range(len(short_name_parts) - 1, -1, -1):
            part = short_name_parts[i]

            # todo: to be removed
            # print(f"*{part}*")

            # On supprime la dernière partie si elle contient un '.', si elle fait partie de linking_words,
            if not last_part_removed:
                # si la dernière partie n'a pas été supprimée, fin du traitement
                pass
            elif "." in part:
                very_short_name_parts.pop()
            elif part in linking_words:
                very_short_name_parts.pop()
            elif part != " " and part.upper().lower() == part and not part[0].isdigit():
                very_short_name_parts.pop()
            elif part in parts_to_cut.values():
                very_short_name_parts.pop()
            elif part in other_parts_to_keep:
                very_short_name_parts.pop()
            else:
                last_part_removed = False
        very_short_name = "".join(very_short_name_parts)
        return very_short_name
