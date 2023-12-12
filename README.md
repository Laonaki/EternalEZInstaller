
# Eternal Retro EZ Installer
Ce projet contourne les sécurités de Eternal pour proposer un téléchargement et une installation rapide et 100% automatique du dernier client de la version Retro Eternal. Le client 1.40.13 est **non requis** (les clés sont déjà fournies dans le script).

## Comment utiliser facilement le script ?
1) Télécharger le script disponible se trouvant dans le dossier executables
2) Lancer le script et attendre qu'il se termine
3) Profiter du jeu

Les sources du script sont dispo dans le dossier sources. C'est un script Python que vous pouvez auditer et compiler vous même si vous avez pas confiance dans les binaires qui sont proposés, et qui ont été construits avec PyInstaller (un module Pip3).
Le script fonctionne sous Linux aussi mais il faut le lancer soi même avec Python.

## Informations à propos du .exe
VirusTotal du .exe : https://www.virustotal.com/gui/file/fd93bd8c19ae0760fbe50ce0fdf599a4b185d690ca4d6e0273781e7c6e04888a/detection
Windows Defender le détecte comme faux positif et le supprimera peut être de votre PC automatiquement. Soit vous désactivez Windows Defender, soit il faut lancer le script manuellement.

### Lancement manuel du script avec Python (plus difficile mais aucun soucis avec les antivirus)
1) Télécharger Python : https://www.python.org/downloads/
2) Installer Python et bien cocher (si Windows) l'option "Add python.exe to path"
3) Ouvrir une invite de commandes dans le dossier "sources" (c'est le dossier dans lequel se trouve le fichier "eternalupdater.py")
4) Entrer cette commande pour installer les dépendances : 
```
pip install -r requirements.txt
```
5) Entrer cette commande pour exécuter le script avec Python : 
```
python eternalupdater.py
```