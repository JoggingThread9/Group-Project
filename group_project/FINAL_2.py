from FINAL import fraction

import pygame
import sys
import time

pygame.init()

# dimensions
width = 600
height = 500

# colors
white = (255, 255, 255)
black = (0, 0, 0)

blue = (0, 0, 255)
light_blue = (50, 50, 255)

# font
font = pygame.font.Font("freesansbold.ttf", 36)

# variable for tick method
clock = pygame.time.Clock()

# dimensions for the box
box_size = pygame.Rect(250, 320, 75, 50)

# place holders
active = False

user_input = ""

start_fraction = 0

# window
window = pygame.display.set_mode((width, height))
window.fill(white)
pygame.display.set_caption("Egyptian Fraction Maker")

used = []

# GUI
while True:
    # uses the tick method so it runs at 60 fps
    clock.tick(60)
    for event in pygame.event.get():
        # if the users tries to quit the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # quits the program

        if event.type == pygame.MOUSEBUTTONDOWN:
            # if box is pressed
            if box_size.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    # if the users tries to delete what they entered
                    user_input = user_input[:-1]
                    # if the user presses enter
                elif event.key == pygame.K_RETURN:
                    active = False

                    start = time.time()
                    # clears the user_input and assigns it to start fraction
                    start_fraction = user_input
                    user_input = ""

                    # finds the numerator and denominator based upon where the slash is
                    start_fraction = str(start_fraction)
                    slash = start_fraction.index("/")
                    numerator = start_fraction[:slash]
                    denominator = start_fraction[slash + 1:]

                    numerator = int(numerator)
                    denominator = int(denominator)

                    # calls the fraction class and gives it values
                    x = fraction(numerator, denominator)
                    # calls the check method in fraction
                    x.check()

                    # assigns used to fraction.used then clears fraction.used
                    used = fraction.used
                    fraction.used = []

                    end = time.time()
                    print(end - start)
                else:
                    user_input += event.unicode

        # colors the window
        window.fill(blue)

        # changes color of the box if it was pressed
        if active:
            color = white
        else:
            color = light_blue

        # writes the answer of the screen
        answer = font.render(str(start_fraction) + " = " + str(used), True, white, blue)
        answer_rect = answer.get_rect()
        answer_rect.center = (width/2, height/2)
        window.blit(answer, answer_rect)

        # draws a rectangle
        pygame.draw.rect(window, color, box_size)

        # makes the user input box
        input_box = font.render(user_input, True, black)

        # puts the box on the screen
        window.blit(input_box, (box_size.x + 5, box_size.y + 5))

        # updates the box size
        box_size.w = max(100, input_box.get_width() + 10)

        # updates the display
        pygame.display.update()
        pygame.display.flip()
