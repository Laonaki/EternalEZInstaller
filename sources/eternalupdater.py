from urllib.request import urlopen 
import json
import sys, os
import platform
import wget
from hashlib import sha256
import py7zr
from showinfm import show_in_file_manager
ETERNAL_WEBSITE = "https://eternal-games.com/"

if getattr(sys, 'frozen', False):
    APPLICATION_PATH = os.path.dirname(sys.executable)
elif __file__:
    APPLICATION_PATH = os.path.dirname(__file__)

def printHeader():
	print("=== Eternal EZ Installer V1.0 ===")
	print("Cet outil va t'aider à mettre en place facilement et rapidement la dernière version du client Eternal sans prise de tête. Fais-toi un café, croises les doigts et laisses le script te préparer en quelques minutes une version jouable.")
	print("DO WHAT U WANT CAUSE' A PIRATE IS FREE")
	print("=================================")
def downloadRetro():
	print("Etape 1/4 : Récupération des infos de build du dernier client disponible")
	buildDataJsonURL = "https://web-back.eternal-games.com/api/client-releases/last-build-data"
	buildDataResponse = urlopen(buildDataJsonURL) 
	buldDataJson = json.loads(buildDataResponse.read())   
	lastVersion = buldDataJson["version"]
	if "keyPartToHash" not in buldDataJson:
		print("La mise à jour n'est pas encore sortie, réessayes plus tard")
	else:
		keyPartToHash = buldDataJson["keyPartToHash"]
		folderName = os.path.join(APPLICATION_PATH, "retro-" + lastVersion)
		if not os.path.exists(folderName):
			os.mkdir(folderName)
		print("Dernière version : " + lastVersion)
		print("Etape 2/4 : Téléchargement du client")
		buildDlLinks = None
		if platform.system() == "Darwin":
			buildDlLinks = buldDataJson["downloadLinksMacIntel64"]
		elif platform.system() == "Windows":
			buildDlLinks = buldDataJson["downloadLinksWinIntel64"]
		else:
			buildDlLinks = buldDataJson["downloadLinksLinuxIntel64"]
		if (len(buildDlLinks) == 0):
			print("Aucun lien de téléchargement n'a été trouvé, réessayes plus tard")
			return
		sFullLink = ETERNAL_WEBSITE + buildDlLinks[0]
		print("Lien de téléchargement : " + sFullLink)
		print("Lancement du téléchargement, veuillez patienter...")
		zipPathInDisk = os.path.join(folderName, "client.7z")
		if os.path.exists(zipPathInDisk):
			print("Téléchargement annulé : le fichier client.7z existe déjà !")
		else:
			wget.download(sFullLink, out=zipPathInDisk)
		print("\nEtape 3/4 : Déterminer la clé")
		nonRemasteredHash = "49540452afd0c11afeb50fa79051ee35c6be0f998e9374a9b80196b0035fbd5d"
		remasteredHash = "a139bb7420edf6664efabdb1829d0c6d776568a76b7e3c0e30dd33b7ea6c04f9"
		toHash = nonRemasteredHash + remasteredHash + keyPartToHash
		zipPassword = sha256(toHash.encode('utf-8')).hexdigest()
		print("Clé de déchiffrement : " + zipPassword)
		print("Etape 4/4 : Décompression du client")
		destinationPath = os.path.join(folderName, "out")
		if os.path.exists(destinationPath):
			print("Décompression annulée : le dossier out existe déjà !")
		else:
			archive =  py7zr.SevenZipFile(zipPathInDisk, mode='r', password=zipPassword)
			archive.extractall(path=destinationPath)
			archive.close()
			print("Mise à jour terminée, ouverture de l'exploreur...")
			show_in_file_manager(destinationPath)

def main():
	sPlatform = platform.system()
	if sPlatform != "Darwin" and sPlatform != "Windows" and sPlatform != "Linux":
		print("Le système d'exploitation n'a pas pu être déterminé. Arrêt du programme.")
		return
	downloadRetro()

printHeader()
main()