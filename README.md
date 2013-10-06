# french-locality-name-shortener

## Objectif

Ce programme crée les noms contractés des communes françaises.


## Exemple d'utilisation

Exemple de ligne de commande :

python shorten_french_names.py --input="data/coms_france.csv" --output="data/coms_france_abrev.csv"


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

Licence applciable : MIT (cf. license.txt à la racine de ce dépôt)