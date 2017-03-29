# TODO Next : Scale. Jump. Velocity & Animation of Velocity
# Scale http://www.geon.wz.cz/pygame/ref/pygame_transform.html
# Scale resize in paint vs ingame
import sys
import pygame
from enum import Enum


class Input(Enum):
    NONE = 1
    LEFT_DOWN = 2
    RIGHT_DOWN = 3
    LEFT_UP = 4
    RIGHT_UP = 5

# something to store movement
last_input = Input.NONE
current_input = Input.NONE


#
def apply_image_scaling_to_list(scaling_function, images):
    scaled_images = []
    for image in images:
            scaled_images.append(scaling_function(image))
    return scaled_images

screen = pygame.display.set_mode((800,600))

imagesBear = []
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_17.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_18.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_19.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_20.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_21.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_22.png'))

# scale all the images
scaledBearImages = apply_image_scaling_to_list(pygame.transform.scale2x, imagesBear)

current_bear_image = 0
WHITE = (255,255,255)

# scale an image testing
# image_for_scaling = pygame.image.load('./Assets/Images/Fox/Fox Frames/Fox_17.png')
# scaled_fox_image = pygame.transform.smoothscale(image_for_scaling, (50, 50))
# scale2x_fox_image = pygame.transform.scale2x(image_for_scaling)

game_in_progress = True
clock = pygame.time.Clock()
STARTING_X = 50
x = 1
velocity = 1
have_key_up = False
while True:
    #re/set all keyboard movement bools
    have_key_up = False

    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            print("Exiting program...")
            sys.exit()
        if event.type == pygame.KEYUP:
            have_key_up = True
            if event.key == pygame.K_LEFT:
                print ("UP L")
                if last_input == Input.RIGHT_UP:
                    velocity += 1
                #elif last_input == Input.NONE:
                #    velocity += 1
                else:
                    velocity -= 1
                last_input = Input.LEFT_UP
            elif event.key == pygame.K_RIGHT:
                print ("UP R")
                if last_input == Input.LEFT_UP:
                    velocity += 1
                #elif last_input == Input.NONE:
                #    velocity += 1
                else:
                    velocity -= 1
                last_input = Input.RIGHT_UP
    # check for the current input
    # check for the previous input
    # if last and current work together then increase velocity
    # otherwise stagnate or decrease velocity depending
    # if no input then dcrease velocity to (possbly to 0)

    # Process Player Input
    #right = pygame.key.get_pressed()[pygame.K_RIGHT]
    #left = pygame.key.get_pressed()[pygame.K_LEFT]
    print(velocity)
    if (velocity > 5):
        velocity = 5
    if (velocity < 0):
        velocity = 0


    if (velocity > 0):
        current_bear_image += 1
        if current_bear_image >= len(imagesBear):
            current_bear_image = 0

    # current_cat_image += 1
    # if current_cat_image >= len(imagesCat):
    #     current_cat_image = 0

    # THIS IS THE PROBLEM
    if have_key_up:
        x += x * velocity

    print ('x pos %s' % (x))
    #x *= velocity
    # RENDERING
    screen.fill(WHITE)
    screen.blit(scaledBearImages[current_bear_image], (STARTING_X + x, 250))
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