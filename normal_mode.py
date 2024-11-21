import pygame
from pygame.locals import *
import sys
import random
import time

# from choice import *
# from text_box import *
# from reward import *
from result02 import *
from choice_pull import *
from env_page import *


def normal_mode():
    i = 0
    num = 1
    bg_i = 0
    bg = ["sun", "night", "night in city."]

    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Normal mode')

    WIDTH = 720
    HEIGHT = 720

    # background = pygame.image.load('images/sun.jpeg').convert_alpha()
    # background=  pygame.transform.scale(background, (WIDTH, HEIGHT*2//3))

    # question_box = TextBox(screen, width=400, height=60, position=((WIDTH - 400) // 2, HEIGHT // 6), text="Insert Question Here")

    font_size = 20
    choice_size = (250, 80)
    oChoice_1 = Choice(screen, (WIDTH*2//7, HEIGHT*7.5//10), 'images/choice.png', 'images/choice_down.png', font_size, size = choice_size)
    oChoice_2 = Choice(screen, (WIDTH*5//7, HEIGHT*7.5//10), 'images/choice.png', 'images/choice_down.png', font_size, size = choice_size)
    oChoice_3 = Choice(screen, (WIDTH*2//7, HEIGHT*9//10), 'images/choice.png', 'images/choice_down.png', font_size, size = choice_size)
    oChoice_4 = Choice(screen, (WIDTH*5//7, HEIGHT*9//10), 'images/choice.png', 'images/choice_down.png', font_size, size = choice_size)

    rew = c_reward()
    timmer = c_timer(screen,"normol")

    Q_A_check = qusetion_eqution_answer(Need_total_Qusetion=20, choice=60)
    check_Q, check_c = Q_A_check.check_qusetion()

    list_choice = [check_Q[i][0], check_c[i], check_c[i+1], check_c[i+2]]
    ran_list = random.sample(list_choice, k=4)

    anime = animetion(screen)

    # Game loop
    run = True
    while run:
        clock.tick(60)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False

        screen.fill((154, 103, 82))
        if bg_i > 2:
            bg_i = 0
        background = pygame.image.load(f'images/{bg[bg_i]}.jpeg').convert_alpha()
        background=  pygame.transform.scale(background, (WIDTH, HEIGHT*2//3))
        screen.blit(background, background.get_rect())
        if len(check_Q[i][1]) <= 40:
            question_box = TextBox(screen, width=400, height=60, position=((WIDTH - 400) // 2, HEIGHT // 6), text=f"{check_Q[i][1]}")
            question_box.draw()
        else:
            Q_A_check = qusetion_eqution_answer(Need_total_Qusetion=20, choice=60)
            check_Q, check_c = Q_A_check.check_qusetion()
            

            list_choice = [check_Q[i][0], check_c[i], check_c[i+1], check_c[i+2]]
            ran_list = random.sample(list_choice, k=4)
            question_box = TextBox(screen, width=400, height=60, position=((WIDTH - 400) // 2, HEIGHT // 6), text=f"{check_Q[i][1]}")
            question_box.draw()
        oChoice_1.draw(f"{ran_list[0]}")
        oChoice_2.draw(f"{ran_list[1]}")
        oChoice_3.draw(f"{ran_list[2]}")
        oChoice_4.draw(f"{ran_list[3]}")

        if num <= 16 :
            anime.walking(num)
            num += 1
        else:
            num = 1
            anime.walking(num)
        anime.enemy(rew.grade)

        if 0.5 <= rew.grade <= 4 and rew.score >= 0 and i <= 18 and timmer.timer_ingame >= 0:
            if oChoice_1.is_clicked():
                if ran_list[0] == check_Q[i][0]:
                    print("Choice 1 Button Clicked!")
                    rew.reward_up()
                    rew.show_grade()
                    list_choice.clear()
                    i += 1
                    list_choice += [check_Q[i][0], check_c[i*3], check_c[i*3+1], check_c[i*3+2]]
                    ran_list = random.sample(list_choice, k = 4)
                    timmer.time_reset()
                    bg_i += 1
                    continue
                elif ran_list[0] != check_Q[i][0]:
                    print("Choice 1 Button Clicked!")
                    rew.reward_down()
                    rew.show_grade()
                    list_choice.clear()
                    i += 1
                    list_choice += [check_Q[i][0], check_c[i*3], check_c[i*3+1], check_c[i*3+2]]
                    ran_list = random.sample(list_choice, k = 4)
                    timmer.time_reset()
                    bg_i += 1
                    continue
                else:
                    pass
            if oChoice_2.is_clicked():
                if ran_list[1] == check_Q[i][0]:
                    print("Choice 2 Button Clicked!")
                    rew.reward_up()
                    rew.show_grade()
                    list_choice.clear()
                    i += 1
                    list_choice += [check_Q[i][0], check_c[i*3], check_c[i*3+1], check_c[i*3+2]]
                    ran_list = random.sample(list_choice, k = 4)
                    timmer.time_reset()
                    bg_i += 1
                    continue
                elif ran_list[1] != check_Q[i][0]:
                    print("Choice 2 Button Clicked!")
                    rew.reward_down()
                    rew.show_grade()
                    list_choice.clear()
                    i += 1
                    list_choice += [check_Q[i][0], check_c[i*3], check_c[i*3+1], check_c[i*3+2]]
                    ran_list = random.sample(list_choice, k = 4)
                    timmer.time_reset()
                    bg_i += 1
                    continue
                else:
                    pass
            if oChoice_3.is_clicked():
                if ran_list[2] == check_Q[i][0]:
                    print("Choice 3 Button Clicked!")
                    rew.reward_up()
                    rew.show_grade()
                    list_choice.clear()
                    i += 1
                    list_choice += [check_Q[i][0], check_c[i*3], check_c[i*3+1], check_c[i*3+2]]
                    ran_list = random.sample(list_choice, k = 4)
                    timmer.time_reset()
                    bg_i += 1
                    continue
                elif ran_list[2] != check_Q[i][0]:
                    print("Choice 3 Button Clicked!")
                    rew.reward_down()
                    rew.show_grade()
                    list_choice.clear()
                    i += 1
                    list_choice += [check_Q[i][0], check_c[i*3], check_c[i*3+1], check_c[i*3+2]]
                    ran_list = random.sample(list_choice, k = 4)
                    timmer.time_reset()
                    bg_i += 1
                    continue
                else:
                    pass
            if oChoice_4.is_clicked():
                if ran_list[3] == check_Q[i][0]:
                    print("Choice 4 Button Clicked!")
                    rew.reward_up()
                    rew.show_grade()
                    list_choice.clear()
                    i += 1
                    list_choice += [check_Q[i][0], check_c[i*3], check_c[i*3+1], check_c[i*3+2]]
                    ran_list = random.sample(list_choice, k = 4)
                    timmer.time_reset()
                    bg_i += 1
                    continue
                elif ran_list[3] != check_Q[i][0]:
                    print("Choice 4 Button Clicked!")
                    rew.reward_down()
                    rew.show_grade()
                    list_choice.clear()
                    i += 1
                    list_choice += [check_Q[i][0], check_c[i*3], check_c[i*3+1], check_c[i*3+2]]
                    ran_list = random.sample(list_choice, k = 4)
                    timmer.time_reset()
                    bg_i += 1
                    continue
                else:
                    pass
        else:
            i = 0
            list_choice.clear()
            Q_A_check = qusetion_eqution_answer(Need_total_Qusetion=7, choice=21)
            check_Q, check_c = Q_A_check.check_qusetion()

            list_choice += [check_Q[i][0], check_c[i*3], check_c[i*3+1], check_c[i*3+2]]
            ran_list = random.sample(list_choice, k = 4)
            time.sleep(0.3)
            run = result(rew.grade,rew.score)
            rew.reset_reward()
            timmer.time_reset()
            bg_i += 1
            continue

        # Update the screen
        timmer.draw_time()
        pygame.display.flip()


