from constants import *
from enum import *

class Cell(Enum):
    EMPTY_CELL = auto()
    WORMY_TAIL = auto()
    WORMY_HEAD = auto()
    APPLE = auto()
    
class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

# level affects snake speed
class Level(Enum):
    EASY = auto()  
    MEDIUM = auto()
    HARD = auto() 
    EXPERT = auto()  
    
class LevelFPS(Enum):
    EASY = FPS_EASY  
    MEDIUM = FPS_MEDIUM
    HARD = FPS_HARD
    EXPERT = FPS_EXPERT

class State(Enum):
    MENU = auto()
    GAME = auto()
    GAME_OVER = auto()