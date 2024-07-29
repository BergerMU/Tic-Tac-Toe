import sys, pygame
pygame.init()

size = w, h = 300, 800 # right side = 940 left side = 0 top = 0 bottom = 740
speed = [1, 1]
black = 0, 0, 0
squareSize = min(w,h)
squareSize -= squareSize/9
box = pygame.Rect((w/2) - (squareSize/2), (h/2) - (squareSize/2), squareSize, squareSize)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    #Drawing abox then individual lines
    pygame.draw.rect(screen, "white", box, 7)
    #Vertical Lines
    pygame.draw.line(screen, "white", (box.left + box.width/3, box.top), (box.left + box.width/3, box.bottom - 5), 7)
    pygame.draw.line(screen, "white", (box.right - box.width/3, box.top), (box.right - box.width/3, box.bottom - 5), 7)
    # #Horizontal Lines
    pygame.draw.line(screen, "white", (box.left, box.top + box.height/3), (box.right - 5, box.top + box.height/3), 7)
    pygame.draw.line(screen, "white", (box.left, box.bottom - box.height/3), (box.right - 5, box.bottom - box.height/3), 7)


    #alternative method for creating boxes
    #find center of screen
    #set boxsizes according to how large screen is
    #place a box at the center and offset the other boxes using boxsize
    #could also assign numbers 1-9 to each box as I create them so it can just output what number I assigned it to the TicTacToe program I wrote


    pygame.MOUSEBUTTONDOWN

    pygame.display.update()
pygame.quit()