README
Notre ontologie a pour objectif de répertorier les liens entre des artistes (musiciens, peintres ou acteurs) et leur oeuvres (musiques, peintures et films). Pour cela, nous avons décidé de scrapper des sites listant un grand nombre de ces derniers.


Les musiques ainsi que leur compositeur ont été récupérer sur ce site : https://www.cs.ubc.ca/~davet/music/list/Best2.html tandis que ce site https://www.moma.org/collection/works?locale=fr&utf8=%E2%9C%93&q=&classifications=9&date_begin=Pre-1850&date_end=2018&include_uncataloged_works=1 contient un ensemble de peinture.


Les informations  étant bien structurées sur les pages webs, il n’y a pas été nécessaire d’utiliser une bibliothèque comme scrapy afin de récupérer les entitées nommées présentes dans un texte en langage naturel. Nous avons donc uniquement utilisé Beautiful Soup qui est une bibliothèque permettant de parser du code (X)HTML.


À l’aide de cette bibliothèque nous avons donc créer un scrapper pour ces deux pages web qui retourne respectivement dans un dictionnaire les Musiciens associé à leur Chansons, et les Peintres associé à leur Peintures.


Pour ce qui est de la récupération des films et des acteurs, nous avons trouvé la page http://www.allocine.fr/films/ qui en répertorie certains. 


Dans un premier temps, Beautiful Soup nous a permis de récupérer la partie du code html nous intéressant, puis nous avons utiliser scrapy afin de déterminer les entitées nommées. Nous avons ensuite récupéré celle possèdent les labels “PERSON” et “WORK_OF_ART” et avons établis des relations entre eux. Nous sommes partis du principe que toutes les entitées d’une même phrase étaient liées entre elle.


Pour ce qui est du résultat, nous obtenons une reconnaissance des personnes correctes, mais presque aucun des noms des films. Nous avons tout de même choisis de conserver ces résultats, car nous avons réussi à récupérer de nombreuses relations pour les acteurs, comme les genres de film dans lequel ils ont jouées.