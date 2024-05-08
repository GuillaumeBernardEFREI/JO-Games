from Vectors import *

# Fichier qui sert à initialiser les variables



# ************** initialisation variables **************
running=True


#Game_statements = 0 - MENU

game_statement = 0





#Game_statements = 1 - Selection des personnages









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
walk_speed = 9  # Vitesse des sprites #9 de base
volant_speed = 14
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

vitesse_nuage = 0.7

#Pour tout ce qui est defini en fonction de la taille de l'écran :
taille_ecran = (1450, 840)
taille_selection_skin = (240, 380)
#taille_joueur = (120,190)
# ***********************   Initialisation des Sprites *******************************




Window = Screen().screen


#Ecran titre
BG_2 = Background(os.path.join("data","Ecran_titre","Fond_menu_4.png")).BD

anneaux = General_Game_Object(os.path.join("data","Ecran_titre","Anneaux1.png")).sprite
anneaux = pygame.transform.scale(anneaux, taille_ecran)



C1 = General_Game_Object(os.path.join("data","Ecran_titre","Cloud1.png")).sprite
C1 = pygame.transform.scale(C1, taille_ecran)
C1_x = 0
C1_y = 0


C2 = General_Game_Object(os.path.join("data","Ecran_titre","Cloud2.png")).sprite
C2 = pygame.transform.scale(C2, taille_ecran)
C2_x = 0
C2_y = 0


C3 = General_Game_Object(os.path.join("data","Ecran_titre","Cloud3.png")).sprite
C3 = pygame.transform.scale(C3, taille_ecran)
C3_x = 0
C3_y = 0


C4 = General_Game_Object(os.path.join("data","Ecran_titre","Cloud4.png")).sprite
C4 = pygame.transform.scale(C4, taille_ecran)
C4_x = 0
C4_y = 0


C5 = General_Game_Object(os.path.join("data","Ecran_titre","Cloud5.png")).sprite
C5 = pygame.transform.scale(C5, taille_ecran)
C5_x = 0
C5_y = 0


C6 = General_Game_Object(os.path.join("data","Ecran_titre","Cloud6.png")).sprite
C6 = pygame.transform.scale(C6, taille_ecran)
C6_x = 0
C6_y = 0


#Menu
BG_3 = Background(os.path.join("data","Menu","New_Background.png")).BD

P1_Fond_Waiting = General_Game_Object(os.path.join("data","Menu","P1_Waiting.png")).sprite
P1_Fond_Waiting = pygame.transform.scale(P1_Fond_Waiting, taille_ecran)

P1_Fond_Ready = General_Game_Object(os.path.join("data","Menu","P1_Ready.png")).sprite
P1_Fond_Ready = pygame.transform.scale(P1_Fond_Ready, taille_ecran)

P1_Fond_Question = General_Game_Object(os.path.join("data","Menu","ValidationP1.png")).sprite
P1_Fond_Question = pygame.transform.scale(P1_Fond_Question, taille_ecran)


P2_Fond_Waiting = General_Game_Object(os.path.join("data","Menu","P2_Waiting.png")).sprite
P2_Fond_Waiting = pygame.transform.scale(P2_Fond_Waiting, taille_ecran)

P2_Fond_Ready = General_Game_Object(os.path.join("data","Menu","P2_Ready.png")).sprite
P2_Fond_Ready = pygame.transform.scale(P2_Fond_Ready, taille_ecran)

P2_Fond_Question = General_Game_Object(os.path.join("data","Menu","ValidationP2.png")).sprite
P2_Fond_Question = pygame.transform.scale(P2_Fond_Question, taille_ecran)

Valid_P1 = General_Game_Object(os.path.join("data","Menu","Ready.png")).sprite
Valid_P2 = Valid_P1

Tuto = General_Game_Object(os.path.join("data","Menu","Tuto.png")).sprite

Boutons = General_Game_Object(os.path.join("data","Menu","boutons.png")).sprite

ready_P2 = False #Permet de savoir si le joueur à choisi son skin
ready_P1 = False
connected_1 = False #Permet de faire un écran ou il faut enfoncer 2 touches pour se connecter
connected_2 = False

repeat_1 = True #Permet de empecher le spam dans le menu des skins + éviter que la boucle pour attendre se répète
repeat_2 = True

#Les differents skins

P_clean = General_Game_Object(os.path.join("data","Skin","Menu","Player1_rien.png")).sprite
P_clean = pygame.transform.scale(P_clean, taille_selection_skin)

P_band = General_Game_Object(os.path.join("data","Skin","Menu","Player1.png")).sprite
P_band = pygame.transform.scale(P_band, taille_selection_skin)

P_spider = General_Game_Object(os.path.join("data","Skin","Menu","Player1_Spiderman.png")).sprite
P_spider = pygame.transform.scale(P_spider, taille_selection_skin)


#Tout les drapeaux

flag_time_animation = 5
ctn_flag = 0
flag_state = 0


Flags_Fr = [General_Game_Object(os.path.join("data","Menu","Drapeau","France","1.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","France","2.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","France","3.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","France","4.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","France","5.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","France","6.png")).sprite]

Flags_Allm = [General_Game_Object(os.path.join("data","Menu","Drapeau","Allemagne","1.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Allemagne","2.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","Allemagne","3.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Allemagne","4.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","Allemagne","5.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Allemagne","6.png")).sprite]

Flags_It = [General_Game_Object(os.path.join("data","Menu","Drapeau","Italy","1.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Italy","2.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","Italy","3.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Italy","4.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","Italy","5.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Italy","6.png")).sprite]

Flags_Es = [General_Game_Object(os.path.join("data","Menu","Drapeau","Espagne","1.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Espagne","2.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","Espagne","3.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Espagne","4.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","Espagne","5.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Espagne","6.png")).sprite]

Flags_En = [General_Game_Object(os.path.join("data","Menu","Drapeau","Anglais","1.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Anglais","2.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","Anglais","3.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Anglais","4.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","Anglais","5.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","Anglais","6.png")).sprite]

Flags_Us = [General_Game_Object(os.path.join("data","Menu","Drapeau","USA","1.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","USA","2.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","USA","3.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","USA","4.png")).sprite,
General_Game_Object(os.path.join("data","Menu","Drapeau","USA","5.png")).sprite, General_Game_Object(os.path.join("data","Menu","Drapeau","USA","6.png")).sprite]


#pox_x_temp = [200, 250]
#pos_y_temp = [900, 253] #utilisé pour déterminer la position des perso lorsqu'on les affiches dans les cases

pos_x_temp = 0
pos_y_temp = 0

#Jeux

score_P1 = 0
score_P2 = 0
wait_before_new_point = 0
respawn_P1 = True
respawn_P2 = False
score = True #permet d'attendre un peu avant de faire respawn le volant tout en empechant d'avoir trop de point généré d'un coup
Service_P1 = True #initialiste la condition d'affichage du sprite service
Service_P2 = False


#Background
BG_1 = Background(os.path.join("data","Jeux","Fond_final.png")).BD
Flag_pole = General_Game_Object(os.path.join("data","Jeux","Flag_pole.png")).sprite
Flag_pole = pygame.transform.scale(Flag_pole, taille_ecran)


# Configuration du corps de P1
P1_Body = General_Game_Object(os.path.join("data","Skin","Jeux","P1_Body.png")).sprite
P1_Body = pygame.transform.scale(P1_Body, taille_joueur)

P1_Arm = General_Game_Object(os.path.join("data","Skin","Jeux","P1_Arm.png")).sprite
P1_Arm = pygame.transform.scale(P1_Arm, taille_bras)


# Configuration du corps de p2
P2_Body = General_Game_Object(os.path.join("data","Skin","Jeux","P2_Body.png")).sprite
P2_Body = pygame.transform.scale(P2_Body, taille_joueur)

P2_Arm = General_Game_Object(os.path.join("data","Skin","Jeux","P2_Arm.png")).sprite
P2_Arm = pygame.transform.scale(P2_Arm, taille_bras)

# Configuration filet / volant
filet = General_Game_Object(os.path.join("data","Jeux","filet.png")).sprite
volant = General_Game_Object(os.path.join("data","Jeux","Volant2.png")).sprite
volant = pygame.transform.scale(volant, taille_volant)

#Petite icône de service
service = General_Game_Object(os.path.join("data","Jeux","Service.png")).sprite

