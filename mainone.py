import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Ball Catcher")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BLUE = (135, 206, 250)  
RED = (255, 50, 50)

# Circle setup
circle_radius = 25 
circle_x = random.randint(circle_radius, WIDTH - circle_radius)  #for random horizontal position
circle_y = 0                                                     # to start from top
circle_speed = 3
circle_speed_increment = 0.5

# Catcher/basket setup
catcher_width = 150 
catcher_height = 25
catcher_x = WIDTH // 2 - catcher_width // 2   #makes the basket start perfectly centered horizontally
catcher_y = HEIGHT - 50                       #fixes the basket near the bottom of the screen
catcher_speed = 7                             #speed of moving left or right

score = 0

# Function to draw a circle
def draw_circle(xc, yc, r, color):
    pygame.draw.circle(screen, color, (xc, yc), r)
    

# Function to draw basket/catcher
def draw_catcher():
    pygame.draw.rect(screen, BLACK, (catcher_x, catcher_y, catcher_width, catcher_height))
   

# Game Over screen
def game_over():
    font = pygame.font.SysFont(None, 72)
    text = font.render("GAME OVER!", True, RED)   #creates an image of the text that can be drawn on the screen
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))#text appear perfectly in the center of the screen
    pygame.display.flip()  #Updates the screen to show everything you drew
    pygame.time.wait(3000)  #so the player can see the GAME OVER text before the window closes
    pygame.quit()
    sys.exit()

# Main game loop
def main():
    global circle_x, circle_y, catcher_x, score, circle_speed
    clock = pygame.time.Clock()  #controls how fast your game runs

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Catcher movement
        keys = pygame.key.get_pressed()  #checks which keys are currently pressed
        if keys[pygame.K_LEFT] and catcher_x > 0:
            catcher_x -= catcher_speed
        if keys[pygame.K_RIGHT] and catcher_x < WIDTH - catcher_width:
            catcher_x += catcher_speed

        # Update circle position
        circle_y += circle_speed

        # Catch detection
        if (catcher_y <= circle_y + circle_radius <= catcher_y + catcher_height) and \
           (catcher_x <= circle_x <= catcher_x + catcher_width):
            score += 1
            circle_y = 0
            circle_x = random.randint(circle_radius, WIDTH - circle_radius)
            circle_speed += circle_speed_increment  # speed increases after each catch

        # Missed catch
        if circle_y - circle_radius > HEIGHT:
            game_over()

        # Drawing everything
        screen.fill(BLUE) 
        draw_circle(circle_x, circle_y, circle_radius, WHITE)
        draw_catcher()

        # Draw score
        font = pygame.font.SysFont(None, 36)
        img = font.render(f'Score: {score}', True, WHITE)
        screen.blit(img, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
