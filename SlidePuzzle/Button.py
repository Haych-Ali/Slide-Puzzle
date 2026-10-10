#Button file
import pygame

# Reusable button component for the menu and gameplay controls.
# It draws itself and changes color when the mouse hovers over it.
class Button():
    def __init__(self,x_pos, y_pos, text_input, font=None, base_color=(59,130,250), hovering_color=(90,165,250), image=None, width  = 200, height = 50):
        
        self.x_pos = x_pos #horizontal positon 
        self.y_pos = y_pos  #vetical postion
        self.text_input = text_input  # textt for dipslay
        self.font = font if font else pygame.font.Font(None,30)   #specifc font if not use the defualt pygame font 
        self.base_color = base_color      #inital colour
        self.hovering_color=hovering_color  #hovering state colour   
        self.width= width   # width of the button in pixel
        self.height= height  # height of the button in pixels 


        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
        self.current_color = self.base_color
        

        
    def draw(self, screen):
        self.color(pygame.mouse.get_pos())
    # Draw the button background
        pygame.draw.rect(
            screen,
            self.current_color,
            self.rect,
            border_radius=12
            )

    # Draw the button text
        if self.text_input:
            text_surface = self.font.render(
            self.text_input,
            True,
            (255, 255, 255)
            )

            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)
    
    
        
        
        
    def check_for_input(self,position):  
        if self.rect.left<= position[0] <=self.rect.right and self.rect.top <= position[1] <= self.rect.bottom:  #if mouse position is within the bonds of the button 
            return True #return true 
        return False #return false 



    def color(self, position, normal_color=None, hovering_color=None):
        if self.check_for_input(position):
            self.current_color = self.hovering_color
        else:
            self.current_color = self.base_color