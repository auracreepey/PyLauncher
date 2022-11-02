#===========================================================
#            Gestion et lancement de minecraft
#===========================================================


#Activation des logs
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="launcher.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

#Importation des modules
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

#Allocution de ram par défaut pour java
ram = "2"

logging.info("Version de minecraft: " + mcversion)



logging.info("Préparation du lancement du jeu")

#Recherche du nom d'utilisateur du joueur
usernameFile = open("username.txt", "rt")
username=usernameFile.read()
print(usernameFile.read())
usernameFile.close()

#Recherche de l'allocution de ram
ramFile = open("ram.txt", "rt")
ram=ramFile.read()
logging.info("Ram:")
logging.info(ramFile.read())
ramFile.close()

#Données sur l'utilisateur (requis pour le lancement du jeu)
logging.info("Assemblage des options de lancement java et données du joueur")
options = { 
    #nom d'utilisateur
    "username": username,
    #jeton variable selon l'utilisateur
    "uuid": "pylauchr1"+username,
    #le nom d'utilisateur et l'uuid étant publics, le token est utilisé pour se connecter
    "token": "",
    #Arguments java (quand j'aurais le temps il faudra que je modifie cette ligne)
    "jvmArguments": ["-Xmx2G", "-Xms2G"]
}


#On cherche l'id de la version car forge modifie l'id de la version
#L'id de la version est affiché ici à titre indicatif, il faut la copier manuellement à la ligne 18
#Il devrait y avoir un moyen de faire ça automatiquement, mais j'ai un peu la flemme x)
logging.info("Recherche de l'id de version...")
logging.info("PS: Voir l'id de version pour jouer en modée")
version_id = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
logging.info("ID DE VERSION:")
logging.info(version_id)

#Commande de lancement du jeu
logging.info("Génération de la commande de lancement du jeu")

minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("1.12.2-forge-14.23.5.2860", minecraft_directory, options)

logging.info("---Commande de lancement du jeu---")
logging.info(minecraft_command)
logging.info("----------------------------------")


#On lance minecraft (Enfin!!!)
logging.info("Lancement du jeu...")
print("Lancement du jeu...")
print(" ")
print("-----------Console-----------")
subprocess.call(minecraft_command)