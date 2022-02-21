# Breakout game using pygame
import pygame
import math

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

RED = '#A31E0A'
ORANGE = '#C2850A'
GREEN = '#0A8533'
YELLOW = '#C2C229'
WHITE = '#CCCCCC'
BLUE = '#0A85C2'

x = 180
y = 550

block_width = 26
block_height = 10

paddle_width = 40
paddle_height = 20

run = True

pygame.init()
pygame.mixer.init()

impact_with_block = pygame.mixer.Sound('songs/impact_with_block.wav')
impact_with_limit = pygame.mixer.Sound('songs/impact_with_limit.wav')
impact_with_paddle = pygame.mixer.Sound('songs/impact_with_paddle.wav')

game_screen = pygame.display.set_mode(SCREEN_SIZE)



class Ball():
    def __init__(self):
        self.x = 200
        self.y = 300
        self.dx = 1
        self.dy = -5
        self.width = 10
        self.height = 8

    def move(self):
        # movement ball
        global life, text_life
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        # collision with left limit
        if self.x < 0 + self.width/2.0:
            self.x = 0 + self.width/2.0
            self.dx *= -1
            impact_with_limit.play()
        
        # collision with rigth limit 
        elif self.x > 395 - self.width/2.0:
            self.x = 395 - self.width/2.0
            self.dx *= -1
            impact_with_limit.play()

        # collision with top limit
        if self.y < 50 + self.height / 2.0:
            self.y = 50 + self.height / 2.0
            self.dy *= -1
            impact_with_limit.play()

        elif self.y > 600 - self.height / 2.0:
            self.y = 600 - self.height / 2.0
            self.x = SCREEN_WIDTH/2.0
            self.y = 600/2.0
            update_life()


    def render(self, color=WHITE):
        pygame.draw.rect(game_screen, color, (self.x, self.y, 12, 10))
        
    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)


class block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height
        self.color = color
    

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

            position_x = margin_left + (block_width + gap) * i
            position_y = margin_top + (block_height + gap * 2) * j

            a_block = block(block_color, block_width, block_height, position_x, position_y)
            blocks_group.add(a_block)
    return blocks_group

create_blocks()


def screen_limit():
    LIMIT_HEIGHT = 5
    LIMIT_COLOR = WHITE
    limit_rigth = pygame.draw.rect(game_screen,
                                   LIMIT_COLOR,
                                   pygame.Rect(
                                       SCREEN_WIDTH - LIMIT_HEIGHT,  # Position X
                                       0,  # Position Y
                                       LIMIT_HEIGHT,
                                       SCREEN_HEIGHT)
                                   )
    limit_left = pygame.draw.rect(game_screen,
                                  LIMIT_COLOR,
                                  pygame.Rect(
                                      0,  # Position X
                                      0,  # Position Y
                                      LIMIT_HEIGHT,
                                      SCREEN_HEIGHT)
                                  )
    limit_top = pygame.draw.rect(game_screen,
                                 LIMIT_COLOR,
                                 pygame.Rect(
                                     0,  # Position X
                                     40,  # Position Y
                                     SCREEN_WIDTH,
                                     LIMIT_HEIGHT * 3)
                                 )

    colors_details = (RED, ORANGE, GREEN, YELLOW, BLUE)
    pos_details = (117, 147, 177, 207, 545)

    for i in range(len(pos_details)):
        if ball.y > pos_details[i] and ball.y<pos_details[i] +30:
            ball.render(colors_details[i])

    for i in range(5):
        left_details = pygame.draw.rect(game_screen,
                                        colors_details[i],
                                        pygame.Rect(
                                            0,  # Position X
                                            pos_details[i],  # Position Y
                                            LIMIT_HEIGHT,
                                            30)
                                        )
    for i in range(5):
        right_details = pygame.draw.rect(game_screen,
                                         colors_details[i],
                                         pygame.Rect(
                                             SCREEN_WIDTH - LIMIT_HEIGHT,  # Position X
                                             pos_details[i],  # Position Y
                                             LIMIT_HEIGHT,
                                             30)
                                         )


font = pygame.font.Font('font/forward-regular.ttf', 24)
life_1 = '1'

score_1_hundreds = 0
score_1_dozens = 0
score_1_unit = 0

life = 1
score_2 = '000'
color_text = WHITE

def update_score(block_color):
    global score_1_unit, score_1_dozens, score_1_hundreds
    if block_color == YELLOW:
        score_1_unit += 1
    if block_color == GREEN:
        score_1_unit += 3
    if block_color == ORANGE:
        score_1_unit += 5
    if block_color == RED:
        score_1_unit += 7
        
    if score_1_unit > 9:
        score_1_unit = 0
        score_1_dozens += 1

    if score_1_dozens > 9:
        score_1_dozens = 0
        score_1_hundreds += 1

def endgame():
    global paddle_width, run, score_1_unit, score_1_dozens, score_1_hundreds
    
    score_1_hundreds = 0
    score_1_dozens = 0
    score_1_unit = 0

    for a_block in blocks_group:
        a_block.kill() 
    
    create_blocks()
    run = False
    if not run:
        paddle_width = SCREEN_WIDTH
        pygame.time.set_timer(pygame.USEREVENT+1, 5000)

# score and life 
text_life_1 = font.render(life_1, True, color_text)
pos_text_life_1 = text_life_1.get_rect()
pos_text_life_1.center = (20, 70)

text_life = font.render(str(life), True, color_text)
pos_text_life_2 = text_life.get_rect()
pos_text_life_2.center = (220, 70)

text_score_1 = font.render(str(score_1_hundreds)\
                          +str(score_1_dozens)\
                          +str(score_1_unit), True, color_text)

pos_text_score_1 = text_score_1.get_rect()
pos_text_score_1.center = (65, 100)

text_score_2 = font.render(score_2, True, color_text)
pos_text_score_2 = text_score_2.get_rect()
pos_text_score_2.center = (265, 100)

def update_life():
    global life, text_life, run
    if run:
        life +=1
    text_life = font.render(str(life), True, color_text)
    if life == 4:
        endgame()
        life = 1
        text_life = font.render(str(life), True, color_text)

def break_block():
    for a_block in blocks_group:
        if ball.is_aabb_collision(a_block):
            ball.render(a_block.color)
            ball.dy *= -1
            impact_with_block.play()       
           
            # break block
            a_block.kill()
            
            # update score
            update_score(a_block.color)
            if score_1_unit > 4 and ball.dy < 7:
                ball.dy = ball.dy + 2
            if a_block.color == GREEN and ball.dy < 10:
                ball.dy = ball.dy + 3 
            if a_block.color == ORANGE and ball.dy < 14:
                ball.dy = ball.dy + 4
            if a_block.color == RED and ball.dy < 18:
                ball.dy = ball.dy + 4
        if len(blocks_group) < 1:
            create_blocks()

clock = pygame.time.Clock()
ball = Ball()

# Game_loop
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if event.type == pygame.USEREVENT+1: 
            pygame.time.set_timer(pygame.USEREVENT+1, 0)
            run = True
            paddle_width = 40
            ball.y = SCREEN_HEIGHT/2
            ball.x = SCREEN_WIDTH/2
            x = SCREEN_WIDTH/2

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x -= 10
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x += 10

    ball.move()
    game_screen.fill((0, 0, 0))
    paddle = pygame.draw.rect(game_screen, BLUE, (x, y, paddle_width, paddle_height))
    
    if ball.is_aabb_collision(paddle):
        ball.dy *= -1
        impact_with_paddle.play()

    if x <= 0:
        x = 0
    if x >= SCREEN_WIDTH - paddle_width:
        x = SCREEN_WIDTH - paddle_width

    ball.render()

    game_screen.blit(text_life_1, pos_text_life_1)
    game_screen.blit(text_life, pos_text_life_2)
    game_screen.blit(text_score_1, pos_text_score_1)
    game_screen.blit(text_score_2, pos_text_score_2)
    text_score_1 = font.render(str(score_1_hundreds)\
                                +str(score_1_dozens)\
                                +str(score_1_unit), True, color_text)
        
    if run:    
        break_block()
    else:
        if ball.y <= 230:
            ball.dy *= -1
            impact_with_block.play()
        if ball.y >= y:
            ball.dy *= -1
            impact_with_paddle.play()

    screen_limit()
    blocks_group.draw(game_screen)
    
    blocks_group.update()
    pygame.display.update()