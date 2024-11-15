import pygame
from pygame.locals import *
import sys

from choice import *
from text_box import *


def normal_mode():

    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Normal mode')

    WIDTH = 600
    HEIGHT = 600

    background = pygame.image.load('images/sun.jpeg').convert_alpha()
    background=  pygame.transform.scale(background, (WIDTH, HEIGHT*2//3))

    question_box = TextBox(screen, width=400, height=60, position=((WIDTH - 400) // 2, HEIGHT // 6), text="Insert Question Here")

    font_size = 20
    choice_size = (200, 60)
    oChoice_1 = Choice(screen, (WIDTH*1.5//5, HEIGHT*7.5//10), 'images/choice.png', 'images/choice_down.png', font_size, "Insert Choice 1 Here", size = choice_size)
    oChoice_2 = Choice(screen, (WIDTH*3.5//5, HEIGHT*7.5//10), 'images/choice.png', 'images/choice_down.png', font_size, "Insert Choice 2 Here", size = choice_size)
    oChoice_3 = Choice(screen, (WIDTH*1.5//5, HEIGHT*9//10), 'images/choice.png', 'images/choice_down.png', font_size, "Insert Choice 3 Here", size = choice_size)
    oChoice_4 = Choice(screen, (WIDTH*3.5//5, HEIGHT*9//10), 'images/choice.png', 'images/choice_down.png', font_size, "Insert Choice 4 Here", size = choice_size)

    # Game loop
    run = True
    while run:

        clock.tick(60)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False

        screen.fill((154, 103, 82))

        screen.blit(background, background.get_rect())
        question_box.draw()
        oChoice_1.draw()
        oChoice_2.draw()
        oChoice_3.draw()
        oChoice_4.draw()
        
        if oChoice_1.is_clicked():
            print("Choice 1 Button Clicked!")
        if oChoice_2.is_clicked():
            print("Choice 2 Button Clicked!")
        if oChoice_3.is_clicked():
            print("Choice 3 Button Clicked!")
        if oChoice_4.is_clicked():
            print("Choice 4 Button Clicked!")

        # Update the screen
        pygame.display.flip()


