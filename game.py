import pygame
from pygame.locals import *
from map import *
from macgyver import *

class Game:

    def __init__(self):
        pygame.init()
        

    def run(self):
        map = Map("level.txt")
        map.load_maze()
        map.pos_items()
        window = pygame.display.set_mode((ROWS*SPRITE_SIZE, COLUMNS*SPRITE_SIZE))
        map.display(window)
        macg_img = pygame.image.load('ressource/macgyver.png').convert_alpha()
        macg = MG(map, macg_img)

        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        macg.move_down()
                    if event.key == K_UP:
                        macg.move_up()
                    if event.key == K_RIGHT:
                        macg.move_right()
                    if event.key == K_LEFT:
                        macg.move_left()
            
            window.fill((0, 0, 0))
            map.display(window)            
            window.blit(macg.image, (macg.x, macg.y))
            pygame.display.update()


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
