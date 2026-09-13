from constants import *
from states import *
import random
from collections import deque # FIFO policy with O(1) operations

# Why FIFO policy?
# We represent the wormy as a sequence of positions.
# The last element is the head, and the rest form the tail.
# Example:
# [1, 2, 3, 4, 5]   -> head is 5
# [2, 3, 4, 5, 6]   -> after moving, 5 becomes part of the tail and 6 is the new head
# Operations:
# add the new head at the back! 
# remove the old front element! 

# posistions won't be integers, but a tuple of x,y coordinnates.


class Board():
    def __init__(self):
        self.board = []
        self.wormy_size = 0
        self.wormy = deque([]) 
        self.direction = None
        self.apple = [None, None]
        self.game_over_flag = False
        self.eaten_apple_flag = False
        
        
    def generate_random_direction(self) -> Direction:   # tested
        direction = random.choice([d for d in Direction])
        return direction
    
    
    def generate_wormy(self, wormy_size: int = 5) -> None:  # tested
        self.wormy_size = wormy_size
        self.wormy = deque([])
        center = BOARDHEIGHT//2, BOARDWIDTH//2
        center_x, center_y = center
        # wormy_list.append((center_x,center_y))
        self.direction = self.generate_random_direction()
        
        match self.direction:
            case Direction.UP:              # wormy extends down
                for i in range(wormy_size):
                    self.wormy.appendleft((center_x+i, center_y))   
                    self.board[center_x+i][center_y] = Cell.WORMY_TAIL
                    
            case Direction.DOWN:            # wormy extends up
                for i in range(wormy_size):
                    self.wormy.appendleft((center_x-i, center_y))
                    self.board[center_x-i][center_y] = Cell.WORMY_TAIL
                    
            case Direction.LEFT:            # wormy extends right
                for i in range(wormy_size):
                    self.wormy.appendleft((center_x, center_y+i))
                    self.board[center_x][center_y+i] = Cell.WORMY_TAIL
                    
            case Direction.RIGHT:           # wormy extend left
                for i in range(wormy_size):
                    self.wormy.appendleft((center_x, center_y-i))
                    self.board[center_x][center_y-i] = Cell.WORMY_TAIL
                    
        self.board[center_x][center_y] = Cell.WORMY_HEAD
        
        
        
        
    def get_empty_coordinates(self) -> list[tuple[int, int]]:   # tested
        empty_coordinates = []
        for row in range(BOARDHEIGHT):
            for column in range(BOARDWIDTH):
                if self.board[row][column] == Cell.EMPTY_CELL:
                    empty_coordinates.append((row, column))
        return empty_coordinates
    
    
    def generate_apple(self) -> None:   # tested
        apple_x, apple_y = random.choice(self.get_empty_coordinates())
        self.apple[0], self.apple[1] = apple_x, apple_y
        self.board[apple_x][apple_y] = Cell.APPLE
        
    
    def generate_board(self) -> None:   # tested
        for row in range(BOARDHEIGHT):
            generated_row = []
            for column in range(BOARDWIDTH):
                generated_row.append(Cell.EMPTY_CELL)
            self.board.append(generated_row)
        
        self.generate_wormy()
        self.generate_apple()
        
    
    def eat_apple(self) -> None:    # tested
        self.board[self.wormy[-1][0]][self.wormy[-1][1]] = Cell.WORMY_TAIL
        self.board[self.apple[0]][self.apple[1]] = Cell.WORMY_HEAD
        self.wormy.append(tuple(self.apple))
        self.wormy_size += 1
        self.generate_apple()
    
    def reset(self) -> None:    # tested
        self.game_over_flag = False
        
        for row in range(BOARDHEIGHT):
            for column in range(BOARDWIDTH):
                self.board[row][column] = Cell.EMPTY_CELL   
                     
        self.generate_wormy()
        self.generate_apple()
    
    def move_to(self) -> None:  # tested
        self.eaten_apple_flag = False
        direction = self.direction
        head_x, head_y = self.wormy[-1]     # old head
        new_x, new_y = self.wormy[-1]       # new head
        last_x, last_y = self.wormy[0]      # old tail
        match direction:
            case Direction.UP:
                new_x -= 1
            case Direction.DOWN:
                new_x += 1
            case Direction.RIGHT:
                new_y += 1
            case Direction.LEFT:
                new_y -=1
        if new_x<0 or new_y<0 or new_x>=BOARDHEIGHT or new_y>=BOARDWIDTH:
            self.game_over_flag = True
            return
        cell_state = self.board[new_x][new_y]
        match cell_state:
            case Cell.WORMY_TAIL:
                self.game_over_flag = True
            case Cell.APPLE:
                self.eaten_apple_flag = True
                self.eat_apple()
            case Cell.EMPTY_CELL:
                self.board[head_x][head_y]  = Cell.WORMY_TAIL
                self.board[new_x][new_y]    = Cell.WORMY_HEAD
                self.board[last_x][last_y]  = Cell.EMPTY_CELL
                self.wormy.append((new_x, new_y))
                self.wormy.popleft()
                