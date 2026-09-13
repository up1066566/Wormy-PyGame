import pygame
from pygame.locals import *
from constants import *
from terminate import Terminate
from states import *
from graphics import Render


class Menu:
    def __init__(self, display_surface: pygame.Surface, fps_clock: pygame.time.Clock):
        self.display_surface = display_surface
        self.fps_clock = fps_clock
        self.options_list = {}
        self.level_selected = None

    
    def main_menu(self):
        self.options()
        self.draw_menu()
                    
    def draw_menu(self):
        # self.display_surface.fill(BGCOLOR)
        background_surface = self.display_surface.copy()
        background_surface.convert_alpha()
        background_rect = background_surface.get_rect()
        background_surface.set_alpha(100)
        background = Render(background_surface)
        main_menu = Render(self.display_surface)
        
        select_level_surface, select_level_rect = Render.generate_text('Select Level', WHITE, DARKGREEN,  50, True)
        select_level_rect.centerx = WINDOWWIDTH//2
        select_level_rect.top = 10
        
        title_text = 'Wormy!'
        title_surf_1, _ = Render.generate_text(title_text, WHITE, DARKGREEN, 100)
        title_surf_2, _ = Render.generate_text(title_text, GREEN, None, 100)

        
        degrees_1 = 0
        degrees_2 = 0
        
        while True:
            self.display_surface.fill(BGCOLOR)
            background_surface.fill(BGCOLOR)
            
            rotated_surf_1 = pygame.transform.rotate(title_surf_1, degrees_1)
            rotated_surf_2 = pygame.transform.rotate(title_surf_2, degrees_2)            
            
            background.draw_text(rotated_surf_1)
            background.draw_text(rotated_surf_2)
            
            background.draw_text(select_level_surface, select_level_rect, select_level_rect.center)
            
            
            self.display_surface.blit(background_surface, background_rect)
            
            for option in self.options_list:
                main_menu.draw_text(option, self.options_list[option], self.options_list[option].center)
                
            Terminate.check_for_quit()
            
            self.option_clicked()
            if self.level_selected:
                break
                
            pygame.display.update()
            
            self.fps_clock.tick(FPS)
            degrees_1+=3
            degrees_2+=5


    def options(self):
        
        for level in Level:    
            level_surf, level_rect = Render.generate_text(level.name,  GREEN, DARKGREEN)
            level_rect.centerx = (WINDOWWIDTH+EXTRABORDER)//2
            level_rect.centery = (WINDOWHEIGHT+EXTRABORDER)//2 + (level.value-1-len(Level)//2)*(level_rect.height+20)
            self.options_list[level_surf] = level_rect
            
        
    def option_clicked(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                for index, option in enumerate(self.options_list):
                    if self.options_list[option].collidepoint(mouse_x, mouse_y):
                        self.level_selected = Level(index+1)
        

def test():
    pygame.init()
    fps_clock = pygame.time.Clock()
    display_surface = pygame.display.set_mode((WINDOWWIDTH+EXTRABORDER, WINDOWHEIGHT+EXTRABORDER))
    pygame.display.set_caption('Menu Test')
    menu = Menu(display_surface, fps_clock)
    menu.main_menu()
    while True:
        menu.draw_menu()
        Terminate.check_for_quit()
        if menu.level_selected:
            print(menu.level_selected)
            menu.level_selected = None
        pygame.display.update()    
        fps_clock.tick(FPS)

    

if __name__ == "__main__":
    test()
        
        