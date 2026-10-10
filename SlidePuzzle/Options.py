#Option file 
import pygame
import sys

from Button import Button
from theme import BACKGROUND

# Shared font helper used in the settings screen.
def get_Font(size=24 ,bold=False ,italic=False, font_name=None):
    font_name = font_name or pygame.font.match_font("arial")
    font = pygame.font.SysFont(font_name, size)
    font.set_bold(bold)
    font.set_italic(italic)
    return font

# Display the settings screen and allow the user to return to the previous menu.
def options():
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    while True:
        # Fill the screen with the global background colour.
        screen.fill(BACKGROUND)

        # Settings heading
        title_font = get_Font(40, bold=True)
        title = title_font.render("SETTINGS", True, (255, 255, 255))
        title_rect = title.get_rect(center=(400, 120))
        screen.blit(title, title_rect)

        # Description
        text_font = get_Font(22)
        description = text_font.render(
                "Game settings and preferences",
                True,
                (148, 163, 184)
            )
        description_rect = description.get_rect(center=(400, 180))
        screen.blit(description, description_rect)

            # Back button
        back_button = Button(
                300, 400, "Back",
                font=get_Font(25),
                base_color=(59, 130, 246),
                hovering_color=(96, 165, 250)
            )
        back_button.draw(screen)

            # Event handling
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if back_button.check_for_input(event.pos):
                            return

        pygame.display.update()
        clock.tick(60)






