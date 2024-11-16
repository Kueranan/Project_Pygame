import pygame
from pygame.locals import *
import sys

from button import *
from mode_button import *
from easy_mode import *
from normal_mode import *
from hard_mode import *

timestamp = 0

def main_menu():
    global timestamp

    pygame.init()
    pygame.mixer.init()

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load('massobeats - honey jam.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=-1, start=timestamp, fade_ms=2000) 

    WIDTH = 720
    HEIGHT = 720

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('"A" Experience English I')
    
    background = pygame.image.load('images/university.jpeg').convert_alpha()
    background=  pygame.transform.scale(background, (WIDTH, HEIGHT))
    rect_surface = pygame.Surface((720, 720), pygame.SRCALPHA)  
    rect_color = (102, 102, 102, 150)
    pygame.draw.rect(rect_surface, rect_color, pygame.Rect(0, 0, 620, 620), border_radius=10)
    title = pygame.image.load('images/title.png').convert_alpha()
    title =  pygame.transform.scale(title, (450, 50))

    choice_size = (300, 175)
    oStart = Button(screen, (WIDTH//2, HEIGHT//2), 'images/start.png', 'images/start_down.png', size = choice_size)
    radioButtons = [ 
        RadioButton(WIDTH//4, HEIGHT*0.75, 120, 80, 'images/easy.png'),
        RadioButton(WIDTH//2, HEIGHT*0.75, 120, 80, 'images/normal.png'),
        RadioButton(WIDTH*3//4, HEIGHT*0.75, 120, 80, 'images/hard.png')
    ]
    for rb in radioButtons:
        rb.setRadioButtons(radioButtons)
    radioButtons[1].clicked = True
    group = pygame.sprite.Group(radioButtons)


    run = True
    while run:

        clock.tick(60)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(2000)
                run = False
               
        group.update(event_list)   

        if oStart.is_clicked():
            pygame.mixer.music.fadeout(2000)
            timestamp = pygame.mixer.music.get_pos() / 1000
            if radioButtons[0].clicked:
                print("Easy mode selected")
                easy_mode()
            elif radioButtons[1].clicked:
                print("Normal mode selected")
                normal_mode()
            elif radioButtons[2].clicked:
                print("Hard mode selected")
                hard_mode()


        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(loops=-1, start=timestamp, fade_ms=2000)

        screen.fill(0)
        screen.blit(background, background.get_rect())
        screen.blit(rect_surface, (50, 50))
        screen.blit(title, (WIDTH//2-225,HEIGHT*0.25))
        oStart.draw()
        group.draw(screen)


        pygame.display.flip()

    pygame.mixer.music.fadeout(2000)

        
main_menu()

pygame.mixer.music.stop()
pygame.quit()
sys.exit()

