# Breakout game using pygame
import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
pygame.init()
game_screen = pygame.display.set_mode(SCREEN_SIZE)

paddle_color = (255,0,0) #Red

paddle = pygame.draw.rect(game_screen,
                            paddle_color, 
                            pygame.Rect(
                            (SCREEN_WIDTH/2)-PADDLE_WIDTH/2, #Position X
                            SCREEN_HEIGHT-50, #Position Y
                            PADDLE_WIDTH,
                            PADDLE_HEIGHT)
                        )
def blocks():
    width = 26
    height = 10
    gap = 2.5
    margin_top = 120
    margin_left = 2
    block_color = 'red'   
    for i in range(14):
        for j in range(8):
            if j == 0 or j == 1:
                block_color = 'red'   
            if j == 2 or j == 3:
                block_color = 'orange'
            if j == 4 or j == 5:
                block_color = 'green'
            if j > 5:
                block_color = 'yellow'


                
            x = margin_left+(width + gap) * i
            y = margin_top+(height + gap*2) * j
            pygame.draw.rect(game_screen, block_color,
            pygame.Rect(x,y,width,height))
            
def screen_limit():
        LIMIT_HEIGHT = 5
        LIMIT_COLOR = 'white'
        limit_rigth = pygame.draw.rect(game_screen,
                            LIMIT_COLOR, 
                            pygame.Rect(
                            SCREEN_WIDTH-LIMIT_HEIGHT, #Position X
                            0, #Position Y
                            LIMIT_HEIGHT,
                            SCREEN_HEIGHT)
                        )
        limit_left = pygame.draw.rect(game_screen,
                            LIMIT_COLOR, 
                            pygame.Rect(
                            0, #Position X
                            0, #Position Y
                            LIMIT_HEIGHT,
                            SCREEN_HEIGHT)
                        )

score_font = pygame.font.Font('assets/PressStart2P-Regular.ttf', 44)
score_text = score_font.render('00 x 00', True, 'white', 'black')
score_text_rect = score_text.get_rect()

screen_limit()
blocks()


#Game_loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



    pygame.display.update()        