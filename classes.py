import pygame
import pandas
import sys

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(topleft=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

class Notes:
    def __init__ (self, screen, note_image, note_pos, note_font, note_text_input, note_color, beat_marker_y):
        self.screen = screen
        self.note_image = note_image
        self.notes_x = note_pos[0]
        self.notes_y = note_pos[1]
        self.notes_font = note_font
        self.notes_text_input = note_text_input
        self.notes_color = note_color
        self.notes_text = self.notes_font.render(self.notes_text_input, True, self.notes_color)
        if self.note_image is None:
            self.note_image = self.notes_text
        self.note_image = pygame.transform.scale(self.note_image, (50, 50))
        self.notes = self.note_image.get_rect()
        self.hit = False
        self.note_speed = beat_marker_y/120

    def move(self):
        self.notes.y = self.notes.y + self.note_speed
        if self.notes.y > self.screen.get_height() and not self.hit:
            print('Missed!')
            self.hit = True  

    def draw(self):
        self.screen.blit(self.note_image, (self.notes.x , self.notes.y))

    def hit(self, beat_marker):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and not self.hit:
                if event.key == pygame.K_SPACE:
                    if beat_marker.colliderect(self.notes):
                        print('Hit!')
                        self.hit = True                
        return self.hit