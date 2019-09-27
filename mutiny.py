import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, math, pygame, random, time
canvas_x = 1400
canvas_y = 800
screen = pygame.display.set_mode((canvas_x, canvas_y))
screen.fill((0, 0, 0))

pygame.init()
pygame.display.set_caption('Mutiny')
pygame.mouse.set_visible(0)
game_start = 0

#Test Box (TB)
TB_x = canvas_x/2
TB_y = canvas_y/2
TB_size = 60
TB_yV = 0

#position
P1_x = canvas_x/4
P1_y = canvas_y/4
P2_x = 3*canvas_x/4
P2_y = 3*canvas_y/4

#velocity
P1_xV = 0
P1_yV = 0
P2_xV = 0
P2_yV = 0

#acceleration
P1_xA = 0
P1_yA = 0
P2_xA = 0
P2_yA = 0

mouse_pos = pygame.mouse.get_pos()

def hitbox(x_pos, y_pos, size):
    if mouse_pos[0] < x_pos + size and mouse_pos[0] > x_pos and mouse_pos[1] > y_pos and mouse_pos[1] < y_pos + size:
        return True

def TB_hitbox():
    if mouse_pos[0] < TB_x + TB_size and mouse_pos[0] > TB_x and mouse_pos[1] > TB_y and mouse_pos[1] < TB_y + TB_size:
        return True

def colour_dectect(x_pos, y_pos, size, colour):
    if str(surface.get_at((x_pos, y_pos + size))[:3]) == colour or str(surface.get_at((x_pos + size, y_pos + size))[:3]) == colour:
        return True

def TB_colour_dectect():
    if str(surface.get_at((TB_x, TB_y + TB_size))[:3]) == "(0, 0, 0)" or str(surface.get_at((TB_x + TB_size, TB_y + TB_size))[:3]) == "(0, 0, 0)":
        return True

#functions
def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def message_display(text, position, size):
    smallText = pygame.font.Font('C:/windows/fonts/times.ttf',size)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = position
    screen.blit(TextSurf, TextRect)

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def announce_player(player_number, time):
        print("player " + player_number + "s turn")
        time.sleep(time)
        clear()  ##do the thing and say whose turn it is

def loop_legality():
    pygame.display.flip()
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # makes the loop mortal
            start = 0
            sys.exit()

def movement():
    if paused == 0:
        P1_x += P1_xV
        P1_y += P1_yV
        P2_x += P2_xV
        P2_y += P2_yV
        P1_xV += P1_xA
        P1_yV += P1_yA
        P2_xV += P2_xA
        P2_yV += P2_yA
        P1_xA = P1_xA*0.85
        P1_yA = P1_yA*0.85
        P2_xA = P2_xA*0.85
        P2_yA = P2_yA*0.85

start = 1
while start == 1: #bigger loop that will contain everything, an embedded while loop will be the game
    loop_legality()
    mouse_pos = pygame.mouse.get_pos()
    message_display("made by Jonny B. and Jake N.",(125, 750),15)
    mouse1 = pygame.mouse.get_pressed()[0]
    mouse2 = pygame.mouse.get_pressed()[2]
    mouse3 = pygame.mouse.get_pressed()[1]

    screen.blit(pygame.image.load(r'mutiny assets\play_button.png'), (canvas_x/2 - 125, canvas_y/2 - 75))
    if hitbox(canvas_x/2, canvas_y/2, 75):
        game_start = 1
    screen.blit(pygame.image.load(r'mutiny assets\cursor.png'), (mouse_pos[0], mouse_pos[1]))

    TB_grounded = 0
    TB_xV = 0
    TB_yV = 0

    while game_start == 1: #game loop
        loop_legality()
        mouse_pos = pygame.mouse.get_pos()
        message_display("made by Jonny B. and Jake N.",(125, 750),15)
        mouse1 = pygame.mouse.get_pressed()[0]
        mouse2 = pygame.mouse.get_pressed()[2]
        mouse3 = pygame.mouse.get_pressed()[1]

        pygame.draw.rect(screen, (0, 150, 0), (TB_x, TB_y, TB_size, TB_size))
        if TB_colour_dectect():
            TB_grounded = 1
            if TB_hitbox() and mouse1 == 1:
                while mouse1 == 1:
                    loop_legality()
                    TB_xV = mouse_pos[0] - TB_x
                    TB_yV = mouse_pos[1] - TB_y
        elif not TB_colour_dectect():
            TB_grounded = 0
            TB_x += TB_xV
            TB_y -= TB_yV



        screen.blit(pygame.image.load(r'mutiny assets\cursor.png'), (mouse_pos[0], mouse_pos[1]))
