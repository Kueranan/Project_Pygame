import pygame
from pygame.locals import *
import sys

from button import *
from mode_button import *
from easy_mode import *
from normal_mode import *
from hard_mode import *


def main_menu():

    pygame.init()

    WIDTH = 720
    HEIGHT = 720

    # Create Game Window
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    font20 = pygame.font.SysFont(None, 20)
    pygame.display.set_caption('"A" Experience English I')

    
    background = pygame.image.load('images/university.jpeg').convert_alpha()
    background=  pygame.transform.scale(background, (WIDTH, HEIGHT))
    title = pygame.image.load('images/title.png').convert_alpha()
    title =  pygame.transform.scale(title, (400, 40))

    rect_surface = pygame.Surface((720, 720), pygame.SRCALPHA)  
    rect_color = (102, 102, 102, 150)
    pygame.draw.rect(rect_surface, rect_color, pygame.Rect(0, 0, 620, 620), border_radius=10)

    oStart_Button = Button(screen, (WIDTH/2, HEIGHT/2), 'images/start.png', 'images/start_down.png')
    radioButtons = [ 
        RadioButton(WIDTH//4-60, 500, 120, 80, 'images/easy.jpeg'),
        RadioButton(WIDTH//2-60, 500, 120, 80, 'images/common.jpeg'),
        RadioButton(WIDTH*3//4-60, 500, 120, 80, 'images/hard.jpeg')
    ]
    for rb in radioButtons:
        rb.setRadioButtons(radioButtons)

    radioButtons[1].clicked = True

    group = pygame.sprite.Group(radioButtons)


    # Game loop
    run = True
    while run:

        clock.tick(60)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
               
        group.update(event_list)   

        if oStart_Button.is_clicked():
            if radioButtons[0].clicked:
                print("Easy mode selected")
                easy_mode()
            elif radioButtons[1].clicked:
                print("Normal mode selected")
                normal_mode()
            elif radioButtons[2].clicked:
                print("Hard mode selected")
                hard_mode()

        screen.fill(0)
        screen.blit(background, background.get_rect())
        screen.blit(rect_surface, (50, 50))
        screen.blit(title, (125,175))
        oStart_Button.draw()
        group.draw(screen)


        # Update the screen
        pygame.display.flip()

        
main_menu()

pygame.quit()
sys.exit()

