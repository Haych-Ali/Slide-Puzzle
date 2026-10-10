#board file 
import pygame
import random
import os

# Board logic for the sliding puzzle.
# This class stores the tile state, handles movement rules, and renders the board on screen.
class Board:
    def __init__(self,game_size, tile_size, screen ):
        self.game_size= game_size   #size of the board  for (3x3) it would be 3 
        self.tile_size = tile_size  # size of the tiles 
        self.screen = screen   #the screen to draw the baoard such as the grids and tiles
        self.grid = self.create_grid() #creates the grid 
        self.moves_made = 0      #counts number of moves mades
        self.best_moves = 0    #stores best move
        # Board styling
        self.board_x = 100
        self.board_y = 150
        self.tile_gap = 6

        self.tile_color = (51, 65, 85)
        self.tile_hover_color = (59, 130, 246)
        self.tile_text_color = (255, 255, 255)
        self.empty_color = (15, 23, 42)


    def create_grid(self):
        grid = list(range(1,self.game_size**2))+[0]    #creates a list from 1 to (Games_size^2) -1 so 1 - 8 and adds a 0 to indicate an empty tile 
        return grid 

    def draw_grid(self):
        board_width = self.game_size * self.tile_size

        board_rect = pygame.Rect(
            self.board_x - 8,
            self.board_y - 8,
            board_width + 16,
            board_width + 16
        )

        pygame.draw.rect(
            self.screen,
            (30, 41, 59),
            board_rect,
            border_radius=16
        )
    
    
    # Draw each visible tile and highlight tiles that can legally be moved.
    def draw_tiles(self):
        mouse_pos = pygame.mouse.get_pos()
        empty_row, empty_col = self.get_empty_tile()

        for row in range(self.game_size):
            for col in range(self.game_size):

                i = row * self.game_size + col
                tile_value = self.grid[i]

                x = self.board_x + col * self.tile_size
                y = self.board_y + row * self.tile_size

                tile_rect = pygame.Rect(
                    x + self.tile_gap,
                    y + self.tile_gap,
                    self.tile_size - self.tile_gap * 2,
                    self.tile_size - self.tile_gap * 2
                )

                if tile_value != 0:

                    is_adjacent = (
                        abs(row - empty_row) +
                        abs(col - empty_col) == 1
                    )

                    if tile_rect.collidepoint(mouse_pos) and is_adjacent:
                        color = self.tile_hover_color
                    else:
                        color = self.tile_color

                    pygame.draw.rect(
                        self.screen,
                        color,
                        tile_rect,
                        border_radius=12
                    )

                    font_size = max(18, min(60, int(self.tile_size * 0.55)))
                    font = pygame.font.Font(None, font_size)

                    text = font.render(
                        str(tile_value),
                        True,
                        self.tile_text_color
                    )
                    text_rect = text.get_rect(center=tile_rect.center)
                    self.screen.blit(text, text_rect)

    def get_empty_tile(self):
        empty_tile = self.grid.index(0)     # find the index of 0 which would be 8
        row= empty_tile//self.game_size     # if game_Size  is 3 , you would  8 // 3 =  2 so row = 2 
        col = empty_tile % self.game_size    # same for column
        return row,col  #return these two co ordinates 
    
    # Check whether the empty space can move in the requested direction.
    def check_move(self, direction):
        empty_row ,empty_col = self.get_empty_tile()     # (2,2)
        if direction == "up" and empty_row < self.game_size-1:   #if direction is up and if # empty row = 2 is less than 2 which is false #as empty tile isnt at the top its at the bottom im moving tiles adjacent to it 
            return empty_row+1 , empty_col   #move the tile above empty tile so empty tile would move down 
        elif direction == "down" and empty_row >0 :  # if the empty tile is not at the top 
            return empty_row-1, empty_col  #basically move the tile below and the empty tile above 
        elif direction == "left" and empty_col < self.game_size -1 :  #if the empty tile is not at the right most which would be 2  so less than 2 
            return empty_row, empty_col+1  #basically move the tiles to the left so empty tile moves right 
        elif direction == "right" and empty_col> 0:  #checks if the empty tile is  at the right most  so not at the left most
            return empty_row, empty_col-1  #tiles basically move to right as empty tile moevs to the left 
        
        return None
    
    def Move_Up(self):
        move_pos = self.check_move("up") #check if you can move up so if empty_index was(2,2) it would be the tuple (1,2)
        if move_pos:  #if not none 
            empty_index = self.grid.index(0)  #get index of the empty tile so if (8)
            swap_index = move_pos[0] * self.game_size + move_pos[1]  #so (1,2)  would 1*3+2 = 5 so swap index is 5 
            self.grid[swap_index], self.grid[empty_index] = self.grid[empty_index], self.grid[swap_index] #so swap 5 and 9
        
            self.Moves()
    #similar thing for the other moves 
    def Move_Down(self):
        move_pos = self.check_move("down")
        if move_pos:
            empty_index = self.grid.index(0) 
            swap_index = move_pos[0] * self.game_size+ move_pos[1]
            self.grid[swap_index], self.grid[empty_index] = self.grid[empty_index], self.grid[swap_index]
            self.Moves()
    
    def Move_Left(self):
        move_pos = self.check_move("left")
        if move_pos:
            empty_index = self.grid.index(0)
            swap_index = move_pos[0] * self.game_size + move_pos[1]
            self.grid[swap_index], self.grid[empty_index] = self.grid[empty_index], self.grid[swap_index]
            self.Moves()
    
    def Move_Right(self):#
        move_pos = self.check_move("right")
        if move_pos:
            empty_index = self.grid.index(0)
            swap_index = move_pos[0] * self.game_size + move_pos[1]
            self.grid[swap_index], self.grid[empty_index] = self.grid[empty_index], self.grid[swap_index]
            self.Moves()
    
    #create a mouse handling
    # Convert a mouse click into a valid tile move on the board.
    def mouse_handling(self, mouse_pos):
        mouse_pos_x,mouse_pos_y = mouse_pos  #gets coordiantes of the mouse posiotion and sets its to each of the varible 
        local_x = (mouse_pos_x - self.board_x) % self.tile_size
        local_y = (mouse_pos_y - self.board_y) % self.tile_size

        if (
            local_x < self.tile_gap
            or local_x >= self.tile_size - self.tile_gap
            or local_y < self.tile_gap
            or local_y >= self.tile_size - self.tile_gap
                ):
            return False
        tile_col = (mouse_pos_x - self.board_x) // self.tile_size
        tile_row = (mouse_pos_y - self.board_y) // self.tile_size  #example  if cicked at (350,250) for 3x3
        # 350 - 250 // 100 = 1 and 250-150// = 1 therofore it would be at row 1 col 1
        if (0<= tile_col<self.game_size and 0<= tile_row <self.game_size): #ensure that its within the board 
            #by evaualting time grid cooridante where it must be bigger or equal to 0 and less or equal to maxium row,col
            #eg 3x3   0<tile_col<3
            empty_index = self.grid.index(0)  #index 0 on the grid is the empty tile which it set to index
            #find the positon of the empty index  #eg index 4 on 3x3
            empty_row = empty_index // self.game_size  # 4//3 = 1
            empty_col = empty_index % self.game_size   # 4 % 3 = 1 row 1 col 1

            #calcualtes the distance  eg  empty 2,1 and tile 1,1  so adjacent would be 
            adjacent_row = abs(tile_row - empty_row) #1 abs makes sure there are no negatives 
            adjacent_col = abs(tile_col - empty_col) #0   
            #must be (0,1) or (1,0)   basically must be able to move in a direction     
            if (adjacent_row == 1 and adjacent_col == 0) or (adjacent_col == 1 and adjacent_row == 0 ):
                if tile_row < empty_row:   #if its above so [1] e.g(1,3) so row 1 
                    self.Move_Down()                       #[x]     (2,3) so row 2 so it calls move down 
                elif tile_row > empty_row:  
                    self.Move_Up()                          #logic is similar but to their respecitve positions
                elif tile_col < empty_col :
                    self.Move_Right()
                elif tile_col > empty_col:
                    self.Move_Left()
            
                return True  #returns true showing that tile has moveed
            return False # other wise tile hasnt moved 
                

                








    def shuffle(self):
        for i in range(100): # shuffles the board 100 times
            direction = random.choice(["up","down","left","right"]) #direction is set to a random move every time till for loop ends
            #moves correspoinding to the random choice 
            if direction == "up":
                self.Move_Up()
            if direction == "down":
                self.Move_Down()
            if direction == "left":
                self.Move_Left()
            if direction == "right":
                self.Move_Right()
            
        self.reset_Moves_Made()


    def check_win(self):
        solved = list(range(1, self.game_size ** 2))+[0]
        if self.grid == solved:  #if list grid  == solved list 
            self.best_moves_made() #calcuate call on best move Made  and return true 
            return True 
        return False
    
    def Moves(self): #counts moves made 
        self.moves_made += 1 #increments moves made every time moves procedure is called 
        return self.moves_made #updates moves mades each time and returns it
    
    def reset_Moves_Made(self):
        self.moves_made = 0  #resets moves made by eqauting it to 0
    
    def best_moves_made(self):
        if self.best_moves == 0 or self.best_moves > self.moves_made: # if best move = 0 or  moves made is less than best moves 
            self.best_moves = self.moves_made # equates moves made to best moves made if the condition is met  
    
    def reset_best_moves(self):
        self.best_moves = 0

    def get_current_state(self):
        return self.grid.copy() #returns of current grid 
    

    
    def set_grid(self, new_state):
        self.grid = new_state #set the grid to new stae   

    
