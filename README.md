
LeetSpeak Converter - Projet Lycée
=========================================

Un projet Python permettant la conversion bidirectionnelle entre du texte classique (humain)
et du leet speak (1337), avec deux modes de fonctionnement :

- Human → Leet
- Leet → Human

Le projet propose également une interface graphique (GUI) pour une utilisation conviviale.

Structure du code
-----------------

- importDic(fileName) :
    Importe un dictionnaire de correspondances depuis un fichier CSV (ex: A,4).

- humanToLeet(text, dic) :
    Convertit un texte humain vers du leet speak.

- leetToHuman(text, dic) :
    Reconvertit un texte leet vers du texte humain.

- maxLetters(dic) :
    Trouve la longueur maximale d’un mot leet (utile pour décoder).

- returnDic(dic) :
    Inverse le dictionnaire (leet → humain).

Exemple de dictionnaire (leet.csv)
----------------------------------
A,4
E,3
L,1
O,0
H,#
W,\/\/
R,2
D,|)

Chaque ligne contient une lettre majuscule et son équivalent leet, séparés par une virgule.

Exemple d'utilisation avec "Hello World"
----------------------------------------

dic = importDic("leet.csv")
text = "Hello World"
leet = humanToLeet(text, dic)
print(leet)  # → "#3110 \/\/021|)"

decoded = leetToHuman(leet, dic)
print(decoded)  # → "HELLO WORLD"

Deux versions disponibles
-------------------------

1. Version CLI (Console) : Interaction par terminal.
2. Version GUI (Graphique) : Utilisation via interface utilisateur.

Prérequis
---------

- Python 3.7+
- Fichier dictionnaire 'leet.csv'
- Pour GUI : Tkinter (inclus dans Python standard)

Auteur
------

Projet universitaire réalisé dans le cadre d’un travail de groupe – Licence Informatique – 2025.
