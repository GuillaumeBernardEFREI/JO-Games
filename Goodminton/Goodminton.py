import pygame.event

from Constantes import *
import math

pygame.init()
clock = pygame.time.Clock()
cloud_font_1 = pygame.font.Font('data/Font/DCC - Cloud.otf', 200)
normal_font = pygame.font.Font('data/Font/Light Stories.otf', 100)
small_font = pygame.font.Font('data/Font/Light Stories.otf', 40)
pixel_font = pygame.font.Font('data/Font/Rémi.ttf', 40)

text_minton_surf = cloud_font_1.render("Goodminton", True, '#96527A')
text_menu = normal_font.render("Select your character", True, '#00353F')
text_waiting = small_font.render("Waiting on :     /", True, '#00353F')
text_P1_waiting = small_font.render("P1", True, '#00353F')
text_P2_waiting = small_font.render("P2", True, '#00353F')
text_proceed = small_font.render("Press < space > to proceed", True, '#00353F')



while running:


    if game_statement == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pour fermer le programme
                running = False
        keys = pygame.key.get_pressed()
        # Les touches :
        if keys[pygame.K_ESCAPE]:
            running = False  # Pour fermer programme

        selection_statement_P1 = 1 #tres important pour reboot le menu et les scores
        flag_P1 = 0
        skin_P1 = 0
        ready_P1 = False
        repeat_1 = True
        score_P1 = 0

        selection_statement_P2 = 1 #same
        flag_P2 = 0
        skin_P2 = 0
        ready_P2 = False
        repeat_2 = True
        score_P2 = 0

        if keys[pygame.K_SPACE]:
            game_statement = 1
            pygame.event.wait(6000)

        if C1_x >= 1111:
            C1_x = -600
        else:
            C1_x += vitesse_nuage

        if C2_x >= 1280:
            C2_x = -600
        else:
            C2_x += vitesse_nuage

        if C3_x >= 1450:
            C3_x = -200
        else:
            C3_x += vitesse_nuage

        if C4_x >= 730:
            C4_x = -950
        else:
            C4_x += vitesse_nuage

        if C5_x >= 600:
            C5_x = -1100
        else:
            C5_x += vitesse_nuage

        if C6_x >= 300:
            C6_x = -1410
        else:
            C6_x += vitesse_nuage


        Window.blit(pygame.transform.scale(BG_2, Window.get_size()), [0, 0])
        Window.blit(anneaux, [0, 0])
        Window.blit(text_minton_surf, [174, 134])
        Window.blit(text_proceed, [547, 779])
        Window.blit(C1, [C1_x, C1_y - 50])
        Window.blit(C2, [C2_x, C2_y - 50])
        Window.blit(C3, [C3_x, C3_y - 50])
        Window.blit(C4, [C4_x, C4_y - 50])
        Window.blit(C5, [C5_x, C5_y - 50])
        Window.blit(C6, [C6_x, C6_y - 50])



    elif game_statement == 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pour fermer le programme
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
           running = False  # Pour fermer programme


        # Menu P1 *************************************
        if selection_statement_P1 == 1:
            connected_1 = False

            if keys[pygame.K_z]:
                selection_statement_P1 = 2
                no_spam_P1_2 = False


        elif selection_statement_P1 == 2:
            connected_1 = True

            if keys[pygame.K_q]:
                flag_P1 -= 1
                pygame.event.wait(300)

            if keys[pygame.K_d]:
                flag_P1 += 1
                pygame.event.wait(300)

            if keys[pygame.K_z] and no_spam_P1_2:
                selection_statement_P1 = 3
                no_spam_P1_3 = False #on dit au programme que l'utilisateur ne va pas pouvoir passer direct au niveau 4
                pygame.event.wait(300)

            if not no_spam_P1_2 and repeat_1:
                repeat_1 = False
                no_spam_P1_2 = True
                pygame.event.wait(300)

        elif selection_statement_P1 == 3:

            if keys[pygame.K_q] and no_spam_P1_3:
                skin_P1 -= 1
                pygame.event.wait(300)

            if keys[pygame.K_d] and no_spam_P1_3:
                skin_P1 += 1
                pygame.event.wait(300)

            if keys[pygame.K_z] and no_spam_P1_3:
                no_spam_P1_4 = False #pareil pour le niveau 4
                selection_statement_P1 = 4
                pygame.event.wait(300)

            if keys[pygame.K_s] and no_spam_P1_3:
                selection_statement_P1 = 2
                pygame.event.wait(300)

            if not keys[pygame.K_s]:
                no_spam_P1_3 = True

        elif selection_statement_P1 == 4:
            ready_P1 = False

            if keys[pygame.K_z] and no_spam_P1_4:
                selection_statement_P1 = 5
                no_spam_P1_4 = False
                pygame.event.wait(300)

            if keys[pygame.K_s] and no_spam_P1_4:
                no_spam_P1_3 = False
                selection_statement_P1 = 3
                pygame.event.wait(300)

            if not keys[pygame.K_z]: #Vu que ce sont des if en cascade et comme je ne peux pas laisser l'utilisateur
            #changer les touches pour éviter le spam, je laisse l'utilisateur la possibilité de continuer
            #seulement s'il relâche la touche 2 (ici c'est z)
                no_spam_P1_4 = True

        elif selection_statement_P1 == 5:
            ready_P1 = True

        #Menu P2 *************************************
        if selection_statement_P2 == 1:
            connected_2 = False #affiche ou non l'écran après une connection
            if keys[pygame.K_UP]:
                selection_statement_P2 = 2
                no_spam_P2_2 = False

        elif selection_statement_P2 == 2:
            connected_2 = True
            if keys[pygame.K_LEFT]:
                flag_P2 -= 1
                pygame.event.wait(300)

            if keys[pygame.K_RIGHT]:
                flag_P2 += 1
                pygame.event.wait(300)

            if keys[pygame.K_UP] and no_spam_P2_2:
                selection_statement_P2 = 3
                no_spam_P2_3 = False  # on dit au programme que l'utilisateur ne va pas pouvoir passer direct au niveau 4
                pygame.event.wait(300)

            if not keys[pygame.K_UP] and repeat_2:
                repeat_2 = False
                no_spam_P2_2 = True
                pygame.event.wait(300)


        elif selection_statement_P2 == 3:

            if keys[pygame.K_LEFT] and no_spam_P2_3:
                skin_P2 -= 1
                pygame.event.wait(300)

            if keys[pygame.K_RIGHT] and no_spam_P2_3:
                skin_P2 += 1
                pygame.event.wait(300)

            if keys[pygame.K_UP] and no_spam_P2_3:
                no_spam_P2_4 = False  # pareil pour le niveau 4
                selection_statement_P2 = 4
                pygame.event.wait(300)

            if keys[pygame.K_DOWN] and no_spam_P2_3:
                selection_statement_P2 = 2
                pygame.event.wait(300)

            if not keys[pygame.K_UP]:
                no_spam_P2_3 = True

        elif selection_statement_P2 == 4:
            ready_P2 = False

            if keys[pygame.K_UP] and no_spam_P2_4:
                selection_statement_P2 = 5
                no_spam_P2_4 = False
                pygame.event.wait(300)

            if keys[pygame.K_DOWN] and no_spam_P2_4:
                no_spam_P2_3 = False
                selection_statement_P2 = 3
                pygame.event.wait(300)

            if not keys[pygame.K_UP]:
                no_spam_P2_4 = True

        elif selection_statement_P2 == 5:
            ready_P2 = True



        if keys[pygame.K_SPACE] and ready_P2 and ready_P1 :
            game_statement = 2
            pygame.event.wait(6000)


        if keys[pygame.K_q] and keys[pygame.K_d] and not connected_1:
            connected_1 = True


        #Déroulement des drapeaux
        if flag_P1 >= 5:
            flag_P1 = 5
        elif flag_P1 <= 0:
            flag_P1 = 0

        if flag_P2 >= 5:
            flag_P2 = 5
        elif flag_P2 <= 0:
            flag_P2 = 0


        if flag_P1 == 0:
            P1_Selected_flag = Flags_Fr
        elif flag_P1 == 1:
            P1_Selected_flag = Flags_Allm
        elif flag_P1 == 2:
            P1_Selected_flag = Flags_It
        elif flag_P1 == 3:
            P1_Selected_flag = Flags_Es
        elif flag_P1 == 4:
            P1_Selected_flag = Flags_En
        elif flag_P1 == 5:
            P1_Selected_flag = Flags_Us

        if flag_P2 == 0:
            P2_Selected_flag = Flags_Fr
        elif flag_P2 == 1:
            P2_Selected_flag = Flags_Allm
        elif flag_P2 == 2:
            P2_Selected_flag = Flags_It
        elif flag_P2 == 3:
            P2_Selected_flag = Flags_Es
        elif flag_P2 == 4:
            P2_Selected_flag = Flags_En
        elif flag_P2 == 5:
            P2_Selected_flag = Flags_Us


        #Déroulement des skins
        if skin_P1 >= 2:
            skin_P1 = 2
        elif skin_P1 <= 0:
            skin_P1 = 0

        if skin_P2 >= 2:
            skin_P2 = 2
        elif skin_P2 <= 0:
            skin_P2 = 0


        if skin_P1 == 0:
            P1_Selected = P_clean
        elif skin_P1 == 1:
            P1_Selected = P_band
        elif skin_P1 == 2:
            P1_Selected = P_spider

        if skin_P2 == 0:
            P2_Selected = P_clean
        elif skin_P2 == 1:
            P2_Selected = P_band
        elif skin_P2 == 2:
            P2_Selected = P_spider


        if ctn_flag >= flag_time_animation:
            ctn_flag = 0
            flag_state += 1
        else:
            ctn_flag += 1

        if flag_state >= 6:
            flag_state = 0


        P1_flag = P1_Selected_flag[flag_state]
        P2_flag = P2_Selected_flag[flag_state]


        if connected_1:
            Fond_P1 = P1_Fond_Ready
        else:
            Fond_P1 = P1_Fond_Waiting

        if connected_2:
            Fond_P2 = P2_Fond_Ready
        else:
            Fond_P2 = P2_Fond_Waiting




        Window.blit(pygame.transform.scale(BG_3, Window.get_size()), [0, 0])

        Window.blit(Fond_P1, [0, 0])
        Window.blit(Fond_P2, [0, 0])


        if connected_1 or connected_2:
            Window.blit(Tuto, [276, 146])

        if selection_statement_P1 == 4 or ready_P1:
            Window.blit(P1_Fond_Question, [-5, -2])
        if selection_statement_P2 == 4 or ready_P2:
            Window.blit(P2_Fond_Question, [6, -4])

        if ready_P1 :
            Window.blit(Valid_P1 , [652, 519])

        if ready_P2:
            Window.blit(Valid_P2, [1378, 519])


        if connected_1 :
            Window.blit(P1_flag, [-105, -1])
            Window.blit(P1_Selected, [38, 549])
            if selection_statement_P1 == 2 :
                Window.blit(Boutons, [-105, -1])
            elif selection_statement_P1 == 3 :
                Window.blit(Boutons, [-270, 490])

        if connected_2:
            Window.blit(P2_flag, [615, -1])
            Window.blit(P2_Selected, [768, 549])
            if selection_statement_P2 == 2 :
                Window.blit(Boutons, [615, -1])
            elif selection_statement_P2 == 3 :
                Window.blit(Boutons, [455, 490])

        Window.blit(text_menu, [334, 24])

        if not (ready_P2 and ready_P1):
            Window.blit(text_waiting, [576, 142])
        else:
            Window.blit(text_proceed, [540, 150])
        if not ready_P1:
            Window.blit(text_P1_waiting, [755, 142])
        if not ready_P2:
            Window.blit(text_P2_waiting, [822, 141])

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
            Service_P1 = False

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
            Service_P2 = False

        if keys[pygame.K_RIGHT]:
            pos_y2 += walk_speed


        rotation_in_progress3 = True

        # tuto
        if keys[pygame.K_k]:
            pos_x_temp += 1
            score_P1 += 1
        if keys[pygame.K_h]:
            pos_x_temp -= 1
            score_P1 -= 1
        if keys[pygame.K_u]:
            pos_y_temp -= 1
            score_P2 -= 1
        if keys[pygame.K_j]:
            pos_y_temp += 1
            score_P2 += 1

        print(pos_x_temp, pos_y_temp)


    #VOLANNNNT



        if keys[pygame.K_SPACE] or respawn_P1:
            Service_P1 = True
            Actif = True
            pos_y3, pos_x3 = 360, 540
            en_saut_volant_D = False
            en_saut_volant_G = False
            volant_force = -14.5
            GRAVITE_volant = GRAVITE
            volant_speed = 14
            vitesse_x3 = 0
            one_time1 = True
            one_time2 = True
            smash_P2 = False
            smash_P1 = False
            Contact = False
            respawn_P1 = False

        if keys[pygame.K_n] or respawn_P2:
            Service_P2 = True
            Actif = True
            pos_y3, pos_x3 = 900, 540
            en_saut_volant_D = False
            en_saut_volant_G = False
            volant_force = -14.5
            GRAVITE_volant = GRAVITE
            volant_speed = 14
            vitesse_x3 = 0
            one_time1 = True
            one_time2 = True
            smash_P2 = False
            smash_P1 = False
            Contact = False
            respawn_P2 = False


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

        #Animation drapeau des pays:
        if ctn_flag >= flag_time_animation:
            ctn_flag = 0
            flag_state += 1
        else:
            ctn_flag += 1

        if flag_state >= 6:
            flag_state = 0


        P1_flag = P1_Selected_flag[flag_state]
        P2_flag = P2_Selected_flag[flag_state]

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

    #Détéction score: # 705 ou 609 à tester
        if (pos_x3 == SOL_VOLANT) and (pos_y3 >= 609):
            if score :
                score_P1 += 1
                score = False

            if wait_before_new_point >= 60:
                respawn_P1 = True
                wait_before_new_point = 0
                score = True
            else :
                wait_before_new_point += 1

        if (pos_x3 == SOL_VOLANT) and (pos_y3 <= 609):
            if score:
                score_P2 += 1
                score = False

            if wait_before_new_point >= 60:
                respawn_P2 = True
                wait_before_new_point = 0
                score = True
            else:
                wait_before_new_point += 1


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

        if (mask_p1.overlap(mask_vol, (rect_vol.x - rect_p1.x, rect_vol.y - rect_p1.y)) or mask_p1.overlap(mask_vol_rotated, (rect_vol_rotated.x - rect_p1.x, rect_vol_rotated.y - rect_p1.y))) and Actif and rotation_in_progress1 and test1 != 1 and one_time1:
            one_time1 = False
            one_time2 = True
            Contact = True
            en_saut_volant_G = True
            en_saut_volant_D = False
            smash_P2 = False

            if en_saut1:
                smash_P1 = True

            if not Do_a_flip:
                volant = pygame.transform.flip(volant, False, True)
                Do_a_flip = True

        if (mask_p2.overlap(mask_vol, (rect_vol.x - rect_p2.x, rect_vol.y - rect_p2.y)) or mask_p2.overlap(mask_vol_rotated, (rect_vol_rotated.x - rect_p2.x, rect_vol_rotated.y - rect_p2.y))) and Actif and rotation_in_progress2 and test2 != 1 and one_time2:
            one_time2 = False
            one_time1 = True
            Contact = True
            en_saut_volant_D = True
            en_saut_volant_G = False
            smash_P1 = False

            if en_saut2:
                smash_P2 = True

            if Do_a_flip:
                volant = pygame.transform.flip(volant, False, True)
                Do_a_flip = False

        if  smash_P2 or smash_P1:
            volant_force = -3
            volant_speed = 25
        else:
            volant_force = - 14.5
            volant_speed = 10

        if (en_saut_volant_D or en_saut_volant_G) and Contact:
            vitesse_x3 = volant_force
            Contact = False


        # ****************************************************



        # ************ Dessiner le perso à sa nouvelle position ************

    # Filet au bon endroit
        Window.blit(filet, [700, 550])

    # On affiche le drapeau des joueurs sur les côtés
        Window.blit(Flag_pole, [-4, 0])
        Window.blit(P1_flag, [-311, 245])
        Window.blit(P2_flag, [820, 244])

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

    # Score
        text_score = pixel_font.render(("{}:{}".format(score_P1, score_P2)), True, '#00353F')
        text_rect = text_score.get_rect(center=(723, 454))
        Window.blit(text_score, text_rect.topleft)

    # Volant
        if Actif:
            if rotation_in_progress3:
                Window.blit(volant_rotated, rect_rotated3)
            else:
                Window.blit(volant, [pos_y3, pos_x3])

    # Service
        #on veut afficher le petit logo service à gauche ou à droite tant que le joueur n'a pas tirer
        if Service_P1:
            Window.blit(service, [pos_y1 + 43, pos_x1 - 25])
        if Service_P2:
            Window.blit(service, [pos_y2 + 1, pos_x2 - 22])



#********************************************************


#****** End of while loop *********

    clock.tick(60)
    pygame.display.update()
pygame.quit()