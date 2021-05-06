from name_shortener import processName

# test des noms simples
def test_process_name_simple():
    assert processName("Ambronay") == ("Ambronay", "Ambronay", "Ambronay")


# noms composés
def test_process_name_compound():
    assert processName("L' Abergement-Clémenciat") == (
        "L'Abergement-Clémenciat",
        "L'Abergement-C.",
        "L'Abergement",
    )


# noms avec des parenthèses
def test_process_name_parenthesis():
    assert processName("Bors (Canton de Baignes-Sainte-Radegonde)") == (
        "Bors",
        "Bors",
        "Bors",
    )


# noms avec parts_to_keep_1
def test_process_name_parts_to_keep_1():
    assert processName("Margny-lès-Compiègne") == (
        "Margny-lès-Compiègne",
        "Margny-lès-C.",
        "Margny",
    )


# noms avec parts_to_keep_2
def test_process_name_parts_to_keep_2():
    assert processName("Saint-Amand-des-Hautes-Terres") == (
        "Saint-Amand-des-Hautes-Terres",
        "St-Amand-des-H.-T.",
        "St-Amand",
    )


# noms avec parts_to_keep_3 == "Notre"
def test_process_name_parts_to_keep_3():
    assert processName("Esquay-Notre-Dame") == (
        "Esquay-Notre-Dame",
        "Esquay-Notre-D.",
        "Esquay",
    )


# noms avec "saint"
def test_process_name_saint():
    assert processName("Saint-Brice-sous-Forêt") == (
        "Saint-Brice-sous-Forêt",
        "St-Brice-sous-F.",
        "St-Brice",
    )


# noms avec "sainte"
def test_process_name_sainte():
    assert processName("Sainte-Julie") == (
        "Sainte-Julie",
        "Ste-Julie",
        "Ste-Julie",
    )


# noms avec "saintes"
def test_process_name_saintes():
    assert processName("Saintes-Maries-de-la-Mer") == (
        "Saintes-Maries-de-la-Mer",
        "Stes-Maries-de-la-M.",
        "Stes-Maries",
    )


# noms avec "saints"
def test_process_name_saints():
    assert processName("La Chapelle-aux-Saints") == (
        "La Chapelle-aux-Saints",
        "La Chapelle-aux-Sts",
        "La Chapelle",
    )


# noms avec "arrondissement":
def test_process_name_arrondissement():
    assert processName("Lyon 5e  Arrondissement") == (
        "Lyon 5e Arrondissement",
        "Lyon 5e arr.",
        "Lyon 5e",
    )
