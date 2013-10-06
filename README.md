# french-locality-name-shortener

## Objectif

Ce programme crée les noms contractés des communes françaises.


## Exemple d'utilisation

Exemple de ligne de commande :

python shorten_french_names.py --input="data/coms_france.csv" --output="data/coms_france_abrev.csv"


## Exemples de résultats

 | Goudelancourt-lès-Berrieux              | Goudelancourt-lès-B.     | Goudelancourt | 
 | Givonne                                 | Givonne                  | Givonne | 
 | Saint-Pierre-sur-Vence                  | St-Pierre-sur-V.         | St-Pierre | 
 | Soligny-les-Étangs                      | Soligny-les-É.           | Soligny | 
 | Fontiers-Cabardès                       | Fontiers-C.              | Fontiers | 
 | Mireval-Lauragais                       | Mireval-L.               | Mireval | 
 | Saint-Martin-de-Mailloc                 | St-Martin-de-M.          | St-Martin | 
 | Beaumont-sur-Vingeanne                  | Beaumont-sur-V.          | Beaumont | 
 | Fraignot-et-Vesvrotte                   | Fraignot-et-V.           | Fraignot | 
 | Saint-Vincent-de-Paul                   | St-Vincent-de-P.         | St-Vincent | 
 | Saint-Pierre                            | St-Pierre                | St-Pierre | 
 | Paris 7e Arrondissement                 | Paris 7e arr.            | Paris 7e | 
 | Druyes-les-Belles-Fontaines             | Druyes-les-B.-F.         | Druyes | 


## Source des noms en entrée

Le fichier d'exemple en entrée présent dans le répertoire "data" est basé sur les noms de communes fournis pour l'INSEE.


## Copyright - licence

Copyright (c) 2013 Benjamin Chartier

Licence applciable : MIT (cf. license.txt à mla racine de ce dépôt)