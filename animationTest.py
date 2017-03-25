# TODO Next : Scale. Jump. Velocity & Animation of Velocity

import sys, pygame

screen = pygame.display.set_mode((800,600))

imagesBear = []
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_17.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_18.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_19.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_21.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_21.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_22.png'))
imagesCat = []
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_17.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_18.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_19.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_21.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_21.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_22.png'))
bearImages = 5
catImages = 5

num_images = 5
current_bear_image = 0
current_cat_image = 0
WHITE = (255,255,255)
game_in_progress = True

clock = pygame.time.Clock()
x = 50
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting program...")
            sys.exit()

    # Process Player Input
    right = pygame.key.get_pressed()[pygame.K_RIGHT]
    left = pygame.key.get_pressed()[pygame.K_LEFT]

    if right:
        x += 2
        current_bear_image += 1
        if current_bear_image > 5:
            current_bear_image = 0

    current_cat_image += 1
    if current_cat_image > 5:
        current_cat_image = 0

    # RENDERING
    screen.fill(WHITE)
    screen.blit(imagesBear[current_bear_image], (x, 250))
    screen.blit(imagesCat[current_cat_image], (50, 300))
    pygame.display.update()
    clock.tick(10) # 60 -> 60 fps


'''Animation
Name - Frames - Recommended FPS - Note
Passive - 1,1,2,2 - 6
Jumping - 11,12,13 - 6 - Hold frame 11 going upwards, 13 going downwards. 12 is a transition between 11, 13.
Slide - 14,15,14,16 - 6
Walking - 3,4,5,6,7,8,9,10 - 6
Teleport (Mid-air) - 25,26,27,28,29,30,31,32,33,34 - 6 - It is supposed to used mid-air so that the character falls down on the ground.
Teleport (Ground) - 25,26,27,28,29,30,2 - 6
Hit - 23,24,2,1 - 6 - Hold frame 23 when the character is pushed backwards
Running - 17,18,19,21,21,22 - 6
'''