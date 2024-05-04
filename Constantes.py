from Vectors import *

# Fichier qui sert à initialiser les variables



# ************** initialisation variables **************
running=True


#Game_statements = 0 - MENU

game_statement = 0













#Game_statements = 2 - Jeu

taille_joueur = (120,190)
taille_bras = (173,190)
taille_volant =(50,50)
pos_x1 = 540
pos_y1 = 360
pos_x2 = 540
pos_y2 = 950
pos_x3 = 540
pos_y3 = 360

previous_x3 = pos_x3
previous_y3 = pos_y3

en_saut1 = False # Variables pour suivre l'état du saut
en_saut2 = False
vitesse_x1 = 0
vitesse_x2 = 0

#Rotation des bras
angle_rotation1 = 0
angle_rotation2 = 0
test1 = 0   # Pour faire l'effet aller retour du coup de raquette
test2 = 0
rotation_speed = 14  # Vitesse de rotation en degrés par frame
rotation_in_progress1 = False # Variable pour suivre l'état de la rotation
rotation_in_progress2 = False
rotation_center1 = (0, 0)  # Centre de rotation, on peut le définir que si on connait la position du sprite, ici on l'initialise simplement
rotation_center2 = (0, 0)
smash_P1 = False
smash_P2 = False
Test_smash = False
Start = False


Saut_Force = -11
GRAVITE = 0.5
GRAVITE_volant = GRAVITE
SOL = 540  # Pour définir un sol: les joueurs ne pourront pas aller en dessous de ces coordonées
walk_speed = 7  # Vitesse des sprites
volant_speed = -walk_speed * 2
SOL_VOLANT = 700

# Variables du volant
Actif = False
timer = 0
en_saut_volant_G = False
en_saut_volant_D = False
vitesse_x3 = 0
volant_force = -10
angle_rotation3 = 0
rotation_center3 = (0,0)
rotation_speed_2 = 14
rotation_in_progress3 = False
test3 = False
Do_a_flip = False


# ***********************   Initialisation des Sprites *******************************




Window = Screen().screen


#Ecran titre
BG_2 = Background(os.path.join("data","Ecran_titre","Fond_menu_2.jpg")).BD
anneaux = General_Game_Object(os.path.join("data","Ecran_titre","Anneaux.png")).sprite
titre = General_Game_Object(os.path.join("data","Ecran_titre","Nom du jeux_3.png")).sprite


#Menu
BG_3 = Background(os.path.join("data","Menu","Fond_3.webp")).BD

texte = General_Game_Object(os.path.join("data","Menu","Character_selection.png")).sprite

P_1 = General_Game_Object(os.path.join("data","Menu","P_1.png")).sprite
#P_1 = pygame.transform.scale(P_1, (50,40))

P_2 = General_Game_Object(os.path.join("data","Menu","P_2.png")).sprite
P_2 = pygame.transform.scale(P_2, (147,90))


Fond_P1= General_Game_Object(os.path.join("data","Jeux","Fond_perso_1.png")).sprite
Fond_P2= General_Game_Object(os.path.join("data","Jeux","Fond_perso_2.png")).sprite

P1_clean = General_Game_Object(os.path.join("data","Skin","Player1_rien.png")).sprite
P1_band = General_Game_Object(os.path.join("data","Skin","Player1.png")).sprite
P1_spider = General_Game_Object(os.path.join("data","Skin","Player1_Spiderman.png")).sprite


P2_clean = General_Game_Object(os.path.join("data","Skin","Player2_rien.png")).sprite
P2_band = General_Game_Object(os.path.join("data","Skin","Player2.png")).sprite
P2_spider = General_Game_Object(os.path.join("data","Skin","Player2_Spiderman.png")).sprite


#Jeux

#Background
BG_1 = Background(os.path.join("data","Jeux","Fond.png")).BD

# Configuration du corps de P1
P1_Body = General_Game_Object(os.path.join("data","Jeux","P1_Body.png")).sprite
P1_Body = pygame.transform.scale(P1_Body, taille_joueur)

P1_Arm = General_Game_Object(os.path.join("data","Jeux","P1_Arm.png")).sprite
P1_Arm = pygame.transform.scale(P1_Arm, taille_bras)


# Configuration du corps de p2
P2_Body = General_Game_Object(os.path.join("data","Jeux","P2_Body.png")).sprite
P2_Body = pygame.transform.scale(P2_Body, taille_joueur)

P2_Arm = General_Game_Object(os.path.join("data","Jeux","P2_Arm.png")).sprite
P2_Arm = pygame.transform.scale(P2_Arm, taille_bras)

# Configuration filet / volant
filet = General_Game_Object(os.path.join("data","Jeux","filet.png")).sprite
volant = General_Game_Object(os.path.join("data","Jeux","Volant2.png")).sprite
volant = pygame.transform.scale(volant, taille_volant)

