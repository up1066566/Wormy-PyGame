import pygame
from pygame.locals import *

from constants import *
from states import *

from graphics import *
from logic import *
from move import *

from terminate import *

class Game:
    def __init__(self, display_surface: pygame.Surface, fps_clock: pygame.time.Clock, logic_board: Board):
        self.display_surf = display_surface
        self.fps_clock = fps_clock
        self.board = logic_board
        self.board.generate_board()
        self.move = Move(logic_board)
        self.render = Render(display_surface)
        self.pause_flag = False
        self.fps = FPS
    

    def start_game(self, level = Level.EASY):
        self.fps = LevelFPS[level.name].value
        if self.board.game_over_flag:
            self.board.reset()
        
    def update_pause_flag(self):
        for event in pygame.event.get(KEYUP):
            if event.key in (K_p, K_SPACE):
                self.pause_flag = not self.pause_flag
                return
            pygame.event.post(event)
        
    def pause(self):
        self.update_pause_flag()
        if self.pause_flag:
            self.render.draw_pause()
        while self.pause_flag:
            self.update_pause_flag()
            Terminate.check_for_quit()
            pygame.event.get(KEYDOWN)
            pygame.display.update()
        


    def next_frame(self):
        self.move.move_to()
        if self.board.eaten_apple_flag:
            self.fps+=1
        self.render.draw_board(self.board)
        self.fps_clock.tick(self.fps)
        pygame.display.update()
        

def test():
    pygame.init()
    fps_clock = pygame.time.Clock()
    display_surface = pygame.display.set_mode((WINDOWWIDTH+EXTRABORDER, WINDOWHEIGHT+EXTRABORDER))
    pygame.display.set_caption('Game Test')
    board = Board()
    game = Game(display_surface, fps_clock, board)
    while True:
        game.start_game(Level.EXPERT)
        game.pause()
        Terminate.check_for_quit()
        game.next_frame()
    
if __name__ == "__main__":
    test()