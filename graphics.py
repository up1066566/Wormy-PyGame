import pygame
from constants import *
from logic import Board
from terminate import *

class Render:
    
    def __init__(self, display_surface: pygame.Surface):
        self.display_surface = display_surface
        
    
    def draw_board(self, logic_board: Board) -> None:
        
        self.display_surface.fill(BGCOLOR)
        pygame.draw.rect(self.display_surface, DARKGRAY, (0,0, WINDOWWIDTH+EXTRABORDER, WINDOWHEIGHT+EXTRABORDER), EXTRABORDER//2)
        for index, (row, column) in enumerate(logic_board.wormy):
            if index == (logic_board.wormy_size-1):
                self.draw_wormy(row,column, True)
            else:
                self.draw_wormy(row,column, False)
        apple_row, apple_column = logic_board.apple
        self.draw_apple(apple_row, apple_column)
        
    
    def draw_wormy(self, row: int, column: int, head: bool = True) -> None:
        # board_x = BOARDWIDTH//2
        # board_y = BOARDHEIGHT//2
        x = column * CELLSIZE + EXTRABORDER//2
        y = row * CELLSIZE + EXTRABORDER//2

        if head:
            pygame.draw.ellipse(self.display_surface, WHITE, (x,y, CELLSIZE, CELLSIZE))
        else:
            pygame.draw.ellipse(self.display_surface, DARKGREEN, (x,y, CELLSIZE, CELLSIZE))
        pygame.draw.ellipse(self.display_surface, GREEN, (x,y, CELLSIZE, CELLSIZE), 3*CELLSIZE//8)
        pygame.draw.ellipse(self.display_surface, DARKGREEN, (x,y, CELLSIZE, CELLSIZE), CELLSIZE//6)
    
        
    
    def draw_apple(self, row, column) -> None:
        x = column * CELLSIZE+EXTRABORDER//2 + CELLSIZE//2
        y = row * CELLSIZE+EXTRABORDER//2 + CELLSIZE//2
        pygame.draw.circle(self.display_surface, RED, (x,y), CELLSIZE//3)
      
        
    @staticmethod    
    def generate_text(text: str, color: tuple[int, int, int],
                  bgcolor: tuple[int,int,int]|None = None,
                  font_size = 30,
                  bold = False,
                  font_style = 'freesansbold.ttf'):
        text_fonts = pygame.font.Font(font_style, font_size)
        text_fonts.set_bold(bold)
        text_surface = text_fonts.render(text, True, color, bgcolor)
        text_rect = text_surface.get_rect()
        return text_surface, text_rect
    
    
    def draw_text(self, text_surface: pygame.Surface, text_rect : pygame.Rect|None = None, 
                  center : tuple[int,int]|None = None,
                  topleft: tuple[int,int]|None = None):
        
                if text_rect is None:
                    text_rect = text_surface.get_rect()
                
                if center is not None:
                    text_rect.center = center
                elif topleft is not None:
                    text_rect.topleft = topleft
                else:
                    text_rect.center = ((WINDOWWIDTH+EXTRABORDER)//2, (WINDOWHEIGHT+EXTRABORDER)//2)
                
                self.display_surface.blit(text_surface, text_rect)
        
    def draw_pause(self):
        pause_surface = self.display_surface.copy()
        pause_surface.fill(WHITE)
        pause_surface.convert_alpha()
        pause_surface.set_alpha(100)
        self.display_surface.blit(pause_surface, pause_surface.get_rect())
        text_surf, text_rect = self.generate_text('Paused', WHITE, font_size = 100, bold = True)
        self.draw_text(text_surf, text_rect)
    

        
def test():
    pygame.init()
    fps_clock = pygame.time.Clock()
    display_surface = pygame.display.set_mode((WINDOWWIDTH + EXTRABORDER, WINDOWHEIGHT + EXTRABORDER))
    pygame.display.set_caption('Move Test')
    board = Board()
    render = Render(display_surface)
    while True:
        board.generate_board()
        render.draw_board(board)
        print(board.wormy)
        print(board.apple)
        print(board.direction)
        
        Terminate.check_for_quit()
        
        pygame.display.update()
        pygame.time.wait(2000)
        #fps_clock.tick(1)

if __name__ == "__main__":
    test()
                