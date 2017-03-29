# TODO : rename vars to P1. Add P2. Improve Timing. Add win condition. Add end line.
# TODO : Add Game Timer to show player score/time.
# TODO : Add AI with levels.

import sys
import pygame
from enum import Enum

# enum for input detection
class Input(Enum):
    NONE = 1
    LEFT_DOWN = 2
    RIGHT_DOWN = 3
    LEFT_UP = 4
    RIGHT_UP = 5

# something to store movement
last_input = Input.NONE
p2_last_input = Input.NONE


# set teh screen size
screen = pygame.display.set_mode((800,600))

# load all images
imagesBear = []
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_17.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_18.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_19.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_20.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_21.png'))
imagesBear.append(pygame.image.load('./Assets/Images/Brown Bear/Brown Bear Frames/Brown Bear_22.png'))

# scale all the images
scaled_bear_images = []
for image in imagesBear:
    scaled_bear_images.append(pygame.transform.scale2x(image))

# Set-Up
# set starting frames
current_bear_image = 0
WHITE = (255,255,255)
game_in_progress = True
clock = pygame.time.Clock()
STARTING_X = 50
current_position = 0
velocity = 1
have_p1_key_up = False

while True:
    #re/set all keyboard movement bools
    have_p1_key_up = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting program...")
            sys.exit()

        # have a look see if player pressed the up key
        if event.type == pygame.KEYUP:
            have_p1_key_up = True
            if event.key == pygame.K_LEFT:
                if last_input == Input.RIGHT_UP:
                    velocity += 1
                last_input = Input.LEFT_UP
            elif event.key == pygame.K_RIGHT:
                if last_input == Input.LEFT_UP:
                    velocity += 1
                last_input = Input.RIGHT_UP

    # no key press so slow down
    if not have_p1_key_up:
        velocity -= 1

    # Keep velocity in check
    if velocity > 15:
        velocity = 15
    if velocity < 0:
        velocity = 0

    # if we moved at all then get next sprite frame
    if velocity > 0:
        current_bear_image += 1
        if current_bear_image >= len(imagesBear):
            current_bear_image = 0

    # add velocity for this clock tick to current X position
    current_position += velocity

    # RENDERING
    screen.fill(WHITE)
    screen.blit(scaled_bear_images[current_bear_image], (STARTING_X + current_position, 250))
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