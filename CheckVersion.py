#===========================================================
#                ----Vérifications----
#===========================================================
#Ici, on vérifie que le client est connecté à internet, puis on cherche les mises à jour


#Activation des logs
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="launcher.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

#---Importation des modules---
#wget est utilisé pour télécharger des fichiers
import wget

#ZipFile permet d'extraire des fichiers .zip
from zipfile import ZipFile

import os
from tkinter import messagebox
import sys
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)
from colorama import Back, Fore, Style

#requests est utilisé pour vérifier la connexion internet
import requests


#===========================================================
#      ----Vérification de la connexion internet----
#===========================================================
#Ici on vérifie que l'utilisateur est connecté à internet

logging.info("Tentative de connexion aux serveurs...")
print(Fore.BLUE + "Chargement du Launcher..." + Fore.RESET)

url = "https://www.google.fr/"
timeout = 5
try:
  request = requests.get(url, timeout=timeout)
  logging.info("Client en ligne")
except (requests.ConnectionError, requests.Timeout) as exception:
  print(Fore.RED + "Aucune connexion internet" + Fore.RESET)
  logging.info("Erreur: Le client n'est pas connecté à internet, ou Google est dead\nArrêt du launcher.")
  messagebox.showerror(title="Connxion à internet requise", message="Il semblerait que vous ne soyez pas connecté à internet.\n" + 
  "Une connexion à internet est requise pour lancer le launcher, vérifiez votre connexion et réessayez.")
  sys.exit()

#Maintenant on vérifie que le serveur est en ligne
url = "http://185.171.202.142/minecraft"
timeout = 5
try:
  request = requests.get(url, timeout=timeout)
  logging.info("Serveur en ligne!")
except (requests.ConnectionError, requests.Timeout) as exception:
  logging.CRITICAL("Erreur: Le serveur est down. Arret du launcher.")

  print(Fore.RED + "Erreur: Le serveur est down" + 
  "\nNote: Vu que le serveur n'est pas disponible, toutes les opérations vont echouer et le launcher ne va fonctionner correctement.\nArret du launcher." + Fore.RESET)

  messagebox.showerror(title="Serveur injoignable", message="Le serveur est injoignable.\n" + 
  "Peut-être qu'il est en cours de maintenance, ou qu'une mise à jour du launcher est nécéssaire\n" +
  "Note: Le wifi du lycée bloque l'ip du serveur")
  sys.exit()

#===========================================================
#          ----Recherche des mises à jours----
#===========================================================
#Version du launcher
LauncherVersion = "1.0.0"


#import hashlib
#def md5(file1):
#    md5h = hashlib.md5()
#    with open(file1, "rb") as f:
#        for chunk in iter(lambda: f.read(4096), b""):
#            md5h.update(chunk)
#    return md5h.hexdigest()

print(Fore.BLUE +"Version du launcher: " + LauncherVersion )



#Chemin de l'url
url = "http://185.171.202.142/minecraft/launchers/pylauncher/Empisurvie/LauncherUpdate.txt"

#Appdata
appdataDir = os.getenv('APPDATA')
download_directory = appdataDir + "\PyLaunchr\Empisurvie"
minecraft_directory = appdataDir + "\PyLaunchr\Empisurvie"


#Supprime le fichier de la vesrsion cible si il existe
if os.path.exists(appdataDir + "\PyLaunchr\Empisurvie\LauncherUpdate.txt"):
  os.remove(appdataDir + "\PyLaunchr\Empisurvie\LauncherUpdate.txt")


#Téléchargement du fichier de la version cible
wget.download(url, download_directory)

#Répertoire de destination
file = download_directory + "\\LauncherUpdate.txt"

#Ouverture du fichier installé pour le comparer à la version locale
LatestVersionFile = open(appdataDir + "\PyLaunchr\Empisurvie\LauncherUpdate.txt", "rt")
LastVersion=LatestVersionFile.read()
print(LatestVersionFile.read())
LatestVersionFile.close()

#Affichage du résultat
if LastVersion == LauncherVersion:
    logging.info("Version à jour!" )
else:
    logging.info(Fore.RED +"Version obsolete. Nouvelle version disponible: " + LastVersion + Fore.RED)
    messagebox.showerror(title="Version obsolete", message="Une mise à jour du launcher est disponible! (" + LastVersion +
                        "). Veuillez la télécharger pour obtenir les dernières nouveautés et correctifs de bug.")
