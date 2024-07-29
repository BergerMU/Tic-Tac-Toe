import sys, pygame
pygame.init()

size = w, h = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

#Define Variables
one_third = int(h / 3)
line_width = 7
markers = [[0,0,0], [0,0,0], [0,0,0]]
clicked = False
pos = []
player = 1
winner = 0
game_over = False

#define colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#define font
font = pygame.font.SysFont(None, 40)

#create play again rectangle
again_rect = pygame.Rect(w // 2 - 80, h // 2, 160, 50)

def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for i in range(1,3):
        pygame.draw.line(screen, grid, (0, i*one_third), (w, i*one_third), line_width)
        pygame.draw.line(screen, grid, (i*one_third, 0), (i*one_third, h), line_width)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:  #Draws Cross
                pygame.draw.line(screen, green, (x_pos*one_third + 15, y_pos*one_third + 15), (x_pos*one_third + 85, y_pos*one_third + 85), line_width)
                pygame.draw.line(screen, green, (x_pos*one_third + 15, y_pos*one_third + 85), (x_pos*one_third + 85, y_pos*one_third + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos*one_third + 50, y_pos*one_third + 50), 30, line_width)
            y_pos += 1
        x_pos += 1

def restart():
    markers = [[0,0,0], [0,0,0], [0,0,0]]
    # draw_grid()


def check_winner():
    global winner
    global game_over
    y_pos = 0

    for x in markers:
        #check columns
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        #check rows
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    #check diagonals
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True

def draw_winner(winner):
    win_text = 'Player ' + str(winner) + " wins!"
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (w // 2 - 100, h // 2 - 60, 200, 50))
    screen.blit(win_img, (w // 2 - 100, h // 2 - 50))

    #play again
    again_text = 'Play Again?'
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (w //2 -80, h // 2 + 10))

while True:
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // one_third][cell_y // one_third] == 0:
                    markers[cell_x // one_third][cell_y // one_third] = player
                    player *= -1
                    check_winner()

    if game_over == True:
        draw_winner(winner)
        #check for mouse click to see if player clicks "play again?"
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                #reset variables
                markers = [[0,0,0], [0,0,0], [0,0,0]]
                pos = []
                player = 1
                winner = 0
                game_over = False
                
    pygame.display.update()
pygame.quit