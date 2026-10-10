#timer file 
# Handles start, stop, and display functions for the gameplay timer and best score tracking.
import pygame

class Timer():
    def __init__(self):
        self._start_timestamp = None
        self.running = False
        self.best_time = None
        self.final_time = 0
    
    
    # Begin timing when the first valid move is made.
    def start_time(self):
        if not self.running:
            self._start_timestamp = pygame.time.get_ticks()
            self.running = True
    
    # Stop the timer and update the best result if needed.
    def stop_time(self):
        if self.running:
            elapsed_time = self.get_time_taken()
            self.final_time = elapsed_time
            if self.best_time is None or elapsed_time<self.best_time:
                self.best_time = elapsed_time
            self.running = False

             
             
    
    # Reset the current timer run and keep the final time at zero.
    def reset(self):
        self._start_timestamp = pygame.time.get_ticks()
        self.running = False
        self.final_time= 0
          
    

    # Return the elapsed time while the timer is running, or the last completed time.
    def get_time_taken(self):
            if self.running and self._start_timestamp != None:
                return (pygame.time.get_ticks() - self._start_timestamp)
            return self.final_time
        
    # Format the current elapsed time as mm:ss:ms for display on screen.
    def time(self):
            total_time = self.get_time_taken()
            minutes = total_time // 60000
            seconds = (total_time % 60000)//1000
            milliseconds = total_time %1000

            return f"{minutes:02}:{seconds:02}:{milliseconds:03}"
        
    # Format the best completed time for display in the interface.
    def best_time_display(self):
        if self.best_time is None or self.best_time == 0:
            return "00:00:000"
        total_time = self.best_time 
        minutes = total_time // 60000
        seconds =  (total_time % (60*1000)) // 1000
        millseconds = total_time % 1000
        time = f"{minutes:02}:{seconds:02}:{millseconds:03}"
        return time
    
    def reset_best_time(self):
         self.best_time = 0
         self.final_time = 0



