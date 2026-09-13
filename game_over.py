import pygame


from constants import * 
from graphics import *
from terminate import *
from states import *
from graphics import *

class GameOver:
    def __init__(self, display_surface: pygame.Surface, render: Render):
        self.display_surface = display_surface

        self.render = render
        self.next_state = None
        self.rects = [None,None]
        
    def game_over_screen(self):
        game_over_surface = self.display_surface.copy()
        game_over_surface.fill(DARKGREEN)
        game_over_surface.convert_alpha()
        game_over_surface.set_alpha(40)
        self.display_surface.blit(game_over_surface, game_over_surface.get_rect())
    
    
    def draw_texts(self):
        text_surf, text_rect = self.render.generate_text('GAME OVER', GREEN, font_size = 70, bold = True)
        text_rect.midtop = ((WINDOWWIDTH+EXTRABORDER)//2, 20)
        self.render.draw_text(text_surf, text_rect, text_rect.center)
        
        text_surf, text_rect = self.render.generate_text('Replay', GREEN, DARKGREEN, font_size = 40, bold = True)
        text_rect.midtop =  ((WINDOWWIDTH+EXTRABORDER)//2, 2*WINDOWHEIGHT//5)
        self.rects[0] = text_rect
        self.render.draw_text(text_surf, text_rect, text_rect.center)
        
        text_surf, text_rect = self.render.generate_text('Main Menu', GREEN, DARKGRAY, font_size = 40, bold = True)
        text_rect.midtop = ((WINDOWWIDTH+EXTRABORDER)//2, 3*WINDOWHEIGHT//5)
        self.rects[1] = text_rect
        self.render.draw_text(text_surf, text_rect, text_rect.center)
        
    
    def choose_next_state(self):
        for event in pygame.event.get(MOUSEBUTTONUP):
            mouse_x, mouse_y = event.pos
            if self.rects[0].collidepoint(mouse_x, mouse_y):
                self.next_state = State.GAME
                return
            elif self.rects[1].collidepoint(mouse_x, mouse_y):
                self.next_state = State.MENU
                return
        
    
def test():
    pygame.init()
    fps_clock = pygame.time.Clock()
    display_surface = pygame.display.set_mode((WINDOWWIDTH+EXTRABORDER, WINDOWHEIGHT+EXTRABORDER))
    pygame.display.set_caption('Menu Test')
    render = Render(display_surface)
    game_over = GameOver(display_surface, render)
    game_over.game_over_screen()
    game_over.draw_texts()
    pygame.display.update()
    
    while True:
        Terminate.check_for_quit()
        game_over.choose_next_state()
        if game_over.next_state:
            print(game_over.next_state)
            game_over.next_state = None
        fps_clock.tick(FPS)
            
    
    

if __name__ == "__main__":
    test()
    