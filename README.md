# french-locality-name-shortener

## Objectif

Ce programme crée les noms contractés des communes françaises.


## Exemple d'utilisation

Exemple de ligne de commande :

python shorten_french_names.py --input="data/coms_france.csv" --output="data/coms_france_abrev.csv"


## Règles appliquées
### Noms courts
Si le nom ne comprend pas de '-' ou 'arrondissement', le nom court est exactement le nom complet.
Par exemple :
<table>
  <tr><td>Givonne</td><td>-></td><td>Givonne</td></tr>
</table>

Sinon, on applique au nom les règles citées ci-après.

**1- Le premier mot est conservé en entier.**

**2- Les mots suivants sont remplacés par leur équivalent :**
<table>
  <tr><td>Saint</td><td>-></td><td>St</td></tr>
  <tr><td>Sainte</td><td>-></td><td>Ste</td></tr>
  <tr><td>Saints</td><td>-></td><td>Sts</td></tr>
  <tr><td>Saintes</td><td>-></td><td>Stes</td></tr>
  <tr><td>Arrondissement</td><td>-></td><td>arr.</td></tr>
  <tr><td>l'</td><td>-></td><td>l.</td></tr>
  <tr><td>d'</td><td>-></td><td>d.</td></tr>
</table>

**3- Si le premier mot est 'St' ou une variante, le mot suivant est conservé en entier.**

**4- Les mots présents dans les tableaux suivants sont conservés.**

Les "mots de liaison" :
<table>
  <tr><td>à</td><td>au</td><td>aux</td><td></td><td></td></tr>
  <tr><td>d'</td><td>de</td><td>des</td><td>dit</td><td>du</td></tr>
  <tr><td>en</td><td>et</td><td></td><td></td><td></td></tr>
  <tr><td>l'</td><td>la</td><td>le</td><td>les</td><td>lès</td></tr>
  <tr><td>sous</td><td>sur</td><td></td><td></td><td></td></tr>
</table>

Les nombres :
<table>
  <tr>
    <td>Un</td><td>Deux</td><td>Trois</td><td>Quatre</td><td>Cinq</td><td>Six</td><td>Sept</td><td>Treize</td><td>Vingt</td><td>Cent</td><td>Mille</td>
  </tr>
</table>

Les adjectifs :
<table>
  <tr><td>Bas</td><td>Basse</td><td>Basses</td><td></td></tr>
  <tr>
    <td>Beau</td><td>Beaux</td><td>Belle</td><td>Belles</td>
  </tr>
  <tr>
    <td>Grand</td><td>Grande</td><td>Grandes</td><td>Grands</td>
  </tr>
  <tr><td>Gros</td><td>Grosse</td><td>Grosses</td><td></td></tr>
  <tr>
    <td>Haut</td><td>Haute</td><td>Hautes</td><td>Hauts</td>
  </tr>
  <tr>
    <td>Jeune</td><td>Jeunes</td><td></td><td></td>
  </tr>
  <tr>
    <td>Neuf</td><td>Neufs</td><td>Neuve</td><td>Neuves</td>
  </tr>
  <tr>
    <td>Petit</td><td>Petite</td><td>Petites</td><td>Petits</td>
  </tr>
  <tr>
    <td>Vieille</td><td>Vieilles</td><td>Vieux</td><td></td>
  </tr>
</table>

Ainsi que :
<table>
  <tr><td>Notre</td><td>Entre</td></tr>
</table>

**5- Les mots contenants "d'" ou "l'" sont abrégés comme dans les deux exemples suivants :**
<table>
  <tr><td>d'Allier</td><td>-></td><td>d'A.</td></tr>
  <tr><td>L'Abergement</td><td>-></td><td>L'A.</td></tr>
</table>

**6- Tous les autres mots sont abrégés comme dans les deux exemples suivants :**
<table>
  <tr><td>Vence</td><td>-></td><td>V.</td></tr>
  <tr><td>Berrieux</td><td>-></td><td>B.</td></tr>
</table>

### Noms très courts
Le nom très court est formé à partir du nom court.

Cela consiste à prendre le nom court en partant de la droite vers la gauche et de supprimer ou pas le mot.

**Le mot est supprimé si :**

- Le mot contient un point (".").

- Le mot est un mot de liaison ou un mot abrégé.

Par exemple :
<table>
  <tr>
    <td>St</td><td>Notre</td>
  </tr>
</table>

**Le mot est conservé si :**

- Le mot est le premier mot du nom.

*ou alors*

- Le nom commence par 'St', seulement le mot suivant est conservé.

Par exemple :
<table>
  <tr><td>St-André-d'H.</td><td>-></td><td>St-André</td></tr>
</table>

*ou alors*

- Le nom comporte un 'arr.', seulement le nom de la ville et le numéro d'arrondissement sont conservés.

Par exemple :
<table>
  <tr><td>Lyon 4e arr.</td><td>-></td><td>Lyon 4e</td></tr>
</table>


## Exemples de résultats

<table>
  <tr><td>Goudelancourt-lès-Berrieux</td><td>Goudelancourt-lès-B.</td><td>Goudelancourt</td></tr>
  <tr><td>Givonne</td><td>Givonne</td><td>Givonne</td></tr>
  <tr><td>Saint-Pierre-sur-Vence</td><td>St-Pierre-sur-V.</td><td>St-Pierre</td></tr>
  <tr><td>Soligny-les-Étangs</td><td>Soligny-les-É.</td><td>Soligny</td></tr>
  <tr><td>Fontiers-Cabardès</td><td>Fontiers-C.</td><td>Fontiers</td></tr>
  <tr><td>Paris 7e Arrondissement</td><td>Paris 7e arr.</td><td>Paris 7e</td></tr>
  <tr><td>Druyes-les-Belles-Fontaines</td><td>Druyes-les-B.-F.</td><td>Druyes</td></tr>
</table>


## Source des noms en entrée

Le fichier d'exemple en entrée présent dans le répertoire "data" est basé sur les noms de communes fournis pour l'INSEE.


## Copyright - licence

Copyright (c) 2013 Benjamin Chartier

Licence applicable : MIT (cf. license.txt à la racine de ce dépôt)