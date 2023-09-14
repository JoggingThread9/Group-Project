import pygame
pygame.init()

width = 600
height = 500

white = (255,255,255)
blue = (0,0,255)
light_blue = (50,50,255)
black = (0,0,0)

start_fraction = 0
egyptian_fraction = "?"

font = pygame.font.Font("freesansbold.ttf", 36)

user_input = ""

box_size = pygame.Rect(250,320,75,50)

off_color = light_blue

on_color = white
color = off_color

active = False

fps = 60

clock = pygame.time.Clock()

#create window
screen = pygame.display.set_mode((width,height))
screen.fill(white)
pygame.display.set_caption("Egyptian Fractions")

#main loop
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if box_size.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                if event.key == pygame.K_RETURN:
                    active = False
                    start_fraction = user_input
                    user_input = ""
                else:
                    user_input += event.unicode
        screen.fill(blue)
        if active:
            color = on_color
        else:
            color = off_color
        inter = font.render(str(start_fraction) + " = " + egyptian_fraction, True, white, blue)
        inter_rect = inter.get_rect()
        inter_rect.center = (width/2, height/2)
        screen.blit(inter, inter_rect)
        pygame.draw.rect(screen, color, box_size)
        input_box = font.render(user_input, True, black)
        screen.blit(input_box, (box_size.x+5, box_size.y+5))
        box_size.w = max(100, input_box.get_width() + 10)
        pygame.display.update()
        pygame.display.flip()

