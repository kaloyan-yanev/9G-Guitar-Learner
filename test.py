import pygame
from classes import *
import sys

pygame.init()
                

screen = pygame.display.set_mode((2560, 1440))
pygame.display.set_caption("GuitarLearner")

Logo = pygame.image.load("assets/logo.jpg")
pygame.display.set_icon(Logo)

beat_marker = pygame.Rect ( screen.get_width() // 2, screen.get_height() - 200, screen.get_width() // 2 - 475, 30)
 
hit = False

note = Notes(screen, 'assets/note.png' , 5)

rect_1 = pygame.Rect(screen.get_width() // 2 + 100, 0, 10, screen.get_height())
rect_2 = pygame.Rect(screen.get_width() // 2 + 200, 0, 10, screen.get_height())
rect_3 = pygame.Rect(screen.get_width() // 2 + 300, 0, 10, screen.get_height())
rect_4 = pygame.Rect(screen.get_width() // 2 + 400, 0, 10, screen.get_height())
rect_5 = pygame.Rect(screen.get_width() // 2 + 500, 0, 10, screen.get_height())
rect_6 = pygame.Rect(screen.get_width() // 2 + 600, 0, 10, screen.get_height())
rect_7 = pygame.Rect(screen.get_width() // 2 + 700, 0, 10, screen.get_height())

running = True
while running:
    note.Hit(beat_marker)
    screen.fill("black")

    note.move()
    note.draw()
    
    pygame.draw.rect(screen, "red", beat_marker)
    pygame.draw.rect(screen, "gray", rect_1)
    pygame.draw.rect(screen, "gray", rect_2)
    pygame.draw.rect(screen, "gray", rect_3)
    pygame.draw.rect(screen, "gray", rect_4)
    pygame.draw.rect(screen, "gray", rect_5)
    pygame.draw.rect(screen, "gray", rect_6)
    pygame.draw.rect(screen, "gray", rect_7)


    pygame.time.Clock().tick(60)

    pygame.display.update()