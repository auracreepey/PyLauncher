#=========================
#-----EmpiLauncher Py-----
#-----Par aura_creeper----
#=========================

#Version du jeu de base (vanilla)
#Pour changer la version du jeu, il faut aussi modifier la valeur de "mcversion" dans LaunchForge.py
mcversion = "1.12.2"


#===========================================================
#                ----Pré Initialisation----
#===========================================================
#Activation des logs

#os permet de réaliser des actions sur l'ordinateur (ex: copier/coller des fichiers)
import os

#On supprime les logs précédents du launcher si il y en a
if os.path.exists("launcher.log"):
    os.remove("launcher.log")

#Paramètrage et activation des logs
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="launcher.log",
                    filemode="a",
                    format='[%(asctime)s] - [%(levelname)s] -> %(message)s')

#logging() enregistre des infos utiles dans le fichier launcher.log
#Cela permet de savoir ce que fait le launcher
#Ca peut servir pour localiser et résoudre des bugs
logging.info("----------------------------------")
logging.info("----Empisurvie Python Launcher----")
logging.info("----------------------------------")
logging.info("            {]Logs[}")

#Ici on affiche des infos sur la console du launcher
print("----------------------------------")
print("----Empisurvie Python Launcher----")
print("----------------------------------")
print("            Console")
print(".")
print("Les actions effectués par le launcher sont affichés ici!")




#===========================================================
#                  ----Initialisation----
#===========================================================
#Imporation des modules, vérification de la connexion internet et
#des mises à jours....

#----Initialisation des modules----

logging.info("Importation des libs...")

#colorama permet d'afficher des couleurs dans la console
import colorama
from colorama import Back, Fore, Style


#Initialisation des couleurs de la console
colorama.init(autoreset=True)
logging.info("[Libs] Colorama OK")


#tkinter permet de créer des interfaces graphiques
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
logging.info("[Libs] Tkinter OK")

#wget permet de télécharger des fichiers
import wget
logging.info("[Libs] WGET OK")

#PIL permet de manipuler des images. Ici je l'utilise pour afficher des images avec tkinter
from PIL import ImageTk, Image
logging.info("[Libs] PIL OK")

#re est utilisé lors de la création du nom d'utilisateur
import re
logging.info("[Libs] re OK")


#----Vérifiaction des fichiers et de la version installé----

#Répertoire d'installation des fichiers
appdataDir = os.getenv('APPDATA')
minecraft_directory = appdataDir + "\PyLaunchr\Empisurvie"
logging.info("Répertoire de minecraft: " + minecraft_directory)

#On vérifie la présence du répertoire d'installation
#Si il n'existe pas, on le créé.
if os.path.exists(appdataDir + "\PyLaunchr\Empisurvie"):
    logging.info("Répertoire du jeu trouvé")
else:
    logging.info("Répertoire du jeu absent")
    os.makedirs(minecraft_directory)

#Pareil pour le répertoire "Downloads"...
if os.path.exists(appdataDir + "\PyLaunchr\Downloads"):
    logging.info("Répertoire de téléchargement trouvé")
else:
    logging.info("Répertoire de téléchargement absent, création...")
    os.makedirs(appdataDir + "\PyLaunchr\Downloads")


#Vérification de la version du launcher
logging.info("Lancement de la recherche des mises à jour...")
import CheckVersion


#Ici, on cherche le fichier username.txt
#Si il n'existe pas, le joueur lance le launcher pour la première fois.
if os.path.exists("username.txt") and os.path.exists(appdataDir + "\PyLaunchr\Downloads"):
    logging.info("[Initialisation] Fichiers requis trouvés")
    FirstInit = 0
else:
    logging.warning("[Initialisation] Fichiers requis absents, affichage du message de bienvenu.")
    #Message de bienvenu
    messagebox.showinfo(title="Bienvenu sur Empilauncher Python🚀, conçu par aura_creeper!!", message="Pour jouer, tu doit créer un nom d'utilisateur." + 
    ' Met le dans la case pseudo, puis clique sur "Sign Up Now"!')

    FirstInit = 1
    #Le fichier username.txt est créé plus tard, une fois que la fenêtre principale est chargé.

logging.info("[Initialisation] Création de la fenêtre principale")


#===========================================================
#  ----Affichage et scripts de la fenêtre du launcher----
#===========================================================
#Tout ce qui est visible par l'utilisateur est créé ici!

#Inspiré de Sen Gideons https://www.youtube.com/watch?v=gOtzf-Yhn-k
class LoginPage:
    def __init__(self, window):

        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Empilauncher🐍')

        #Image d'arrière plan
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        #Login Frame
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        #Nom de la fenêtre principale
        self.txt = "EMPILAUNCHER Py"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        #Image à gauche
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        #Sign in image
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=590, y=130)

        #Sign in label
        self.sign_in_label = Label(self.lgn_frame, text="Connexion", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        #Username input
        self.username_label = Label(self.lgn_frame, text="Pseudo", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        #Ici, on cherche le fichier username.txt pour afficher automatiquement le nom d'utilisateur
        #Si le fichier n'existe pas, il est automatiquement créé.
        if os.path.exists("username.txt"):
            #On crée la variable self.defaultuser
            #Créer cette variable en avance permet d'éviter des erreurs
            self.defaultuser=StringVar()

            #On ouvre le fichier en mode lecture (r), et type texte (t)
            self.usernameFile = open("username.txt", "rt")

            #On met le contenu du fichier dans la variable self.defaultuser
            self.defaultuser.set(self.usernameFile.read())

            #Et on ferme le fichier pour éviter les problèmes x)
            self.usernameFile.close()
        else:
            logging.warning("Le fichier username.txt n'existe pas")
            self.defaultuser=StringVar()
            self.defaultuser.set("Met ton pseudo ici!")
            self.usernameFile = open("username.txt", "w")

            #On met la valeur NotSet! pour qu'on sache que le joueur n'a pas encore choisi son nom d'utilisateur
            self.usernameFile.write("NotSet!")

            FirstInit = 1

            self.usernameFile.close()

        #Si le nom d'utilisateur à été défini, on bloque la modification.
        self.usernameFile = open("username.txt", "rt")
        self.username=self.usernameFile.read()
        self.usernameFile.close()

        if self.username=="NotSet!":
            self.username_entry = Entry(self.lgn_frame, textvariable=self.defaultuser, highlightthickness=0, relief=FLAT, bg="#040405", fg="#BFBFBE",
                                        font=("yu gothic ui ", 12, "bold"))
        else:
            self.username_entry = Entry(self.lgn_frame, state='disabled', textvariable=self.defaultuser, highlightthickness=0, relief=FLAT, bg="#040405", fg="#BFBFBE",
                                        font=("yu gothic ui ", 12, "bold"))
        #La variable "self.username_entry" contient le contenu de l'input "nom d'utilisateur"
        #On ne peut pas la réutiliser tel quel, donc on emballe la variable avec .pack()
        self.username_entry.pack()
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        
        #Username icon
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        #Login button
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, command=self.login, text='JOUER', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)

        #Mot de passe oublié
        self.forgot_button = Button(self.lgn_frame, text="Bienvenu sur Empisurvie!",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)

        #Nouveau compte
        self.sign_label = Label(self.lgn_frame, text='Pas de compte?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, command=self.newuser, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        #Création d'une variable pour l'allocution de ram
        ramvalue=IntVar()

        #Quantité de ram par défaut
        ramvalue.set(3)

        self.ramSpinbox=IntVar()

        #Input pour la quantité de ram
        self.ramSpinbox = Spinbox(window, from_=2, to=6, width=10, highlightthickness=0, relief=FLAT, bg="#040405", fg="#BFBFBE", textvariable=ramvalue,
                            command=self.SetRam, font=("yu gothic ui", 12, "bold"))
        self.ramSpinbox.place(x=800, y=485)

        #Texte au dessus de l'input
        self.password_label = Label(self.lgn_frame, text="Allocution de RAM (En Go)", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        #Ligne en dessous de l'input
        self.password_line = Canvas(self.lgn_frame, width=155, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        #Password icon
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)


        #----Barre de progression----
        self.progressbar_label = Label(self.lgn_frame, text="Progression:", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.progressbar_label.place(x=50, y=570)

        self.progressbar = Progressbar(window, length=200)
        self.progressbar.place(x=350, y=645)

    #----Création d'un compte----
    #Si un compte est déjà existant, il sera remplacé
    #Cette partie est celle qui m'a pris le plus de temps à faire de tout le launcher x)
    def newuser(self):
        logging.info("[Auth] Création d'un nouveau compte")

        #self.username_entry correspond a l'input "nom d'utilisateur"
        #On peut obtenir le contenu de cette variable grace à pack()
        #Cf. plus haut
        #Pour ne pas modifier le contenu de l'input, on va copier son contenu sur une autre variable
        self.username = self.username_entry.get()


        #Maintenant on vérifie si le nom d'utilisateur correspond aux critères
        #Le nom d'utilisateur doit être compris entre 4 et 15 caractères
        #On utilise len() pour calculer le nombre de caractère.
        #Le résultat est stocké dans la variable self.username
        self.usernameScale = len(self.username)


        if self.usernameScale <= 15 and self.usernameScale >= 4:

            #Maintenant, on vérifie que le nom d'utilisateur ne contient pas des caractères qui
            #posent problèmes (espace, %, !, etc...)
            if re.match("^[a-zA-Z0-9_]*$", self.username):
                logging.info("[AuthCreate] Nom d'utilisateur valide")
                logging.info("[AuthCreate] Nouveau nom d'utilisateur : " + self.username)
                logging.info("[AuthCreate] Ecriture du nom d'utilisateur")
                messagebox.showinfo(title="Création réussi", message="Bienvenu " + self.username + "!")
                messagebox.showinfo(title="Création réussi", message="Votre compte est mainenant créé. Cliquez sur jouer pour commencer le téléchargement du jeu." + 
                                    " Vous devrez créer un mot de passe lors de la première connexion au serveur.")

                #Si tout est OK, on ouvre le fichier username.txt en mode overwrite ("w")
                f = open("username.txt", "w")

                #On écrit le nouveau nom d'utilisateur dans le fichier
                f.write(str(self.username))

                #Puis on ferme le fichier pour éviter les problèmes
                f.close()
            else:
                #La fonction messagebox permet d'afficher une fenêtre en plus avec des informations
                messagebox.showerror(title="Erreur", message="Votre identifiant contient des caractères invalides!")
                logging.error("[AuthCreate] Création échoué: Contient des caractères invalides!")

        else:
            logging.error("[AuthCreate] Création échoué: Trop ou pas assez de caractères!")
            messagebox.showerror(title="Error", message="Votre identifiant est trop court/long!")

    def SetRam(self):
        self.ramSet = self.ramSpinbox.get()
        
        if os.path.exists("ram.txt"):
            logging.info("[RamCheck] Fichier ram.txt trouvé")
        else:
            logging.warning("[RamCheck] Fichier ram.txt absent, création...")
            self.ramFile = open("ram.txt", "w")
            self.ramFile.close()
        
        self.ramFile = open("ram.txt", "w")
        self.ramFile.write(str(self.ramSet))
        self.ramFile.close()

        logging.info("Valeur de la ram modifié. Nouvelle valeur:")
        logging.info(self.ramSet)



    def login(self):

        self.userEntry = self.username_entry.get()



        #open and read the file after the appending:
        self.usernameFile = open("username.txt", "rt")

        self.username=self.usernameFile.read()


        self.usernameFile.close()
        
        if self.username=="NotSet!":
            messagebox.showerror(title="Erreur", message="Pour jouer, vous devez créer un identifiant!")
            logging.error("[AuthError] Autentification échoué: le joueur n'a pas encore créé son nom d'utilisateur!")

        else:
            if self.username==self.userEntry:
                messagebox.showinfo(title="Login Success", message="Vous êtes connecté, lancement du jeu...")
                logging.info("[Auth] Autentification réussi")

                #Si le joueur lance le launcher pour la première fois, on installe le jeu
                #Sinon on ignore cette étape
                #Note: Cette étape fait freeze le launcher.
                if os.path.exists(appdataDir + "\\PyLaunchr\\Empisurvie\\assets") and os.path.exists(appdataDir + "\PyLaunchr\Empisurvie\libraries") and os.path.exists(appdataDir + "\PyLaunchr\Empisurvie\mods"):
                    logging.info("[MainInstaller] Installation du jeu ignoré, normalement les fichiers requis sont déjà installés, lancement du jeu...")
                else:
                    messagebox.showinfo(title="Installation requise", message="Minecraft n'est pas encore installé. " + 
                    "Le launcher va se charger d'installer le jeu, la fenêtre du launcher va frezze pendant l'opération. " + 
                    "Vous pourrez suivre l'avancement de l'installation dans les logs.")
                    logging.info("[MainInstaller] Initialisation de l'installation")
                    self.installGame()
                    
                logging.info("[Initalisation] initialisation du jeu")

                #Destruction de la fenêtre
                self.window.destroy()
                
                self.game()

            else:
                messagebox.showerror(title="Erreur", message="Indentifiant invalide.")
                logging.error("[AuthError] Autentification échoué: Mauvais nom d'utilisateur!")
                logging.error("[AuthError] Nom d'utilisateur entré : " + self.userEntry )
                logging.error("[AuthError] Nom d'utilisateur attendu : " + self.username )
    
    #===========================================================
    #          Installation, et gestion de minecraft
    #===========================================================

    def installGame(self):
        logging.info(Fore.BLUE + "Installation du jeu!")

        logging.info("Répertoire du jeu:")
        logging.info(minecraft_directory)

        import minecraft_launcher_lib

        logging.info("Version de minecraft: " + mcversion)

        forge_version = minecraft_launcher_lib.forge.find_forge_version(mcversion)
        if forge_version is None:
            logging.info("This Minecraft Version is not supported by Forge")
        else:
            logging.info("Version de forge:" + forge_version)

        print("Installation du jeu....")
        # Taken from https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
        def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
            """
            Call in a loop to create terminal progress bar
            @params:
                iteration   - Required  : current iteration (Int)
                total       - Required  : total iterations (Int)
                prefix      - Optional  : prefix string (Str)
                suffix      - Optional  : suffix string (Str)
                decimals    - Optional  : positive number of decimals in percent complete (Int)
                length      - Optional  : character length of bar (Int)
                fill        - Optional  : bar fill character (Str)
                printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
            """
            percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
            filledLength = int(length * iteration // total)
            bar = fill * filledLength + '-' * (length - filledLength)
            print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)

            self.progressbar = percent
            
            # Print New Line on Complete
            if iteration == total:
                print()


        def maximum(max_value, value):
            max_value[0] = value


        def main():
            # lambda doesn't allow setting vars, so we need this little hack
            max_value = [0]

            callback = {
                "setStatus": lambda text: print(text),
                "setProgress": lambda value: printProgressBar(value, max_value[0]),
                "setMax": lambda value: maximum(max_value, value)
            }

            version = mcversion
            directory = minecraft_directory

            minecraft_launcher_lib.install.install_minecraft_version(version, directory, callback=callback)
            minecraft_launcher_lib.forge.install_forge_version(forge_version, minecraft_directory, callback=callback)

        



        if __name__ == "__main__":
            main()
        
    def game(self):
        #Appdata
        appdataDir = os.getenv('APPDATA')
        download_directory = appdataDir + "\PyLaunchr\Downloads"

        #Supprime le fichier de la version cible (du fichier online) si il existe
        if os.path.exists(appdataDir + "\PyLaunchr\Downloads\ArchiveUpdate.txt"):
            os.remove(appdataDir + "\PyLaunchr\Downloads\ArchiveUpdate.txt")
        else:
            import DownloadMods
        
        #Chemin de l'url du fichier en ligne
        url = "http://185.171.202.142/minecraft/launchers/pylauncher/Empisurvie/ArchiveUpdate.txt"
        #Téléchargement du fichier de la version cible
        wget.download(url, download_directory)


        #Ouverture du fichier téléchargé pour le comparer à la version locale
        ArchiveVersionFileOnline = open(appdataDir + "\PyLaunchr\Downloads\ArchiveUpdate.txt", "rt")
        ArchiveVersionOnline=ArchiveVersionFileOnline.read()

        logging.info("Version de la dernière archive disponible:")
        logging.info(ArchiveVersionOnline)
        ArchiveVersionFileOnline.close()

        #Ouverture du fichier installé pour le comparer à la version en ligne
        ArchiveVersionFileLocal = open(appdataDir + "\PyLaunchr\Empisurvie\ArchiveUpdate.txt", "rt")
        ArchiveVersionLocal=ArchiveVersionFileLocal.read()

        logging.info("Version de l'archive actuellement installé:")
        logging.info(ArchiveVersionLocal)
        ArchiveVersionFileLocal.close()

        #Affichage du résultat
        if ArchiveVersionLocal == ArchiveVersionOnline:
            logging.info("[ModsInstaller] Version du pack à jour!")
        else:
            logging.warning("[ModsInstaller] Version du pack obsolete. Nouvelle version disponible: " + ArchiveVersionOnline)
            messagebox.showinfo(title="Mise à jour de l'archive nécéssaire", message="Une mise à jour des ressources est nécéssaire, " + 
                            "le jeu démarrera automatiquement une fois l'installation terminée..." + 
                            "Cette opération prend 1 à 2min")
            import DownloadMods
            
        #Initialisation et lancement du jeu !!
        import LaunchForge



#Lancer l'affichage de la fenêtre et l'executer en boucle
def page():
    window = Tk()
    LoginPage(window)
    #Execute la fenêtre principale en boucle
    #C'est nécésaire pour que les boutons fonctionnent correctement
    window.mainloop()





#Script lié à la fenêtre du launcher
#Doit être toujours placé en dernier
if __name__ == '__main__':
    page()


logging.info("Arret du launcher.")
print(Fore.RED + "[Arrêt du launcher]" + Fore.RESET)
