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
total_time = 0.0
time_tracker = 0.0
STARTING_X = 50
current_position = 0
speed_per_second = 1
have_p1_key_up = False
tick = 0
FPS = 60
while True:

    tick += 1
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
                    speed_per_second += 3
                last_input = Input.LEFT_UP
            elif event.key == pygame.K_RIGHT:
                if last_input == Input.LEFT_UP:
                    speed_per_second += 3
                last_input = Input.RIGHT_UP

    # no key press so slow down
    if not have_p1_key_up:
        speed_per_second -= .5

    # Keep velocity in check
    if speed_per_second > 15:
        speed_per_second = 15
    if speed_per_second < 0:
        speed_per_second = 0

    # clock calculations
    # time_passed = clock.tick()
    # time_passed_seconds = time_passed / 1000.0
    # time_tracker += time_passed
    # print (time_tracker)

    # add velocity for this clock tick to current X position
    current_position += speed_per_second / 2

    if tick >= FPS:
        print ("1 Second: %s" % time_tracker)

    # if we moved at all then get next sprite frame
    #if speed_per_second > 0:
    if tick % 3 == 0 and speed_per_second > 0:
        current_bear_image += 1
        if current_bear_image >= len(imagesBear):
            current_bear_image = 0


    # RENDERING
    screen.fill(WHITE)

    screen.blit(scaled_bear_images[current_bear_image], (STARTING_X + current_position, 250))

    pygame.display.update()

    #print (tick)
    if tick >= FPS:
        tick = 0
    clock.tick(FPS) # 60 -> 60 fps


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