import sys
import getopt
import os
import string
import copy
import random
import codecs

# Fonction découpant une chaîne en plusieurs parties en utilisant
# le séparateur fourni en paramètre
def divide_string_with_one_sep(s, sep):
    parts = []

    if s == None or sep == "" or sep == None:
        return parts.append(s)

    before_sep = None
    after_sep = s

    while len(after_sep) > 0:
        before_sep, sep, after_sep = after_sep.partition(sep)
        if len(before_sep) > 0:
            parts.append(before_sep)
        if len(sep) > 0:
            parts.append(sep)

    return parts


# Fonction découpant une chaîne en plusieurs parties
# Les séparateurs à utiliser sont présents dans une liste
# Grosso modo, cette fonction ne fait qu'appeler la fonction
# divide_string_with_one_sep de manière itérative avec un séparateur
# différent
def divide_string_with_mutiple_seps(s, seps):
    parts = [s]
    temp_parts = []

    for sep in seps:
        for part in parts:
            temp_parts.extend(divide_string_with_one_sep(part, sep))

        parts = copy.copy(temp_parts)
        temp_parts = []

    return parts


# Traitement d'un nom : Calcul du nom court et du nom très court à partir du nom complet
def processName(original_name):

    short_name_parts = []
    very_short_name_parts = []
    short_name = ""
    very_short_name = ""

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

    short_name = "".join(short_name_parts)
    very_short_name = "".join(very_short_name_parts)

    return (
        complete_name,
        short_name,
        very_short_name,
    )
