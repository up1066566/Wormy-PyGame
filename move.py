from constants import *
from states import *
import pygame
from pygame.locals import *
from terminate import *
from logic import *

class Move():
    def __init__(self, logic_board):
        self.logic_board = logic_board
    
        
    def choose_direction(self):
        direction = self.logic_board.direction
        for event in pygame.event.get(KEYDOWN):
            if direction in (Direction.LEFT, Direction.RIGHT):
                if event.key in (K_UP, K_w):
                    self.logic_board.direction = Direction.UP
                if event.key in (K_DOWN, K_s):
                    self.logic_board.direction = Direction.DOWN
                    
            if direction in (Direction.UP, Direction.DOWN):
                if event.key in (K_LEFT, K_a):
                    self.logic_board.direction = Direction.LEFT
                if event.key in (K_RIGHT, K_d):
                    self.logic_board.direction = Direction.RIGHT

    def move_to(self):
        self.choose_direction()
        self.logic_board.move_to()
        
        
        
def test():
    pygame.init()
    fps_clock = pygame.time.Clock()
    display_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Move Test')
    board = Board()
    board.generate_board()
    move = Move(board)
    while True:
        
        Terminate.check_for_quit()
        move.choose_direction()
        
        move.move_to()
        
        if board.game_over_flag == True:
            board.reset()
        print(board.wormy, board.direction)
        fps_clock.tick(1)

if __name__ == "__main__":
    test()
                