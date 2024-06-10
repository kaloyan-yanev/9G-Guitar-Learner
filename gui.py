import pygame
from button import Button
import sys

pygame.init()

screen = pygame.display.set_mode((2560, 1440),
                                 pygame.FULLSCREEN)
pygame.display.set_caption("GuitarLearner")

Logo = pygame.image.load("assets/logo.jpg")
pygame.display.set_icon(Logo)

def font(size):
    return pygame.font.Font("assets/AIR_____.TTF", size)

def play():
    while True:

        play_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        play_text = font(200).render("This is the PLAY screen.", True, "White")
        play_rect = play_text.get_rect(topleft = (100,0))
        screen.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(100, 275), 
                            text_input="BACK", font=font(200), base_color="White", hovering_color="Green")

        play_back.changeColor(play_mouse_pos)
        play_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(play_mouse_pos):
                    main_menu()

        pygame.display.update()

def options():
    while True:
        options_mouse_pos = pygame.mouse.get_pos()

        screen.fill("white")

        options_text = font(200).render("This is the OPTIONS screen.", True, "Black")
        options_rect = options_text.get_rect(topleft=(100,0))
        screen.blit(options_text, options_rect)

        options_back = Button(image=None, pos=(100, 275), 
                            text_input="BACK", font=font(200), base_color="Black", hovering_color="Green")

        options_back.changeColor(options_mouse_pos)
        options_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.checkForInput(options_mouse_pos):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        screen.fill("black")

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = font(200).render("MAIN MENU", True, "white")
        menu_rect = menu_text.get_rect(topleft = (100,0))

        play_button = Button(None, pos = (100, 275), text_input="PLAY", font = font(200), base_color = "white", hovering_color="Green")
        options_button = Button(None, pos = (100, 525), text_input="OPTIONS", font = font(200), base_color = "white", hovering_color="Green")
        quit_button = Button(None, pos = (100, 775), text_input="QUIT", font = font(200), base_color = "white", hovering_color="Green")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play()
                if options_button.checkForInput(menu_mouse_pos):
                    options()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()