import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((2560, 1440),
                                 pygame.FULLSCREEN)

width = screen.get_width()
height = screen.get_height()

Icon = pygame.image.load("logo.jpg")
pygame.display.set_caption("GuitarLearner")
pygame.display.set_icon(Icon)

color = (80, 80, 80)
color_light = (175, 175, 175)
color_dark = (50, 50, 50)

smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('play song', True, color_light)

screen.fill(color)
pygame.display.flip()



exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
               
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 
    mouse = pygame.mouse.get_pos()
    
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
      
    screen.blit(text , (width/2+50,height/2)) 
     
    pygame.display.update() 
pygame.quit