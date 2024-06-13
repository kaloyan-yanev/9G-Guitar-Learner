import pygame
from classes import Button
import sys

pygame.init()

screen = pygame.display.set_mode((2560, 1440))
pygame.display.set_caption("GuitarLearner")

Logo = pygame.image.load("assets/logo.jpg")
pygame.display.set_icon(Logo)

screen_height = 1440
screen.blit(Logo, (0,0))

while True:

            BLACK = (0, 0, 0)
            WHITE = (255, 255, 255)
            RED = (255, 0, 0)

            note_image = pygame.image.load('assets/note.png')
            note_image = pygame.transform.scale(note_image, (200, 200))
            beat_marker = pygame.Rect ( 0, 1440 + 100, 2560, 50)

            note_speed = 5
            notes = note_image.get_rect()
            hit = False

            screen.blit(note_image, (notes.x , notes.y))
            pygame.draw.rect(screen, RED, beat_marker)

            pygame.display.update
 
            running = True
            while running:
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if beat_marker.colliderect(notes):
                                print('Hit!')
                                hit = True
                                
                screen.fill("black")

                if not hit:
                    notes.y = notes.y + note_speed
                    if notes.y > 1440:
                        print('Missed!')
                        
                
                screen.blit(note_image, (notes.x , notes.y))
                pygame.draw.rect(screen, RED, beat_marker)
                
                pygame.time.Clock().tick(60)

                pygame.display.update