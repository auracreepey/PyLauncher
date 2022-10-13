import wget
from zipfile import ZipFile
import os
from tkinter import messagebox
import colorama
from colorama import Back, Fore, Style

#Version du launcher
LauncherVersion = "1.0.0"


#import hashlib
#def md5(file1):
#    md5h = hashlib.md5()
#    with open(file1, "rb") as f:
#        for chunk in iter(lambda: f.read(4096), b""):
#            md5h.update(chunk)
#    return md5h.hexdigest()

print(Fore.BLUE +"Version du launcher: " + LauncherVersion + Fore.RESET)



#Chemin de l'url
url = "http://185.171.202.142/minecraft/pylauncher/Empisurvie/LauncherUpdate.txt"

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
    print(Fore.GREEN + "Version à jour!" + Fore.RESET)
else:
    print(Fore.RED +"Version obsolete. Nouvelle version disponible: " + LastVersion + Fore.RED)
    messagebox.showerror(title="Version obsolete", message="Une mise à jour du launcher est disponible! (" + LastVersion +
                        "). Veuillez la télécharger pour obtenir les dernières nouveautés et correctifs de bug.")
