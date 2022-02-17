# Breakout game using pygame
import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
game_screen = pygame.display.set_mode(SCREEN_SIZE)

x = 150
y = 550

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
        limit_top = pygame.draw.rect(game_screen,
                            LIMIT_COLOR, 
                            pygame.Rect(
                            0, #Position X
                            40, #Position Y
                            SCREEN_WIDTH,
                            LIMIT_HEIGHT*3)
                        )

font = pygame.font.Font('freesansbold.ttf', 24)
life_1 = '1'
score_1 = '000'
life_2 = '1'
score_2 = '000' 

color_text = 'white'

text_life_1 = font.render(life_1, True, color_text)
pos_text_life_1 = text_life_1.get_rect()
pos_text_life_1.center = (SCREEN_WIDTH*0.1, 70)

text_life_2 = font.render(life_2, True, color_text)
pos_text_life_2 = text_life_2.get_rect()
pos_text_life_2.center = (SCREEN_WIDTH*0.55, 70)

text_score_1 = font.render(score_1, True, color_text)
pos_text_score_1 = text_score_1.get_rect()
pos_text_score_1.center = (SCREEN_WIDTH*0.2, 100)

text_score_2 = font.render(score_2, True, color_text)
pos_text_score_2 = text_score_2.get_rect()
pos_text_score_2.center = (SCREEN_WIDTH*0.65, 100)



#Game_loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 20
            if event.key == pygame.K_RIGHT:
                x = x + 20
                
    if x <= 0:
        x = 0
    if x >= 300:
        x = 300

    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, (0, 0, 100), (x, y, 100, 20))

    game_screen.blit(text_life_1, pos_text_life_1)
    game_screen.blit(text_life_2, pos_text_life_2)
    game_screen.blit(text_score_1, pos_text_score_1)
    game_screen.blit(text_score_2, pos_text_score_2)        

    screen_limit()
    blocks()
    pygame.display.update()        
