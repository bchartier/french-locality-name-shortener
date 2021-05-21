from name_shortener import NameProcessor

# test des noms simples
def test_process_name_simple():
    name = NameProcessor("Ambronay")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "Ambronay",
        "Ambronay",
        "Ambronay",
    )


# noms composés
def test_process_name_compound():
    name = NameProcessor("L' Abergement-Clémenciat")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "L'Abergement-Clémenciat",
        "L'Abergement-C.",
        "L'Abergement",
    )


# noms avec des parenthèses
def test_process_name_parenthesis():
    name = NameProcessor("Bors (Canton de Baignes-Sainte-Radegonde)")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "Bors",
        "Bors",
        "Bors",
    )


# noms avec parts_to_keep_1
def test_process_name_parts_to_keep_1():
    name = NameProcessor("Margny-lès-Compiègne")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "Margny-lès-Compiègne",
        "Margny-lès-C.",
        "Margny",
    )


# noms avec parts_to_keep_2
def test_process_name_parts_to_keep_2():
    name = NameProcessor("Saint-Amand-des-Hautes-Terres")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "Saint-Amand-des-Hautes-Terres",
        "St-Amand-des-H.-T.",
        "St-Amand",
    )


# noms avec parts_to_keep_3 == "Notre"
def test_process_name_parts_to_keep_3():
    name = NameProcessor("Esquay-Notre-Dame")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "Esquay-Notre-Dame",
        "Esquay-Notre-D.",
        "Esquay",
    )


# noms avec "saint"
def test_process_name_saint():
    name = NameProcessor("Saint-Brice-sous-Forêt")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "Saint-Brice-sous-Forêt",
        "St-Brice-sous-F.",
        "St-Brice",
    )


# noms avec "sainte"
def test_process_name_sainte():
    name = NameProcessor("Sainte-Julie")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "Sainte-Julie",
        "Ste-Julie",
        "Ste-Julie",
    )


# noms avec "saintes"
def test_process_name_saintes():
    name = NameProcessor("Saintes-Maries-de-la-Mer")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "Saintes-Maries-de-la-Mer",
        "Stes-Maries-de-la-M.",
        "Stes-Maries",
    )


# noms avec "saints"
def test_process_name_saints():
    name = NameProcessor("La Chapelle-aux-Saints")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "La Chapelle-aux-Saints",
        "La Chapelle-aux-Sts",
        "La Chapelle",
    )


# noms avec "arrondissement":
def test_process_name_arrondissement():
    name = NameProcessor("Lyon 5e  Arrondissement")
    assert (
        name.preprocess_name(),
        name.get_short_name(),
        name.get_very_short_name(),
    ) == (
        "Lyon 5e Arrondissement",
        "Lyon 5e arr.",
        "Lyon 5e",
    )
