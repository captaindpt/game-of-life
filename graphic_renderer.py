import pygame
import numpy as np
from game_engine import GameOfLife  # Assuming this is the class we defined earlier

# Pygame Initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
FPS = 10  # Frames per second, can be adjusted to control speed

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Create a GameOfLife instance
game = GameOfLife(width=WIDTH // CELL_SIZE, height=HEIGHT // CELL_SIZE)

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            if game.grid[y // CELL_SIZE][x // CELL_SIZE]:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

# Button and Slider Attributes
button_font = pygame.font.Font(None, 24)  # Adjust as needed
button_color = WHITE
button_hover_color = (200, 200, 200)
buttons = [
    {"label": "Randomize", "rect": pygame.Rect(0, HEIGHT - 40, 100, 30), "action": "randomize"},
    {"label": "Play/Pause", "rect": pygame.Rect(110, HEIGHT - 40, 100, 30), "action": "toggle"},
    {"label": "Reset", "rect": pygame.Rect(220, HEIGHT - 40, 100, 30), "action": "reset"},
]
slider = {"rect": pygame.Rect(330, HEIGHT - 40, 100, 30), "value": FPS, "min": 1, "max": 60, "action": "speed"}

def draw_button(button, screen):
    pygame.draw.rect(screen, button_color if not button["hover"] else button_hover_color, button["rect"])
    text_surf = button_font.render(button["label"], True, BLACK)
    text_rect = text_surf.get_rect(center=button["rect"].center)
    screen.blit(text_surf, text_rect)

def draw_slider(slider, screen):
    pygame.draw.rect(screen, WHITE, slider["rect"], 2)
    indicator_pos = (slider["rect"].x + (slider["value"] - slider["min"]) / (slider["max"] - slider["min"]) * slider["rect"].width, slider["rect"].y + slider["rect"].height / 2)
    pygame.draw.circle(screen, WHITE, indicator_pos, 10)
def handle_button_click(mouse_pos):
    global playing, FPS  # Ensure these are defined as global if you're modifying them
    for button in buttons:
        if button["rect"].collidepoint(mouse_pos):
            if button["action"] == "randomize":
                density = np.random.randint(1, 101)  # Example density value, adjust as needed
                # Add your randomize grid logic here based on density
            elif button["action"] == "toggle":
                playing = not playing
            elif button["action"] == "reset":
                game.reset()
            break  # Only handle the first button clicked

def handle_slider_click(mouse_pos):
    if slider["rect"].collidepoint(mouse_pos):
        # Adjust FPS based on mouse position within the slider rect
        slider_value = (mouse_pos[0] - slider["rect"].x) / slider["rect"].width
        FPS = int(slider_value * (slider["max"] - slider["min"]) + slider["min"])
        slider["value"] = FPS

def main():
    global FPS
    clock = pygame.time.Clock()
    running = True
    playing = False

    while running:
        
        
        screen.fill(BLACK)
        
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                game.grid[y // CELL_SIZE][x // CELL_SIZE] ^= True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                elif event.key == pygame.K_r:
                    game.reset()
                elif event.key == pygame.K_UP:
                    FPS += 5  # Increase speed
                elif event.key == pygame.K_DOWN:
                    FPS = max(5, FPS - 5)  # Decrease speed, with a minimum limit

        if playing:
            game.update()

        draw_grid()
        mouse_pos = pygame.mouse.get_pos()

        # Update hover state for buttons
        for button in buttons:
            button["hover"] = button["rect"].collidepoint(mouse_pos)

        # Event handling for clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_button_click(mouse_pos)
                handle_slider_click(mouse_pos)

        # Drawing buttons and slider
        for button in buttons:
            draw_button(button, screen)
        draw_slider(slider, screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
