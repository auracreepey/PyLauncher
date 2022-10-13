    #On lance minecraft (Enfin!!!)
    #===========================================================
    #            Gestion et lancement de minecraft
    #===========================================================




#Importation des library
import minecraft_launcher_lib
import sys
import subprocess
from tkinter import *
import os



#---Paramètres---#

#Repertoire du jeu
appdataDir = os.getenv('APPDATA')
minecraft_directory = appdataDir + "\PyLaunchr\Empisurvie"

#Version du jeu de base (vanilla)
mcversion = "1.12.2"

#Version du jeu utilisé
#Tips: Lorsque le launcher à correctement installé une version du jeu, l'id de version est affiché dans les
#logs juste avant le lancement du jeu.
#exemples:
#pour forge en 1.12.2: launch_version_id = "1.12.2-forge-14.23.5.2860"
#en vanilla 1.12.2: launch_version_id = "1.12.2"
launch_version_id = "1.12.2-forge-14.23.5.2860"

#Allocution de ram pour java
ram = "3"

#---Installation du jeu---#

print("Version de minecraft: " + mcversion)




#Lancement du jeu
print("Préparation du lancement du jeu")

#Ouverture du fichier username
usernameFile = open("username.txt", "rt")
username=usernameFile.read()
print(usernameFile.read())
usernameFile.close()

#Données sur l'utilisateur (requis pour le lancement du jeu)
print("Assemblage des options de lancement java et données du joueur")
options = { 
    #nom d'utilisateur
    "username": username,
    #jeton variable selon l'utilisateur
    "uuid": "pylauchr1"+username,
    #le nom d'utilisateur et l'uuid étant publics, le token est utilisé pour se connecter
    "token": "",
    #Arguments java
    "jvmArguments": ["-Xmx2G", "-Xms2G"]
}


#On cherche l'id de la version car forge modifie l'id de la version
#L'id de la version est affiché ici à titre indicatif, il faut la copier manuellement à la ligne 18
#Il devrait y avoir un moyen de faire ça automatiquement, mais j'ai un peu la flemme x)
print("Recherche de l'id de version...")
print("PS: Voir l'id de version pour jouer en modée")
version_id = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
print("ID DE VERSION")
print(version_id)

#Commande de lancement du jeu
print("Génération de la commande de lancement du jeu")

minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("1.12.2-forge-14.23.5.2860", minecraft_directory, options)



print("---Commande de lancement du jeu---")
print(minecraft_command)
print("----------------------------------")

#Lancement du jeu
print("Lancement du jeu")
subprocess.call(minecraft_command)