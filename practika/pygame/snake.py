import pygame
import random
pygame.init()

pink2_fon = (255,192,203)
blue = (0,128,0)
red = (255,69,0)
grey =(188,143,143)
pink = (255,182,193)
grey2 = (128,128,128)
black = (0,0,0)
obod = (105,105,105)

dis = pygame.display.set_mode((500, 600))

time = 2
x = 220
y = 220
print(x)
x_change = 0
y_change = 0
a = random.randrange(20, 480, 20)
c = random.randrange(100, 580, 20)
BLOCK = 20
colonkX = 24
colonkY = 29
count = 0
snake_len = 1
snake_List = []


pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

game_over = False

while not game_over:

    for event in pygame.event.get():  # перебираем события
        if event.type == pygame.QUIT:  # крестик в игре
            game_over = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -20
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 20
            elif event.key == pygame.K_LEFT:
                x_change = -20
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 20
                y_change = 0

    if x >= 480 or x < 20 or y >= 580 or y < 100:
        game_over = True
    x += x_change
    y += y_change
    dis.fill(pink2_fon)

    #рисую сетку
    for i in range(5, colonkY):
        for q in range(1, colonkX):
            if (i+q) % 2 == 0:
                color = grey
            else:
                color = pink
            pygame.draw.rect(dis, color, (q * BLOCK, i * BLOCK, BLOCK, BLOCK))


    def our_snake(BLOCK, snake_List):
        for q in snake_List:
            pygame.draw.rect(dis, blue, [q[0], q[1], BLOCK, BLOCK])

    snake_List2 = []
    snake_List2.append(x)
    snake_List2.append(y)
    snake_List.append(snake_List2)
    if len(snake_List) > snake_len:
        snake_List.pop(0)
        for q in snake_List[:-1]:
            if q == snake_List2:
                game_over = True

    # print(snake_List)
    our_snake(BLOCK, snake_List)

    if x == a and y == c:
        a = random.randrange(20, 480, 20)
        c = random.randrange(100, 580, 20)
        time += 0.5
        count += 1
        snake_len += 1

    # Наполнить
    food = pygame.draw.ellipse(dis, red, (a, c, BLOCK, BLOCK))
    pygame.draw.rect(dis, grey2,(20, 10, 460, 75))

    #ободки
    pygame.draw.rect(dis, obod,(20, 10, 460, 75),1)
    pygame.draw.rect(dis, (222,184,135), (19, 99, 462, 482), 1)
    food_obod = pygame.draw.ellipse(dis, (255, 0, 0), (a, c, BLOCK, BLOCK), 1)

    font = pygame.font.SysFont('Helvetica',75)
    text = font.render(f'{count}',5 , black)
    dis.blit(text,(235, 5))

    pygame.display.update()
    clock.tick(time)

pygame = quit()
quit()
