import pygame
from pygame.locals import *
import time

class RadioButton(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, image_path,):
        super().__init__() 
        self.border_radius = 15
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, (w, h))
        
        self.button_image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.button_image.fill((0, 0, 0, 0))
        self.button_image.blit(image, image.get_rect(center=(w // 2, h // 2)))

        self.hover_image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.hover_image.fill((0, 0, 0, 0))
        self.hover_image.blit(image, image.get_rect(center=(w // 2, h // 2)))
        pygame.draw.rect(self.hover_image, (0, 153, 219), self.hover_image.get_rect(), 3, border_radius=self.border_radius)

        self.clicked_image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.clicked_image.fill((0, 0, 0, 0))
        self.clicked_image.blit(image, image.get_rect(center=(w // 2, h // 2)))

        self.image = self.button_image
        self.rect = self.button_image.get_rect(center = (x,y))

        self.clicked = False
        self.buttons = None
        self.flash_timer = 0  
        self.flash_on = False

    def setRadioButtons(self, buttons):
        self.buttons = buttons

    def update(self, event_list):
        hover = self.rect.collidepoint(pygame.mouse.get_pos())
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover and event.button == 1:
                    for rb in self.buttons:
                        rb.clicked = False
                        rb.flash_timer = 0
                        rb.flash_on = False
                    self.clicked = True
                    
        
        self.image = self.button_image

        if self.clicked:
            
            self.flash_timer += 1
            if self.flash_timer >= 20:
                self.flash_on = not self.flash_on
                self.flash_timer = 0

            if self.flash_on:
                self.image = self.clicked_image.copy()
                pygame.draw.rect(self.image, (254, 174, 52), self.image.get_rect(), 3, border_radius=self.border_radius)
            else:
                self.image = self.clicked_image

        elif hover:
        
            self.image = self.hover_image

class Button:
    def __init__(self, screen, pos, up_image, down_image, size = None):
        self.screen = screen
        self.image_up = pygame.image.load(up_image).convert_alpha()
        self.image_down = pygame.image.load(down_image).convert_alpha()
        
        if size:
            self.image_up = pygame.transform.scale(self.image_up, size)
            self.image_down = pygame.transform.scale(self.image_down, size)
        
        self.image = self.image_up
        self.rect = self.image.get_rect(center=pos)
        self.clicked = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_down
            if mouse_pressed[0] and not self.clicked:
                self.clicked = True
                return True
        else:
            self.image = self.image_up
        
        if not mouse_pressed[0]:
            self.clicked = False
        
        return False
    
class Choice:
    def __init__(self, screen, pos, up_image, down_image, font_size, size = None):
        self.screen = screen
        self.image_up = pygame.image.load(up_image).convert_alpha()
        self.image_down = pygame.image.load(down_image).convert_alpha()

        if size:
            self.image_up = pygame.transform.scale(self.image_up, size)
            self.image_down = pygame.transform.scale(self.image_down, size)
        
        self.font_size = font_size
        self.image = self.image_up
        self.rect = self.image.get_rect(center = pos)
        self.clicked = False

    def draw(self,name):
        if len(name) <= 23 :
            self.font_size = 20
        else:
            self.font_size = 16
        self.font = pygame.font.Font('k2d/K2D-Light.ttf', self.font_size)
        text = self.font.render(name, True, (0, 0, 0))
        texttile = text.get_rect(center=self.rect.center)

        self.screen.blit(self.image, self.rect)
        self.screen.blit(text, texttile)

    def is_clicked(self):
        # Check if button is clicked
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image_down
            if mouse_pressed[0] and not self.clicked:
                self.clicked = True
                return True
        else:
            self.image = self.image_up
        
        if not mouse_pressed[0]:
            self.clicked = False
        
        return False
    
class TextBox():
    def __init__(self, screen, width, height, position, text, font_size=16, color=(102, 102, 102, 225), text_color=(225, 225, 225), transparency=0.75):
        
        self.screen = screen
        self.width = width
        self.height = height
        self.x, self.y = position
        self.color = (color[0], color[1], color[2], int(225 * transparency))
        self.text = text
        self.text_color = text_color
        self.rect_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        if len(self.text) <= 13:
            self.font_size = 40
        elif 13 < len(self.text) <= 26:
            self.font_size = 20
        elif 26 < len(self.text) <= 31:
            self.font_size = 16
        else:
            self.font_size = 16
        self.font = pygame.font.Font('k2d/K2D-Bold.ttf', self.font_size)
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_x = (self.width - self.text_surface.get_width()) // 2
        self.text_y = (self.height - self.text_surface.get_height()) // 2
    def draw(self):

        self.rect_surface.fill((0, 0, 0, 0))
        pygame.draw.rect(self.rect_surface, self.color, pygame.Rect(0, 0, self.width, self.height), border_radius=10)
        self.rect_surface.blit(self.text_surface, (self.text_x, self.text_y))
        self.screen.blit(self.rect_surface, (self.x, self.y))

class c_reward():
    def __init__(self) -> None:
        self.score = 0
        self.grade = 0.5
    def reward_up(self):
        self.score += 10
        self.grade += 0.5
    def reward_down(self):
        self.score -= 10
        self.grade -= 0.5
    def reset_reward(self):
        self.score = 0
        self.grade = 0.5
    def show_grade(self):
        print(self.grade, self.score)

class c_timer():
    def __init__(self, screen, mode):
        if mode == "easy" or mode == "normol":
            self.time_set = 7*60
        else:
            self.time_set = 5*60
        self.timer_ingame = self.time_set
        self.screen = screen
        # self.font = pygame.font.Font('k2d/K2D-Bold.ttf', 20)
        self.color = (255,255,255)
        self.timer_ingame = self.time_set
    def draw_time(self):
        self.timer_ingame -= 3
        clock = pygame.image.load('images/clock.png').convert_alpha()
        clock =  pygame.transform.scale(clock, (40, 40))
        self.screen.blit(clock, (720-672,45))
        pygame.draw.rect(self.screen,(255,0,0),[(720 - 554) // 2, 720-662,582,24], 2)
        pygame.draw.rect(self.screen,self.color,[(720 - 550) // 2, 720-660,(580/self.time_set)*(self.timer_ingame),20])
    def time_reset(self):
        self.timer_ingame = self.time_set

class animetion():
    def __init__(self,screen):
        self.count = 4
        self.screen = screen
        self.pos_enemy = ((720) // 3)
        self.count = 1
        self.y = 1
    def walking(self,num):
        man = pygame.image.load(f'images/animetion/raning{num}.png').convert_alpha()
        man =  pygame.transform.scale(man, (100, 100))
        self.screen.blit(man, ((720-550) // 2, (720-50) // 2))
    def enemy(self,grade):
        if self.count % 15 == 0:
            self.y *= -1
        self.count += 1
        self.pos_enemy += 1.5*self.y
        if grade < 1:
            enemy = pygame.image.load(f'images/enemy/F.png').convert_alpha()
            plus = False
        elif grade == 1.0:
            enemy = pygame.image.load(f'images/enemy/D.png').convert_alpha()
            plus = False
        elif grade == 1.5:
            enemy = pygame.image.load(f'images/enemy/D.png').convert_alpha()
            plus = True
        elif grade == 2.0:
            enemy = pygame.image.load(f'images/enemy/C.png').convert_alpha()
            plus = False
        elif grade == 2.5:
            enemy = pygame.image.load(f'images/enemy/C.png').convert_alpha()
            plus = True
        elif grade == 3.0:
            enemy = pygame.image.load(f'images/enemy/B.png').convert_alpha()
            plus = False
        elif grade == 3.5:
            enemy = pygame.image.load(f'images/enemy/B.png').convert_alpha()
            plus = True
        else:
            enemy = pygame.image.load(f'images/enemy/A.png').convert_alpha()
            plus = False
        enemy =  pygame.transform.scale(enemy, (200, 200))
        if plus:
            enemy_plus = pygame.image.load(f'images/enemy/plus.png').convert_alpha()
            enemy_plus = pygame.transform.scale(enemy_plus, (50, 50))
            self.screen.blit(enemy_plus, (720-90, self.pos_enemy))
        self.screen.blit(enemy, (720-250, self.pos_enemy))