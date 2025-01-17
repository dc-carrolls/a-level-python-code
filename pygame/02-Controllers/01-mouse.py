import pygame

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
colours = (WHITE, BLUE, YELLOW, RED)
colour_choice = 0
frame_count = 0
# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (1200,800)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My First Flipbook")

game_over = False

### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
            
    # -- Game logic goes after this comment
    pos = pygame.mouse.get_pos()
    if True in pygame.mouse.get_pressed() and frame_count > 30:
        colour_choice = (colour_choice + 1) % 4
        frame_count = 0

    frame_count = (frame_count + 1)% 3000
    mouse_x = pos[0]
    mouse_y = pos[1]
    
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here

    # Make the mouse pointer appear in the middle of the square...
    pygame.draw.rect(screen, colours[colour_choice], (mouse_x, mouse_y, 25, 25))


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
