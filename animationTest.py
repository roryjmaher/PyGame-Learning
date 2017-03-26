# TODO Next : Scale. Jump. Velocity & Animation of Velocity
# Scale http://www.geon.wz.cz/pygame/ref/pygame_transform.html
# Scale resize in paint vs ingame
import sys
import pygame


#
def apply_image_scaling_to_list(scaling_function, images):
    scaled_images = []
    for image in images:
            scaled_images.append(scaling_function(image))
    return scaled_images

screen = pygame.display.set_mode((800,600))

imagesBear = []
imagesCat = []
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_17.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_18.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_19.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_20.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_21.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_22.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_17.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_18.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_19.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_20.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_21.png'))
imagesCat.append(pygame.image.load('./Assets/Images/Cat/Cat Frames/Cat_22.png'))

# scale all the images
scaledCatImages = apply_image_scaling_to_list(pygame.transform.scale2x, imagesCat)
scaledFoxImages = apply_image_scaling_to_list(pygame.transform.scale2x, imagesBear)

current_bear_image = 0
current_cat_image = 0
WHITE = (255,255,255)

# scale an image testing
# image_for_scaling = pygame.image.load('./Assets/Images/Fox/Fox Frames/Fox_17.png')
# scaled_fox_image = pygame.transform.smoothscale(image_for_scaling, (50, 50))
# scale2x_fox_image = pygame.transform.scale2x(image_for_scaling)

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
        if current_bear_image >= len(imagesBear):
            current_bear_image = 0

    current_cat_image += 1
    if current_cat_image >= len(imagesCat):
        current_cat_image = 0

    # RENDERING
    screen.fill(WHITE)
    #screen.blit(imagesBear[current_bear_image], (x, 250))
    #screen.blit(imagesCat[current_cat_image], (50, 300))
    screen.blit(scaledCatImages[current_bear_image], (x, 250))
    screen.blit(scaledFoxImages[current_cat_image], (50, 300))
    #screen.blit(scaled_fox_image, (300, 200))
    #screen.blit(scale2x_fox_image, (300, 400))
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
Running - 17,18,19,20,21,22 - 6
'''