import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
FPS = 60
"""
using __init__.py in main and subfolder to
tell "checkers" folder is a python packages
"""

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Checkers')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass 
        board.draw_cubes(WIN)
        pygame.display.update()
           
    pygame.quit()

main()
    

