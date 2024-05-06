import pygame
import random
import math
import os
import basketball.variables as var
#Changed to not have global variables imported in every functions of the runtime.

def game_menu(screen):
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_running = False
                    return False
                if event.key == pygame.K_ESCAPE:
                    return True #quit the game to the big menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check if left mouse button is pressed
                    # Check if the mouse cursor is over the play button
                    if var.play_button_rect.collidepoint(event.pos):
                        menu_running = False
                        return False

        screen.blit(var.menu_surf, var.menu_rect)
        screen.blit(var.play_button_surf, var.play_button_rect)
        pygame.display.update()
def display_score_menu(screen):
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True  # quit the game to the big menu
        # Render the score text
        score_text = var.score_font2.render("{}".format(var.score), True, var.color)
        screen.blit(var.score_menu_surf, var.score_menu_rect)
        screen.blit(score_text, (410, 200))
        pygame.display.update()


def basketball(screen):
    if (game_menu(screen)):  # Call the menu before starting the game loop
        #  test to exit inside the game menu.
        return

    var.running = True
    var.game_active = True

    while var.running == True:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - var.shoot_time) // 1000
        animation_index = (current_time // var.animation_speed) % len(var.player_animation_surf)
        if elapsed_time % 2 == 0 and elapsed_time != 0 and elapsed_time != var.last_action_time and var.number_of_point > 20:  # Make the preview of trajectory less and less precise if the player don't get point
            var.number_of_point = var.number_of_point - 10
            var.last_action_time = elapsed_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                var.running = False
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and not var.shoot:
                if event.key == pygame.K_RIGHT:
                    var.speed += 1
                    var.memo_speed+=1
                    var.trajectory = True
                elif event.key == pygame.K_LEFT and var.speed >= 10:
                    var.speed -= 1
                    var.memo_speed-=1
                    var.trajectory = True
                elif event.key == pygame.K_SPACE:
                    var.shoot = True
                    var.ball_Sound.play()
                    var.time = 0  # Reset time after shooting
                elif event.key == pygame.K_ESCAPE:
                    return #quit the game to the big menu

                var.text1 = var.text_font.render("Angle : {} ".format(var.angle), True, var.color)
                var.text2 = var.text_font.render("Speed : {}".format(var.speed), True, var.color)

        var.back_ground_surf = pygame.transform.scale(pygame.image.load(os.path.join("basketball","assets","basketball court.png")).convert_alpha(),(950, 600))

        for time2 in range(0,var.number_of_point,3):
            if var.bouncetest == False:
                var.x_pre = (var.x_ini + math.cos(math.radians(var.angle)) * var.speed * time2)
                var.y_pre = (var.y_ini - (math.sin(math.radians(var.angle)) * var.speed * time2) + 0.5 * var.gravity * time2 ** 2)
                pygame.draw.circle(var.back_ground_surf,'white',(var.x_pre,var.y_pre),5) # preview trajectory with draw circles

        """mouse = pygame.mouse
        if mouse.get_pressed()[0]:
            print(mouse.get_pos())
        mouse = pygame.mouse"""
        if var.shoot == False:
            var.arrow_x += var.c
            var.angle += var.c
            if var.arrow_x == 382:
                var.c=var.b
            elif var.arrow_x==260:
                var.c=var.a
        var.arrow_power_gauge_rect.center = (var.arrow_x, var.arrow_y)
        var.text1 = var.text_font.render("Angle : {} ".format(var.angle), True, var.color)
        if var.shoot == True:
            # Calculate location
            var.x_val = (var.x_ini + math.cos(math.radians(var.angle)) * var.speed * var.time)
            var.y_val = (var.y_ini - (math.sin(math.radians(var.angle)) * var.speed * var.time) + 0.5 * var.gravity * var.time ** 2)

            if var.y_val + var.ball_surf.get_height() >= var.back_ground_surf.get_height():
                # Implement bounce
                var.bounce_sound.play()
                var.bouncetest=True
                var.bounce_count += 1
                var.y_val = var.back_ground_surf.get_height() - var.ball_surf.get_height()
                var.speed *= var.retention  # Reduce speed due to bounce
                var.angle = -var.angle  # Reverse angle (simulate bounce)
                var.x_ini = var.x_val
                var.y_ini = var.y_val
                var.time = 0
            if var.ball_rect.colliderect(var.hitbox_hopper_rect1) or var.ball_rect.colliderect(var.hitbox_hopper_rect2) or var.ball_rect.colliderect(var.hitbox_hopper_rect3) :
                # Implement bounce or any other action
                var.bounce_sound.play()
                var.bouncetest = True
                var.bounce_count += 1
                var.y_val = var.hopper_rect.topleft[1]+20 - var.ball_surf.get_height()+20  # Set y_val to the top of the hopper hitbox
                var.speed *= var.retention2  # Reduce speed due to bounce
                var.angle = -var.angle  # Reverse angle (simulate bounce)
                var.x_ini = var.x_val
                var.y_ini = var.y_val
                var.time = 0
            if var.ball_rect.colliderect(var.hitbox_score_rect) and var.played_test==False :
                var.win_sound.play()
                var.shoot_time = current_time
                var.number_of_point = 70
                var.played_test=True
                var.angle = 0.0
                var.speed = var.memo_speed
                var.player_rect.midbottom = (random.randint(100, 400),480)
                var.x_val = var.player_rect.x + 70
                var.y_val = var.player_rect.y + 90
                var.x_ini = var.player_rect.x + 70
                var.y_ini = var.player_rect.y + 90
                var.time = 0
                var.bounce_count = 0
                var.shoot = False
                var.bouncetest = False
                var.played_test = False
                var.score += 1
                var.arrow_x = 260
                var.c = var.a

            elif var.x_val + var.ball_surf.get_width() >= var.back_ground_surf.get_width() or var.bounce_count>=3:
                # Reset ball position and shoot
                var.loose_sound.play()
                var.shoot_time = current_time
                var.shoot = False
                var.angle = 0.0
                var.speed = var.memo_speed
                var.x_ini = var.player_rect.x + 70
                var.y_ini = var.player_rect.y + 90
                var.x_val = var.player_rect.x + 70
                var.y_val = var.player_rect.y + 90
                var.time = 0
                var.bounce_count=0
                var.bouncetest=False
                var.played_test=False
                var.arrow_x = 260
                var.c = var.a
                var.ball_rect.center = (var.player_rect.x , var.player_rect.y )
            var.time += 1  # Increment time

        text3 = var.score_font.render("{}".format(var.score), True, 'black')
        var.ball_rect.center = (var.x_val, var.y_val)

        if var.trajectory :
            var.back_ground_surf = pygame.transform.scale(pygame.image.load(os.path.join("basketball","assets","basketball court.png")).convert_alpha(), (950, 600))
        screen.blit(var.hitbox_score_surf, var.hitbox_score_rect)
        screen.blit(var.hitbox_hooper_surf,var.hitbox_hopper_rect2)
        screen.blit(var.hitbox_hooper_surf,var.hitbox_hopper_rect1)
        screen.blit(var.back_ground_surf, var.back_ground_rect)
        screen.blit(var.player_animation_surf[animation_index], var.player_rect)
        screen.blit(var.hopper_surf, var.hopper_rect)
        screen.blit(var.ball_surf, var.ball_rect)
        screen.blit(var.power_gauge_surf, var.power_gauge_rect)
        screen.blit(var.arrow_power_gauge_surf, var.arrow_power_gauge_rect)
        screen.blit(var.score_back_surf, var.score_back_rect)
        screen.blit(text3, (430,100))
        screen.blit(var.text1, (20, 510))
        screen.blit(var.text2, (30, 470))
        time_text = var.text_font.render("Time : {}".format(current_time//1000), True, var.color)
        screen.blit(time_text, (690,540))
        """pygame.draw.rect(screen, 'Green', hopper_rect, 5)
        pygame.draw.rect(screen, 'Red', hitbox_hopper_rect1,5)
        pygame.draw.rect(screen,'Red',hitbox_hopper_rect2,5)
        pygame.draw.rect(screen, 'Red', hitbox_hopper_rect3, 5)
        pygame.draw.rect(screen,'Yellow',hitbox_score_rect)"""
        var.trajectory = False
        var.clock.tick(60)
        pygame.display.update()
        # Display score menu when time reaches 80 seconds
        if current_time // 1000 == 60 and current_time != var.last_score_menu_time:
            display_score_menu(screen)
            var.last_score_menu_time = current_time
            var.clock.tick(60)
            current_time = 0
            return
