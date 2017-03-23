import sys, pygame, platform

print(platform.python_version())

screen = pygame.display.set_mode((800,600))

p1Rect = pygame.Rect((50, 400, 50,50))
p2Rect = pygame.Rect((50, 500, 50,50))

red = (255,0,0)
green = (0,255,0)

game_in_progress = True

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 60)
winningtext = "Winner is: "

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting program...")
            sys.exit()

    quit = pygame.key.get_pressed()[pygame.K_ESCAPE]
    if quit:
        sys.exit()

    if game_in_progress:
        # Process Player Input
        right = pygame.key.get_pressed()[pygame.K_RIGHT]
        left= pygame.key.get_pressed()[pygame.K_LEFT]


        # Updating Game State Logic
        if right:
            p1Rect.x += 10
        if left:
            p2Rect.x += 10

        # RENDERING
        screen.fill((0,0,0))
        p1 = pygame.draw.rect(screen,red,p1Rect)
        p2 = pygame.draw.rect(screen,green,p2Rect)

        if p1Rect.x  >= 400 or p2Rect.x >= 400:
            if p1Rect.x > p2Rect.x:
                winningtext += " P1 Rect"
            elif p2Rect.x > p1Rect.x:
                winningtext += " P2 Rect"
            else:
                winningtext = "It's a Draw!!!!"
            textsurface = myfont.render(winningtext, False, (0, 255, 0))
            screen.blit(textsurface,(400,300))

            game_in_progress = False

        pygame.display.flip()
    clock.tick(60)