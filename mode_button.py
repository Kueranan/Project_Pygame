import pygame

class RadioButton(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, image_path):
        super().__init__() 
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, (w, h))
        
        self.button_image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.button_image.fill((96, 96, 96, 255))
        self.button_image.blit(image, image.get_rect(center=(w // 2, h // 2)))

        self.hover_image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.hover_image.fill((96, 96, 96, 255))
        self.hover_image.blit(image, image.get_rect(center=(w // 2, h // 2)))
        pygame.draw.rect(self.hover_image, (0, 153, 219), self.hover_image.get_rect(), 3)

        self.clicked_image = pygame.Surface((w, h), pygame.SRCALPHA)
        self.clicked_image.fill((96, 196, 96, 255))
        self.clicked_image.blit(image, image.get_rect(center=(w // 2, h // 2)))

        self.image = self.button_image
        self.rect = pygame.Rect(x, y, w, h)
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
                pygame.draw.rect(self.image, (254, 174, 52), self.image.get_rect(), 3)
            else:
                self.image = self.clicked_image

        elif hover:
        
            self.image = self.hover_image
 


