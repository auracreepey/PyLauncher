#===========================================================
#      ----Installation des données supplémentaires----
#===========================================================
#Ici, on s'occupe de l'installation des mods, des fichiers configs pré-configurés
#et des interfaces graphiques personalisés.


#Activation des logs
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="launcher.log",
                    filemode="a",
                    format='[%(asctime)s] [DlMods] - [%(levelname)s] -> %(message)s')

#Importation des modules
import wget
from zipfile import ZipFile
import os
import logging

#import hashlib
#def md5(file1):
#    md5h = hashlib.md5()
#    with open(file1, "rb") as f:
#        for chunk in iter(lambda: f.read(4096), b""):
#            md5h.update(chunk)
#    return md5h.hexdigest()

#Chemin de l'url pour le téléchargement
url = "http://185.171.202.142/minecraft/launchers/pylauncher/Empisurvie/archive.zip"

#Appdata
appdataDir = os.getenv('APPDATA')
#Répertoires d'installation et d'extraction
download_directory = appdataDir + "\PyLaunchr\Downloads"
destination_directory = appdataDir + "\PyLaunchr"

#Téléchargement des fichiers
logging.info('Téléchargement des ressources...')
print(" Ok!")
print("Téléchargement des ressources...")
wget.download(url, download_directory)
logging.info('Téléchargement des ressources terminé')

#Chemin d'accès du fichier téléchargé
file = download_directory + "\\archive.zip"

#Extraction du fichier .zip en mode lecture (r=read)
with ZipFile(file, 'r') as zip:

    #Extraire les fichiers
    logging.info('Extraction...')
    print('Extraction en cours...')
    zip.extractall(destination_directory)
    logging.info('Extraction des ressources terminé!')
    print('Téléchargement terminé !')


