#===========================================================
#      ----Installation des données supplémentaires----
#===========================================================
#Ici, on s'occupe de l'installation des mods, des fichiers configs pré-configurés
#et des interfaces graphiques personalisés.



#Importation des modules
import wget
from zipfile import ZipFile
import os

#import hashlib
#def md5(file1):
#    md5h = hashlib.md5()
#    with open(file1, "rb") as f:
#        for chunk in iter(lambda: f.read(4096), b""):
#            md5h.update(chunk)
#    return md5h.hexdigest()

#Chemin de l'url pour le téléchargement
url = "http://185.171.202.142/minecraft/pylauncher/Empisurvie/archive.zip"

#Appdata
appdataDir = os.getenv('APPDATA')
#Répertoires d'installation et d'extraction
download_directory = appdataDir + "\PyLaunchr\Downloads"
minecraft_directory = appdataDir + "\PyLaunchr\Empisurvie"

#Téléchargement des fichiers
wget.download(url, download_directory)

#Chemin d'accès du fichier téléchargé
file = download_directory + "\\archive.zip"

#Extraction du fichier .zip en mode lecture (r=read)
with ZipFile(file, 'r') as zip: 
    #Afficher tout le contenu du .zip dans la console
    zip.printdir()

    #Extraire les fichiers
    print('extraction...')
    zip.extractall(minecraft_directory)
    print('Terminé!')


