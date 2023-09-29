import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE
#import same level folder then use "."

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        
    def draw_cubes(self, window):               #Hàm draw_cubes với hai tham số là self và window      
        window.fill(BLACK)
        for row in range(ROWS):                 #vòng lặp 0 -> 8 (ROWS), lấy số vòng lặp chia lấy dư cho 2
            for col in range(row % 2, ROWS, 2): #Lấy dư sẽ chỉ ra 0 và 1
                pygame.draw.rect(window, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))