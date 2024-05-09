import pygame
import os
import Goodminton.Constantes as C
import math


def Goodminton(Window):
    clock = pygame.time.Clock()
    cloud_font_1 = pygame.font.Font(os.path.join("Goodminton","data","Font","DCC - Cloud.otf"), 200)
    normal_font = pygame.font.Font(os.path.join("Goodminton","data","Font","Light Stories.otf"), 100)
    small_font = pygame.font.Font(os.path.join("Goodminton","data","Font","Light Stories.otf"), 40)
    pixel_font = pygame.font.Font(os.path.join("Goodminton","data","Font","Rémi.ttf"), 40)

    text_minton_surf = cloud_font_1.render("Goodminton", True, '#96527A')
    text_menu = normal_font.render("Select your character", True, '#00353F')
    text_waiting = small_font.render("Waiting on :     /", True, '#00353F')
    text_P1_waiting = small_font.render("P1", True, '#00353F')
    text_P2_waiting = small_font.render("P2", True, '#00353F')
    text_proceed = small_font.render("Press < space > to proceed", True, '#00353F')

    C.running=True
    C.game_statement=0
    while C.running:


        if C.game_statement == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Pour quitter le programme
                    C.running = False
                    pygame.quit()
                    exit()
            keys = pygame.key.get_pressed()
            # Les touches :
            if keys[pygame.K_ESCAPE]:
                C.running = False  # Pour fermer programme

            selection_statement_P1 = 1 #tres important pour reboot le menu et les scores
            flag_P1 = 0
            skin_P1 = 0
            C.ready_P1 = False
            C.repeat_1 = True
            C.score_P1 = 0

            selection_statement_P2 = 1 #same
            flag_P2 = 0
            skin_P2 = 0
            C.ready_P2 = False
            C.repeat_2 = True
            C.score_P2 = 0

            if keys[pygame.K_SPACE]:
                C.game_statement = 1
                pygame.event.wait(6000)

            if C.C1_x >= 1111:
                C.C1_x = -600
            else:
                C.C1_x += C.vitesse_nuage

            if C.C2_x >= 1280:
                C.C2_x = -600
            else:
                C.C2_x += C.vitesse_nuage

            if C.C3_x >= 1450:
                C.C3_x = -200
            else:
                C.C3_x += C.vitesse_nuage

            if C.C4_x >= 730:
                C.C4_x = -950
            else:
                C.C4_x += C.vitesse_nuage

            if C.C5_x >= 600:
                C.C5_x = -1100
            else:
                C.C5_x += C.vitesse_nuage

            if C.C6_x >= 300:
                C.C6_x = -1410
            else:
                C.C6_x += C.vitesse_nuage


            Window.blit(pygame.transform.scale(C.BG_2, Window.get_size()), [0, 0])
            Window.blit(C.anneaux, [0, 0])
            Window.blit(text_minton_surf, [174, 134])
            Window.blit(text_proceed, [547, 779])
            Window.blit(C.C1, [C.C1_x, C.C1_y - 50])
            Window.blit(C.C2, [C.C2_x, C.C2_y - 50])
            Window.blit(C.C3, [C.C3_x, C.C3_y - 50])
            Window.blit(C.C4, [C.C4_x, C.C4_y - 50])
            Window.blit(C.C5, [C.C5_x, C.C5_y - 50])
            Window.blit(C.C6, [C.C6_x, C.C6_y - 50])



        elif C.game_statement == 1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Pour quitter le programme
                    C.running = False
                    pygame.quit()
                    exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                C.running = False  # Pour fermer programme


            # Menu P1 *************************************
            if selection_statement_P1 == 1:
                C.connected_1 = False

                if keys[pygame.K_z]:
                    selection_statement_P1 = 2
                    no_spam_P1_2 = False


            elif selection_statement_P1 == 2:
                C.connected_1 = True

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

                if not no_spam_P1_2 and C.repeat_1:
                    C.repeat_1 = False
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
                C.ready_P1 = False

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
                C.ready_P1 = True

            #Menu P2 *************************************
            if selection_statement_P2 == 1:
                C.connected_2 = False #affiche ou non l'écran après une connection
                if keys[pygame.K_UP]:
                    selection_statement_P2 = 2
                    no_spam_P2_2 = False

            elif selection_statement_P2 == 2:
                C.connected_2 = True
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

                if not keys[pygame.K_UP] and C.repeat_2:
                    C.repeat_2 = False
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
                C.ready_P2 = False

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
                C.ready_P2 = True



            if keys[pygame.K_SPACE] and C.ready_P2 and C.ready_P1 :
                C.game_statement = 2
                pygame.event.wait(6000)


            if keys[pygame.K_q] and keys[pygame.K_d] and not C.connected_1:
                C.connected_1 = True


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
                P1_Selected_flag = C.Flags_Fr
            elif flag_P1 == 1:
                P1_Selected_flag = C.Flags_Allm
            elif flag_P1 == 2:
                P1_Selected_flag = C.Flags_It
            elif flag_P1 == 3:
                P1_Selected_flag = C.Flags_Es
            elif flag_P1 == 4:
                P1_Selected_flag = C.Flags_En
            elif flag_P1 == 5:
                P1_Selected_flag = C.Flags_Us

            if flag_P2 == 0:
                P2_Selected_flag = C.Flags_Fr
            elif flag_P2 == 1:
                P2_Selected_flag = C.Flags_Allm
            elif flag_P2 == 2:
                P2_Selected_flag = C.Flags_It
            elif flag_P2 == 3:
                P2_Selected_flag = C.Flags_Es
            elif flag_P2 == 4:
                P2_Selected_flag = C.Flags_En
            elif flag_P2 == 5:
                P2_Selected_flag = C.Flags_Us


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
                P1_Selected = C.P_clean
            elif skin_P1 == 1:
                P1_Selected = C.P_band
            elif skin_P1 == 2:
                P1_Selected = C.P_spider

            if skin_P2 == 0:
                P2_Selected = C.P_clean
            elif skin_P2 == 1:
                P2_Selected = C.P_band
            elif skin_P2 == 2:
                P2_Selected = C.P_spider


            if C.ctn_flag >= C.flag_time_animation:
                C.ctn_flag = 0
                C.flag_state += 1
            else:
                C.ctn_flag += 1

            if C.flag_state >= 6:
                C.flag_state = 0


            P1_flag = P1_Selected_flag[C.flag_state]
            P2_flag = P2_Selected_flag[C.flag_state]


            if C.connected_1:
                Fond_P1 = C.P1_Fond_Ready
            else:
                Fond_P1 = C.P1_Fond_Waiting

            if C.connected_2:
                Fond_P2 = C.P2_Fond_Ready
            else:
                Fond_P2 = C.P2_Fond_Waiting




            Window.blit(pygame.transform.scale(C.BG_3, Window.get_size()), [0, 0])

            Window.blit(Fond_P1, [0, 0])
            Window.blit(Fond_P2, [0, 0])


            if C.connected_1 or C.connected_2:
                Window.blit(C.Tuto, [276, 146])

            if selection_statement_P1 == 4 or C.ready_P1:
                Window.blit(C.P1_Fond_Question, [-5, -2])
            if selection_statement_P2 == 4 or C.ready_P2:
                Window.blit(C.P2_Fond_Question, [6, -4])

            if C.ready_P1 :
                Window.blit(C.Valid_P1 , [652, 519])

            if C.ready_P2:
                Window.blit(C.Valid_P2, [1378, 519])


            if C.connected_1 :
                Window.blit(P1_flag, [-105, -1])
                Window.blit(P1_Selected, [38, 549])
                if selection_statement_P1 == 2 :
                    Window.blit(C.Boutons, [-105, -1])
                elif selection_statement_P1 == 3 :
                    Window.blit(C.Boutons, [-270, 490])

            if C.connected_2:
                Window.blit(P2_flag, [615, -1])
                Window.blit(P2_Selected, [768, 549])
                if selection_statement_P2 == 2 :
                    Window.blit(C.Boutons, [615, -1])
                elif selection_statement_P2 == 3 :
                    Window.blit(C.Boutons, [455, 490])

            Window.blit(text_menu, [334, 24])

            if not (C.ready_P2 and C.ready_P1):
                Window.blit(text_waiting, [576, 142])
            else:
                Window.blit(text_proceed, [540, 150])
            if not C.ready_P1:
                Window.blit(text_P1_waiting, [755, 142])
            if not C.ready_P2:
                Window.blit(text_P2_waiting, [822, 141])

        elif C.game_statement == 2:
            Window.blit(pygame.transform.scale(C.BG_1,Window.get_size()), [0, 0])  # Ouvre une fenêtre de jeu avec un arière plan défini, ici, c est fond
            C.rotation_center1 = (C.pos_y1 + 88, C.pos_x1 + 93)
            C.rotation_center2 = (C.pos_y2 + 33, C.pos_x2 + 93)
            C.rotation_center3 = (C.pos_y3 + 24, C.pos_x3 + 24)

            C.previous_x3 = C.pos_x3
            C.previous_y3 = C.pos_y3

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Pour quitter le programme
                    C.running = False
                    pygame.quit()
                    exit()
            keys = pygame.key.get_pressed()
            # Les touches :
            if keys[pygame.K_ESCAPE]:
                C.running = False  # Pour fermer programme
            if keys[pygame.K_m]:
                C.game_statement = 0  # Pour fermer programme

        # ************** Déplacement / Coup dans volant **************

        # Player 1
            if keys[pygame.K_z] and not C.en_saut1:
                C.en_saut1 = True
                C.vitesse_x1 = C.Saut_Force

            if keys[pygame.K_q]:
                C.pos_y1 -= C.walk_speed

            if keys[pygame.K_s] and not C.rotation_in_progress1:
                C.rotation_in_progress1 = True
                C.Service_P1 = False

            if keys[pygame.K_d]:
                C.pos_y1 += C.walk_speed


        # Player 2
            if keys[pygame.K_UP] and not C.en_saut2 :
                C.en_saut2 = True
                C.vitesse_x2 = C.Saut_Force

            if keys[pygame.K_LEFT]:
                C.pos_y2 -= C.walk_speed

            if keys[pygame.K_DOWN] and not C.rotation_in_progress2:
                C.rotation_in_progress2 = True
                C.Service_P2 = False

            if keys[pygame.K_RIGHT]:
                C.pos_y2 += C.walk_speed


            C.rotation_in_progress3 = True

            # tuto
            if keys[pygame.K_k]:
                C.pos_x_temp += 1
                C.score_P1 += 1
            if keys[pygame.K_h]:
                C.pos_x_temp -= 1
                C.score_P1 -= 1
            if keys[pygame.K_u]:
                C.pos_y_temp -= 1
                C.score_P2 -= 1
            if keys[pygame.K_j]:
                C.pos_y_temp += 1
                C.score_P2 += 1


        #VOLANNNNT



            if keys[pygame.K_SPACE] or C.respawn_P1:
                C.Service_P1 = True
                C.Actif = True
                C.pos_y3, C.pos_x3 = 360, 540
                C.en_saut_volant_D = False
                C.en_saut_volant_G = False
                C.volant_force = -14.5
                C.GRAVITE_volant = C.GRAVITE
                C.volant_speed = 14
                C.vitesse_x3 = 0
                one_time1 = True
                one_time2 = True
                C.smash_P2 = False
                C.smash_P1 = False
                Contact = False
                C.respawn_P1 = False

            if keys[pygame.K_n] or C.respawn_P2:
                C.Service_P2 = True
                C.Actif = True
                C.pos_y3, C.pos_x3 = 900, 540
                C.en_saut_volant_D = False
                C.en_saut_volant_G = False
                C.volant_force = -14.5
                C.GRAVITE_volant = C.GRAVITE
                C.volant_speed = 14
                C.vitesse_x3 = 0
                one_time1 = True
                one_time2 = True
                C.smash_P2 = False
                C.smash_P1 = False
                Contact = False
                C.respawn_P2 = False


            if C.en_saut_volant_G:
                C.pos_y3 += C.volant_speed

            if C.en_saut_volant_D:
                C.pos_y3 -= C.volant_speed


        # Appliquer la Gravité:
            if C.en_saut1:
                C.vitesse_x1 += C.GRAVITE
            if C.en_saut2:
                C.vitesse_x2 += C.GRAVITE
            if C.en_saut_volant_D or C.en_saut_volant_G:
                C.vitesse_x3 += C.GRAVITE_volant


        # Mettre à jour la position verticale des sprites
            C.pos_x1 += C.vitesse_x1
            C.pos_x2 += C.vitesse_x2
            C.pos_x3 += C.vitesse_x3

        # ****************** Rotations des bras ************************

        # Player 1:
            if C.rotation_in_progress1 :
                if C.angle_rotation1 < 120 and C.test1 != 1:
                    C.angle_rotation1 += C.rotation_speed
                else:
                    C.angle_rotation1 -= C.rotation_speed
                    C.test1 = 1
                    if C.angle_rotation1 <= 0:
                        C.rotation_in_progress1 = False
                        C.angle_rotation1 = 0
                        C.test1 = 0

            P1_Arm_rotated = pygame.transform.rotate(C.P1_Arm, -C.angle_rotation1)
            rect_rotated1 = P1_Arm_rotated.get_rect(center=C.rotation_center1)   # Permet de rectifier la rotation en changeant les coordonnées du sprite pour ne pas donner un truc tout goofy

        # Player 2:
            if C.rotation_in_progress2:
                if C.angle_rotation2 < 120 and C.test2 != 1:
                    C.angle_rotation2 += C.rotation_speed
                else:
                    C.angle_rotation2 -= C.rotation_speed
                    C.test2 = 1
                    if C.angle_rotation2 <= 0:
                        C.rotation_in_progress2 = False
                        C.angle_rotation2 = 0
                        C.test2 = 0

            P2_Arm_rotated = pygame.transform.rotate(C.P2_Arm, C.angle_rotation2)
            rect_rotated2 = P2_Arm_rotated.get_rect(center=C.rotation_center2)



            # Volant

            if C.pos_x3 - C.previous_x3 != 0:
                C.angle_rotation3 = math.atan((C.pos_y3 - C.previous_y3) / (C.pos_x3 - C.previous_x3))
                if C.angle_rotation3 < 0:
                    C.angle_rotation3 = math.degrees(C.angle_rotation3)
                if C.angle_rotation3 > 0:
                    C.angle_rotation3 = math.degrees(C.angle_rotation3) + 180

            volant_rotated = pygame.transform.rotate(C.volant, C.angle_rotation3)
            rect_rotated3 = volant_rotated.get_rect(center=C.rotation_center3)


            # **********************************************************************

            #Animation drapeau des pays:
            if C.ctn_flag >= C.flag_time_animation:
                C.ctn_flag = 0
                C.flag_state += 1
            else:
                C.ctn_flag += 1

            if C.flag_state >= 6:
                C.flag_state = 0


            P1_flag = P1_Selected_flag[C.flag_state]
            P2_flag = P2_Selected_flag[C.flag_state]

        # ************** Limites du terrain ***********
        # Horizontalement
            if C.pos_y1<130:
                C.pos_y1=130
            if C.pos_y1>575:
                C.pos_y1=575
            if C.pos_y2<755:
                C.pos_y2=755
            if C.pos_y2>1205:
                C.pos_y2=1205
            if C.pos_y3<130:
                C.pos_y3=130
            if C.pos_y3>1205:
                C.pos_y3=1205

        # Verticalement
            if C.pos_x1 >= C.SOL:
                C.en_saut1 = False
                C.pos_x1 = C.SOL
            if C.pos_x2 >= C.SOL:
                C.en_saut2 = False
                C.pos_x2 = C.SOL
            if C.pos_x3 >= C.SOL_VOLANT:
                C.en_saut_volant_G = False
                C.en_saut_volant_D = False
                C.pos_x3 = C.SOL_VOLANT

        #Détéction score: # 705 ou 609 à tester
            if (C.pos_x3 == C.SOL_VOLANT) and (C.pos_y3 >= 609):
                if C.score :
                    C.score_P1 += 1
                    C.score = False

                if C.wait_before_new_point >= 60:
                    C.respawn_P1 = True
                    C.wait_before_new_point = 0
                    C.score = True
                else :
                    C.wait_before_new_point += 1

            if (C.pos_x3 == C.SOL_VOLANT) and (C.pos_y3 <= 609):
                if C.score:
                    C.score_P2 += 1
                    C.score = False

                if C.wait_before_new_point >= 60:
                    C.respawn_P2 = True
                    C.wait_before_new_point = 0
                    C.score = True
                else:
                    C.wait_before_new_point += 1


        # *************** Détection de collision ***************
        # Obtenir les masques de collision pour P1 et P2
            mask_p1 = pygame.mask.from_surface(P1_Arm_rotated)
            mask_p2 = pygame.mask.from_surface(P2_Arm_rotated)
            mask_vol = pygame.mask.from_surface(C.volant)
            mask_vol_rotated = pygame.mask.from_surface(volant_rotated)

        # Définir les rectangles de collision pour P1 et P2
            rect_p1 = C.P1_Arm.get_rect(topleft=(C.pos_y1, C.pos_x1))
            rect_p2 = C.P2_Arm.get_rect(topleft=(C.pos_y2, C.pos_x2))
            rect_vol = C.volant.get_rect(topleft=(C.pos_y3, C.pos_x3))
            rect_vol_rotated = volant_rotated.get_rect(topleft=(C.pos_y3, C.pos_x3))

            if (mask_p1.overlap(mask_vol, (rect_vol.x - rect_p1.x, rect_vol.y - rect_p1.y)) or mask_p1.overlap(mask_vol_rotated, (rect_vol_rotated.x - rect_p1.x, rect_vol_rotated.y - rect_p1.y))) and C.Actif and C.rotation_in_progress1 and C.test1 != 1 and one_time1:
                one_time1 = False
                one_time2 = True
                Contact = True
                C.en_saut_volant_G = True
                C.en_saut_volant_D = False
                C.smash_P2 = False

                if C.en_saut1:
                    C.smash_P1 = True

                if not C.Do_a_flip:
                    C.volant = pygame.transform.flip(C.volant, False, True)
                    C.Do_a_flip = True

            if (mask_p2.overlap(mask_vol, (rect_vol.x - rect_p2.x, rect_vol.y - rect_p2.y)) or mask_p2.overlap(mask_vol_rotated, (rect_vol_rotated.x - rect_p2.x, rect_vol_rotated.y - rect_p2.y))) and C.Actif and C.rotation_in_progress2 and C.test2 != 1 and one_time2:
                one_time2 = False
                one_time1 = True
                Contact = True
                C.en_saut_volant_D = True
                C.en_saut_volant_G = False
                C.smash_P1 = False

                if C.en_saut2:
                    C.smash_P2 = True

                if C.Do_a_flip:
                    C.volant = pygame.transform.flip(C.volant, False, True)
                    C.Do_a_flip = False

            if  C.smash_P2 or C.smash_P1:
                C.volant_force = -3
                C.volant_speed = 25
            else:
                C.volant_force = - 14.5
                C.volant_speed = 10

            if (C.en_saut_volant_D or C.en_saut_volant_G) and Contact:
                C.vitesse_x3 = C.volant_force
                Contact = False


            # ****************************************************



            # ************ Dessiner le perso à sa nouvelle position ************

        # Filet au bon endroit
            Window.blit(C.filet, [700, 550])

        # On affiche le drapeau des joueurs sur les côtés
            Window.blit(C.Flag_pole, [-4, 0])
            Window.blit(P1_flag, [-311, 245])
            Window.blit(P2_flag, [820, 244])

        # Player 1
            Window.blit(C.P1_Body,[C.pos_y1,C.pos_x1]) # On déplace P1 à ses nouvelles coordonnées

            if C.rotation_in_progress1:
                Window.blit(P1_Arm_rotated, rect_rotated1)
            else:
                Window.blit(C.P1_Arm, [C.pos_y1,C.pos_x1])

        # Player 2
            Window.blit(C.P2_Body, [C.pos_y2, C.pos_x2]) # On déplace P2 à ses nouvelles coordonnées

            if C.rotation_in_progress2:   # Position des bras : on ne passe pas tout le temps dans la boucle de rotation pour limiter le lag
                Window.blit(P2_Arm_rotated, rect_rotated2)
            else:
                Window.blit(C.P2_Arm, [C.pos_y2 - 53,C.pos_x2])

        # Score
            text_score = pixel_font.render(("{}:{}".format(C.score_P1, C.score_P2)), True, '#00353F')
            text_rect = text_score.get_rect(center=(723, 454))
            Window.blit(text_score, text_rect.topleft)

        # Volant
            if C.Actif:
                if C.rotation_in_progress3:
                    Window.blit(volant_rotated, rect_rotated3)
                else:
                    Window.blit(C.volant, [C.pos_y3, C.pos_x3])

        # Service
            #on veut afficher le petit logo service à gauche ou à droite tant que le joueur n'a pas tirer
            if C.Service_P1:
                Window.blit(C.service, [C.pos_y1 + 43, C.pos_x1 - 25])
            if C.Service_P2:
                Window.blit(C.service, [C.pos_y2 + 1, C.pos_x2 - 22])



    #********************************************************


    #****** End of while loop *********

        clock.tick(60)
        pygame.display.update()
