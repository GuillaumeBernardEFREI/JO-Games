import pygame.event

from Constantes import *
import math

pygame.init()
clock = pygame.time.Clock()

while running:


    if game_statement == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pour fermer le programme
                running = False
        keys = pygame.key.get_pressed()
        # Les touches :
        if keys[pygame.K_ESCAPE]:
            running = False  # Pour fermer programme

        skin_P1 = 0     #défini le skin de base
        skin_P2 = 0

        Window.blit(pygame.transform.scale(BG_2, Window.get_size()), [0, 0])
        Window.blit(anneaux, [400, 300])
        Window.blit(titre, [230, 150])

        if keys[pygame.K_SPACE]:
            game_statement = 1
            pygame.event.wait(6000)









    elif game_statement == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pour fermer le programme
                running = False
        keys = pygame.key.get_pressed()
        # Les touches :
        if keys[pygame.K_ESCAPE]:
            running = False  # Pour fermer programme


        Window.blit(pygame.transform.scale(BG_3, Window.get_size()), [0, 0])
        Window.blit(texte, [30, 20])
        Window.blit(P_1, [290, 150])
        Window.blit(P_2, [980, 153])

        if keys[pygame.K_SPACE] :
            game_statement = 2
            pygame.event.wait(6000)


        #Selection skin Joueur 1
        if keys[pygame.K_q]:
            skin_P1 -= 1

        if keys[pygame.K_d]:
            skin_P1 += 1

        # Selection skin Joueur 2
        if keys[pygame.K_LEFT]:
            skin_P1 -= 1

        if keys[pygame.K_RIGHT]:
            skin_P1 += 1


        if skin_P1 == 0:
            P1 = P1_clean
        elif skin_P1 == 1:
            P1 = P1_band
        elif skin_P1 == 2
            P1 = P1_spider

        if skin_P2 == 0:
            P2 = P2_clean
        elif skin_P2 == 1:
            P2 = P2_band
        elif skin_P2 == 2:
            P2 = P2_spider


        Window.blit(P1, [200, 250])
        Window.blit(P2, [900, 253])











    elif game_statement == 2:
        Window.blit(pygame.transform.scale(BG_1,Window.get_size()), [0, 0])  # Ouvre une fenêtre de jeu avec un arière plan défini, ici, c est fond
        rotation_center1 = (pos_y1 + 88, pos_x1 + 93)
        rotation_center2 = (pos_y2 + 33, pos_x2 + 93)
        rotation_center3 = (pos_y3 + 24, pos_x3 + 24)

        previous_x3 = pos_x3
        previous_y3 = pos_y3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pour fermer le programme
                running = False
        keys = pygame.key.get_pressed()
        # Les touches :
        if keys[pygame.K_ESCAPE]:
           running = False  # Pour fermer programme
        if keys[pygame.K_m]:
           game_statement = 0  # Pour fermer programme

    # ************** Déplacement / Coup dans volant **************

    # Player 1
        if keys[pygame.K_z] and not en_saut1:
            en_saut1 = True
            vitesse_x1 = Saut_Force

        if keys[pygame.K_q]:
            pos_y1 -= walk_speed

        if keys[pygame.K_s] and not rotation_in_progress1:
            rotation_in_progress1 = True

        if keys[pygame.K_d]:
            pos_y1 += walk_speed


    # Player 2
        if keys[pygame.K_UP] and not en_saut2 :
            en_saut2 = True
            vitesse_x2 = Saut_Force

        if keys[pygame.K_LEFT]:
            pos_y2 -= walk_speed

        if keys[pygame.K_DOWN] and not rotation_in_progress2:
            rotation_in_progress2 = True

        if keys[pygame.K_RIGHT]:
            pos_y2 += walk_speed


        rotation_in_progress3 = True




    #VOLANNNNT

        if keys[pygame.K_SPACE]:
            Actif = True
            pos_y3, pos_x3 = 360, 540
            en_saut_volant_D = False
            en_saut_volant_G = False
            volant_force = -14.5
            GRAVITE_volant = GRAVITE
            volant_speed = walk_speed * 1.5
            vitesse_x3 = 0
            smash_P2 = False
            smash_P1 = False

        if en_saut_volant_G:
            pos_y3 += volant_speed

        if en_saut_volant_D:
            pos_y3 -= volant_speed


    # Appliquer la Gravité:
        if en_saut1:
            vitesse_x1 += GRAVITE
        if en_saut2:
            vitesse_x2 += GRAVITE
        if en_saut_volant_D or en_saut_volant_G:
            vitesse_x3 += GRAVITE_volant


    # Mettre à jour la position verticale des sprites
        pos_x1 += vitesse_x1
        pos_x2 += vitesse_x2
        pos_x3 += vitesse_x3

    # ****************** Rotations des bras ************************

    # Player 1:
        if rotation_in_progress1 :
            if angle_rotation1 < 120 and test1 != 1:
                angle_rotation1 += rotation_speed
            else:
                angle_rotation1 -= rotation_speed
                test1 = 1
                if angle_rotation1 <= 0:
                    rotation_in_progress1 = False
                    angle_rotation1 = 0
                    test1 = 0

        P1_Arm_rotated = pygame.transform.rotate(P1_Arm, -angle_rotation1)
        rect_rotated1 = P1_Arm_rotated.get_rect(center=rotation_center1)   # Permet de rectifier la rotation en changeant les coordonnées du sprite pour ne pas donner un truc tout goofy

    # Player 2:
        if rotation_in_progress2:
            if angle_rotation2 < 120 and test2 != 1:
                angle_rotation2 += rotation_speed
            else:
                angle_rotation2 -= rotation_speed
                test2 = 1
                if angle_rotation2 <= 0:
                    rotation_in_progress2 = False
                    angle_rotation2 = 0
                    test2 = 0

        P2_Arm_rotated = pygame.transform.rotate(P2_Arm, angle_rotation2)
        rect_rotated2 = P2_Arm_rotated.get_rect(center=rotation_center2)



        # Volant

        if pos_x3 - previous_x3 != 0:
            angle_rotation3 = atan((pos_y3 - previous_y3) / (pos_x3 - previous_x3))
            if angle_rotation3 < 0:
                angle_rotation3 = degrees(angle_rotation3)
            if angle_rotation3 > 0:
                angle_rotation3 = degrees(angle_rotation3) + 180

        volant_rotated = pygame.transform.rotate(volant, angle_rotation3)
        rect_rotated3 = volant_rotated.get_rect(center=rotation_center3)


        # **********************************************************************

    # ************** Limites du terrain ***********
    # Horizontalement
        if pos_y1<130:
            pos_y1=130
        if pos_y1>575:
            pos_y1=575
        if pos_y2<755:
            pos_y2=755
        if pos_y2>1205:
            pos_y2=1205
        if pos_y3<130:
            pos_y3=130
        if pos_y3>1205:
            pos_y3=1205

    # Verticalement
        if pos_x1 >= SOL:
            en_saut1 = False
            pos_x1 = SOL
        if pos_x2 >= SOL:
            en_saut2 = False
            pos_x2 = SOL
        if pos_x3 >= SOL_VOLANT:
            en_saut_volant_G = False
            en_saut_volant_D = False
            pos_x3 = SOL_VOLANT

    # *************** Détection de collision ***************
    # Obtenir les masques de collision pour P1 et P2
        mask_p1 = pygame.mask.from_surface(P1_Arm_rotated)
        mask_p2 = pygame.mask.from_surface(P2_Arm_rotated)
        mask_vol = pygame.mask.from_surface(volant)
        mask_vol_rotated = pygame.mask.from_surface(volant_rotated)

    # Définir les rectangles de collision pour P1 et P2
        rect_p1 = P1_Arm.get_rect(topleft=(pos_y1, pos_x1))
        rect_p2 = P2_Arm.get_rect(topleft=(pos_y2, pos_x2))
        rect_vol = volant.get_rect(topleft=(pos_y3, pos_x3))
        rect_vol_rotated = volant_rotated.get_rect(topleft=(pos_y3, pos_x3))

        if (mask_p1.overlap(mask_vol, (rect_vol.x - rect_p1.x, rect_vol.y - rect_p1.y)) or mask_p1.overlap(mask_vol_rotated, (rect_vol_rotated.x - rect_p1.x, rect_vol_rotated.y - rect_p1.y))) and Actif and rotation_in_progress1 and test1 != 1:
            en_saut_volant_G = True
            en_saut_volant_D = False
            smash_P2 = False
            vitesse_x3 = volant_force

            if not Do_a_flip:
                volant = pygame.transform.flip(volant, False, True)
                Do_a_flip = True

            if en_saut1:
                smash_P1 = True



        if (mask_p2.overlap(mask_vol, (rect_vol.x - rect_p2.x, rect_vol.y - rect_p2.y)) or mask_p2.overlap(mask_vol_rotated, (rect_vol_rotated.x - rect_p2.x, rect_vol_rotated.y - rect_p2.y))) and Actif and rotation_in_progress2 and test2 != 1 :
            en_saut_volant_D = True
            en_saut_volant_G = False
            smash_P1 = False
            vitesse_x3 = volant_force

            if en_saut2:
                smash_P2 = True

            if Do_a_flip:
                volant = pygame.transform.flip(volant, False, True)
                Do_a_flip = False



        if (smash_P2 or smash_P1) and (en_saut_volant_G or en_saut_volant_D):
            volant_force = -5
            volant_speed = walk_speed * 2.8
        else :
            volant_force = - 14.5
            volant_speed = walk_speed * 1.5


        # ****************************************************

        # ************ Dessiner le perso à sa nouvelle position ************

    # Filet au bon endroit
        Window.blit(filet, [700, 550])

    # Player 1
        Window.blit(P1_Body,[pos_y1,pos_x1]) # On déplace P1 à ses nouvelles coordonnées

        if rotation_in_progress1:
            Window.blit(P1_Arm_rotated, rect_rotated1)
        else:
            Window.blit(P1_Arm, [pos_y1,pos_x1])

    # Player 2
        Window.blit(P2_Body, [pos_y2, pos_x2]) # On déplace P2 à ses nouvelles coordonnées

        if rotation_in_progress2:   # Position des bras : on ne passe pas tout le temps dans la boucle de rotation pour limiter le lag
            Window.blit(P2_Arm_rotated, rect_rotated2)
        else:
            Window.blit(P2_Arm, [pos_y2 - 53,pos_x2])

    # Volant
        if Actif:
            if rotation_in_progress3:
                Window.blit(volant_rotated, rect_rotated3)
            else:
                Window.blit(volant, [pos_y3, pos_x3])



#********************************************************



#*************** Modération ***************
#
#   print(f"[{pos_x1:2f},{pos_y2:2f}]")
#
#******************************************



#****** End of while loop *********

    clock.tick(60)
    pygame.display.update()
pygame.quit()