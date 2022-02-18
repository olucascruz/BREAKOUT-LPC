# Breakout game using pygame
import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

RED = '#A31E0A'
ORANGE = '#C2850A'
GREEN = '#0A8533'
YELLOW = '#C2C229'
WHITE = '#CCCCCC'
BLUE = '#0A85C2'
pygame.init()
game_screen = pygame.display.set_mode(SCREEN_SIZE)

x = 180
y = 550

ball_x = 200
ball_y = 300

block_width = 26
block_height = 10

class block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def break_block(self):
        global velocity, block_height, block_width
        if self.rect.center[1]+block_height >= ball_y and\
                    (self.rect.center[0]<=ball_x and
                    self.rect.center[0]+block_width>=ball_x):
                        self.kill()

blocks_group = pygame.sprite.Group()
def create_blocks():
    global blocos_grupo, block_height, block_width
    
    gap = 2.5
    margin_top = 125
    margin_left = 15
    block_color = RED  
    for i in range(14):
        for j in range(8):
            if j == 0 or j == 1:
                block_color = RED   
            if j == 2 or j == 3:
                block_color = ORANGE
            if j == 4 or j == 5:
                block_color = GREEN
            if j > 5:
                block_color = YELLOW


                
            position_x = margin_left+(block_width + gap) * i
            position_y = margin_top+(block_height + gap*2) * j

            a_block = block(block_color,block_width,block_height,position_x,position_y)  
            blocks_group.add(a_block)
    return blocks_group
create_blocks()

def screen_limit():
    LIMIT_HEIGHT = 5
    LIMIT_COLOR = WHITE
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
    
    colors_details = (RED, ORANGE, GREEN, YELLOW, BLUE)
    pos_details = (117, 147, 177, 207, 545)

    for i in range(5):
       left_details = pygame.draw.rect(game_screen,
                        colors_details[i], 
                        pygame.Rect(
                        0, #Position X
                        pos_details[i], #Position Y
                        LIMIT_HEIGHT,
                        30)
                    )
    for i in range(5):
        right_details = pygame.draw.rect(game_screen,
                        colors_details[i], 
                        pygame.Rect(
                        SCREEN_WIDTH-LIMIT_HEIGHT, #Position X
                        pos_details[i], #Position Y
                        LIMIT_HEIGHT,
                        30)
                    )
    


font = pygame.font.Font('assets/bauhaus-93.ttf', 42)
life_1 = '1'
score_1 = '000'
life_2 = '1'
score_2 = '000' 

color_text = WHITE

text_life_1 = font.render(life_1, True, color_text)
pos_text_life_1 = text_life_1.get_rect()
pos_text_life_1.center = (20, 70)

text_life_2 = font.render(life_2, True, color_text)
pos_text_life_2 = text_life_2.get_rect()
pos_text_life_2.center = (220, 70)

text_score_1 = font.render(score_1, True, color_text)
pos_text_score_1 = text_score_1.get_rect()
pos_text_score_1.center = (65, 100)

text_score_2 = font.render(score_2, True, color_text)
pos_text_score_2 = text_score_2.get_rect()
pos_text_score_2.center = (265, 100)

clock = pygame.time.Clock()

#Game_loop 
while True:
    clock.tick(100)
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
    if x >= 340:
        x = 340

    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, BLUE, (x, y, 60, 20))
    
    pygame.draw.circle(game_screen, WHITE, (ball_x, ball_y), 5)
    ball_y = ball_y + 1
    ball_x = ball_x + 1

    game_screen.blit(text_life_1, pos_text_life_1)
    game_screen.blit(text_life_2, pos_text_life_2)
    game_screen.blit(text_score_1, pos_text_score_1)
    game_screen.blit(text_score_2, pos_text_score_2)        

    screen_limit()
    blocks_group.draw(game_screen)
    blocks_group.update()
    pygame.display.update()        
