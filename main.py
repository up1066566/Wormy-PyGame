import pygame
from pygame.locals import *

from constants import *
from states import *

from game import *
from menu import *
from game_over import *

from terminate import *

from logic import *
from graphics import *

def main():
    
    pygame.init()
    fps_clock = pygame.time.Clock()
    display_surface = pygame.display.set_mode((WINDOWWIDTH+EXTRABORDER, WINDOWHEIGHT+EXTRABORDER))
    pygame.display.set_caption('Wormy!')
    board = Board()
    board.generate_board()
    render = Render(display_surface)
    game = Game(display_surface, fps_clock, board)
    menu = Menu(display_surface, fps_clock)
    game_over = GameOver(display_surface, render)
    
    state = State.MENU
    
    menu.options()
    
    while True:
        if (state == State.MENU):
            menu.level_selected = None
            menu.draw_menu()
            
        if menu.level_selected:
            state = State.GAME
            game.start_game(menu.level_selected)
    
        
        while(state == State.GAME):
            Terminate.check_for_quit()
            game.pause()
            game.next_frame()
            if board.game_over_flag:
                state = State.GAME_OVER
                board.game_over_flag = False
                board.reset()
        
        if state == State.GAME_OVER:
            game_over.game_over_screen()
            game_over.draw_texts()
            pygame.display.update()
            
        while(state == State.GAME_OVER):
            Terminate.check_for_quit()
            game_over.choose_next_state()
            if game_over.next_state:
                state = game_over.next_state
                game_over.next_state = None
            fps_clock.tick(FPS)
        
        pygame.display.update()
        fps_clock.tick(FPS)
            
    

if __name__ == "__main__":
    main()