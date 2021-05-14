import pygame
import pygame_menu
import random
from random import randint




res_x = 800
res_y = 600
rock_width = 50
rock_height = 50
rock_x = res_x - 100
rock_y = randint(1, 600)
rock_speed = 0.3
rock_1 = pygame.image.load('rock_1.png')

display = pygame.display.set_mode((res_x, res_y))



rock_width2 = 60
rock_height2 = 60
rock_x2 = res_x - 100
rock_y2 = randint(100, 675)
rock_speed2 = 0.3
rock_2 = pygame.image.load('rock_2.png')

rock_width3 = 60
rock_height3 = 60
rock_x3 = res_x - 100
rock_y3 = randint(250, 650)
rock_speed3 = 0.3
rock_3 = pygame.image.load('rock_2.png')
# bg = pygame.image.load('Menu.jpg')


usr_x = res_x // 6
usr_y = 300
usr_widht = 100
usr_height = 66
usr_speed = 0.5
usr_sprite = pygame.image.load('spaceship.png')


score = 0
adove_rock =False

rect1 = pygame.Rect((usr_x, usr_y,usr_widht,usr_height))
rect2 = pygame.Rect((rock_x, rock_y, rock_width, rock_height))

def collide(rect1: pygame.Rect, rect2: pygame.Rect):
    a = False
    if (rect1[0] <= rect2[0] <= rect1[0] + rect1[2] or
        rect1[0] <= rect2[0] + rect2[2] <= rect1[0] + rect1[2] or
        (rect2[0] <= rect1[0] and rect2[0] + rect2[2] >= rect1[0] + rect1[2])) and \
            (rect1[1] <= rect2[1] <= rect1[1] + rect1[3] or
             rect1[1] <= rect2[1] + rect2[3] <= rect1[1] + rect1[3] or
             (rect2[1] <= rect1[1] and rect2[1] + rect2[3] >= rect1[1] + rect1[3])):
        a = True
    return a



def game():

    def draw_rock():
        global rock_x, rock_y, rock_width, rock_height, rock_x2, rock_y2, rock_width2, rock_height3, rock_x3, rock_y3, rock_width3, rock_height3

        if rock_x >= -rock_width:
            display.blit(rock_1,(rock_x,rock_y))
            rock_x -= rock_speed
        elif  rock_x2 >= -rock_width2:
            display.blit(rock_2,(rock_x2,rock_y2))
            rock_x2 -= rock_speed2
        elif  rock_x3 >= -rock_width3:
            display.blit(rock_3,(rock_x3,rock_y3))
            rock_x3 -= rock_speed3
        else:
            rock_x = res_x-50
            rock_x2 = res_x-50
            rock_x3 = res_x - 50
            rock_y = random.randint(50, res_y - 50)
            rock_y2 = random.randint(50, res_y - 50)
            rock_y3 = random.randint(50, res_y - 50)
    usr_x = res_x // 6
    usr_y = 300
    usr_widht = 100
    usr_height = 66
    usr_speed = 0.5
    Score = 0
    bg = pygame.image.load("Background.jpg")

    collide(rect1, rect2)





    pygame.display.set_caption("FLL")


    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        display.blit(bg, (0, 0))





        keys = pygame.key.get_pressed()





        if keys[pygame.K_DOWN] and usr_y < res_y - usr_height - 10:
            usr_y += usr_speed
        if keys[pygame.K_ESCAPE]:
            pause()
        if keys[pygame.K_UP] and usr_y > 10:
            usr_y -= usr_speed
        if keys[pygame.K_RIGHT] and usr_x < res_x - usr_widht - 10:
            usr_x += usr_speed
        if keys[pygame.K_LEFT] and usr_x > 10:
            usr_x -= usr_speed
        if keys[pygame.K_BACKSPACE]:
            run=False

        draw_rock()
        display.blit(usr_sprite,(usr_x,usr_y))
        # pygame.draw.rect(display, (0 ,0 ,255), (usr_x, usr_y, usr_widht, usr_height))

        # print_text('Score: ' + str(score), 10, 10)
        pygame.display.update()
    return game_over()
    # clock.tick(1000)

pygame.init()
surface = pygame.display.set_mode((res_x, res_y))


def Scores():
    global score, adove_rock

def game_over():
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #print_text('GAME OVER', 160, 300)
        keys = pygame.key.get_pressed()
        if keys(pygame.K_RETURN):
            return True
        if keys[pygame.K_ESCAPE]:
            return False
        pygame.display.update()


def set_difficulty(value, difficulty):
    # Do the job here !
    pass
# def print_text(message, x, y, font_color = (0, 0, 0), font_type = 'Pig.ttf', font_size = 70 ):
#     font_type = pygame.font.Font(font_type, font_size)
#     text = font_type.render(message, True, font_color)
#     display.blit(text, (x, y))


def start_the_game():
    # Do the job here !
    while game():
        pass


def check_collision(barriers):
    for barrier in barriers:
        if usr_y + usr_height >= barrier.y:
            if barrier.x <= usr_x <= barrier.x + barrier.width:
                return True;
            elif barrier.x <= usr_x + usr_widht <= barrier.x + barrier.width:
                return True
    return False
#font_color = (0, 0, 0)
WHITE = (255, 255, 255)
# font_type1 = 'Sobaka.png'
DISPLAYSURF = pygame.display.set_mode((res_x, res_y))
DISPLAYSURF.fill(WHITE)



def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('PAUSED. Press 1 to contine', 150, 250)



        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            paused = False
        pygame.display.update()

# menu_bg = pygame.image.load('Lox.jpg')
# display.blit(bg, (0, 0))


show = True
menu = pygame_menu.Menu(300, 500, 'FLL',
                            theme=pygame_menu.themes.THEME_BLUE)
menu.add.text_input('Name :', default='None')
menu.add.selector('Difficulty :', [('Easy', 1), ('Hard', 1)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
pygame.display.update()

pygame.quit()

quit()