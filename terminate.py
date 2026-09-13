# Copy paste this file to every game uses pygame to terminate it with X button or ESC key
from constants import *
import pygame, sys
from pygame.locals import *

class Terminate:
    
    @staticmethod
    def terminate():
        pygame.quit()
        sys.exit()
        
        
    @staticmethod    
    def check_for_quit()-> None:
        for event in pygame.event.get(QUIT): # get all the QUIT events
            Terminate.terminate()

        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                Terminate.terminate()
            pygame.event.post(event) # put the other KEYUP event objects back into the event queue
            
def test():
    pygame.init()
    fps_clock = pygame.time.Clock()
    display_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Terminate Test')
    
    while True:
        Terminate.check_for_quit()
    

if __name__ == "__main__":
    test()
