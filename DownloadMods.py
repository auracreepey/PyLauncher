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

#Chemin de l'url
url = "http://185.171.202.142/minecraft/pylauncher/Empisurvie/archive.zip"

#Appdata
appdataDir = os.getenv('APPDATA')
#Répertoires d'installation et d'extraction
download_directory = appdataDir + "\PyLaunchr\Downloads"
minecraft_directory = appdataDir + "\PyLaunchr\Empisurvie"

#Téléchargement
wget.download(url, download_directory)

# spécifiant le nom du fichier zip
file = download_directory + "\\archive.zip"

# ouvrir le fichier zip en mode lecture
with ZipFile(file, 'r') as zip: 
    # afficher tout le contenu du fichier zip
    zip.printdir()

    # extraire tous les fichiers
    print('extraction...')
    zip.extractall(minecraft_directory)
    print('Terminé!')


