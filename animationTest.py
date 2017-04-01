# TODO : Add a player Class. Include Images, Name, Position so we can sort list of players at end results.
# TODO : Add win condition. Add end line.
# TODO : Starting image of character standing. Winning image ?
# TODO : Add Game Timer to show player score/time.
# TODO : Add AI with levels.
# TODO : Allow Start with Left OR Right when Speed = NONE
# TODO : Re-factor and allow 4 players
# TODO : Allow Handicap/Stamina.
# TODO : Pick a character. Character Player stats. Top Speed/Stamina.
# TODO : Improve Timing.

import sys
import pygame
from enum import Enum
import os

# enum for input detection
class Input(Enum):
    NONE = 1
    LEFT = 2
    RIGHT = 3

def setup_player_images(path):
    scaled_images = []
    p1SpriteList = os.listdir(path)
    for image_string in p1SpriteList:
        scaled_images.append(pygame.transform.scale2x(pygame.image.load(path + '/' + image_string)))
    return scaled_images

# something to store movement
last_input_p1 = Input.NONE
last_input_p2 = Input.NONE

#load the player images
player_one_images = setup_player_images('./Assets/Images/Brown Bear/Brown Bear Frames/Running')
player_two_images = setup_player_images('./Assets/Images/Cat/Cat Frames/Running')

# set the screen size
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# Set-Up
# set starting frames
current_p1_image = 0
current_p2_image = 0
current_position_p1 = 0
current_position_p2 = 0

WHITE = (255,255,255)
clock = pygame.time.Clock()
total_time = 0.0
time_tracker = 0.0
STARTING_X = 50


speed_per_second_p1 = 1
have_p1_key_up = False
speed_per_second_p2 = 1
have_p2_key_up = False

tick = 0
FPS = 60

# pixel spped ups and slowdown
PIXEL_PER_TICK = 3
PIXEL_SLOWDOWN = .5

have_winner = False

# main game loop
while not have_winner:
    tick += 1

    # reset all keyboard movement booleans
    have_p1_key_up = False
    have_p2_key_up = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting program...")
            sys.exit()

        # have a look see if a player one released correct key
        if event.type == pygame.KEYUP:
            # Player 1 - LEFT/RIGHT
            if event.key == pygame.K_LEFT:
                have_p1_key_up = True
                if last_input_p1 == Input.RIGHT:
                    speed_per_second_p1 += PIXEL_PER_TICK
                last_input_p1 = Input.LEFT
            elif event.key == pygame.K_RIGHT:
                have_p1_key_up = True
                if last_input_p1 == Input.LEFT:
                    speed_per_second_p1 += PIXEL_PER_TICK
                last_input_p1 = Input.RIGHT

            # Player 2 - A/D
            if event.key == pygame.K_a:
                have_p2_key_up = True
                if last_input_p2 == Input.RIGHT:
                    speed_per_second_p2 += PIXEL_PER_TICK
                last_input_p2 = Input.LEFT
            elif event.key == pygame.K_d:
                have_p2_key_up = True
                if last_input_p2 == Input.LEFT:
                    speed_per_second_p2 += PIXEL_PER_TICK
                last_input_p2 = Input.RIGHT

    print ("Speed_per_second : %s : %s" % (speed_per_second_p1, speed_per_second_p2))
    # no key press so slow down
    if not have_p1_key_up:
        speed_per_second_p1 -= PIXEL_SLOWDOWN
    if not have_p2_key_up:
        speed_per_second_p2 -= PIXEL_SLOWDOWN

    # Keep velocity in check
    if speed_per_second_p1 > 15:
        speed_per_second_p1 = 15
    if speed_per_second_p1 < 0:
        speed_per_second_p1 = 0

    if speed_per_second_p2 > 15:
        speed_per_second_p2 = 15
    if speed_per_second_p2 < 0:
        speed_per_second_p2 = 0

    # clock calculations
    # time_passed = clock.tick()
    # time_passed_seconds = time_passed / 1000.0
    # time_tracker += time_passed
    # print (time_tracker)

    # add velocity for this clock tick to current X position
    current_position_p1 += speed_per_second_p1 / 2
    current_position_p2 += speed_per_second_p2 / 2

    if tick >= FPS:
        print ("1 Second: %s" % time_tracker)

    # if we moved at all then get next sprite frame
    #if speed_per_second > 0:
    if tick % 3 == 0:
        if speed_per_second_p1 > 0:
            current_p1_image += 1
            if current_p1_image >= len(player_one_images):
                current_p1_image = 0
        if speed_per_second_p2 > 0:
            current_p2_image += 1
            if current_p2_image >= len(player_two_images):
                current_p2_image = 0

    # RENDERING
    screen.fill(WHITE)

    # TODO: see if we have a winner. See who actually won.
    if (current_position_p1 >= (WINDOW_WIDTH - 100)):
        have_winner = True
    elif (current_position_p2 >= (WINDOW_WIDTH - 100)):
        have_winner = True

    # display new positions
    screen.blit(player_one_images[current_p1_image], (STARTING_X + current_position_p1, 250))
    screen.blit(player_two_images[current_p2_image], (STARTING_X + current_position_p2, 450))
    print ("%s : %s" % (current_position_p1,current_position_p2))
    pygame.display.update()

    #print (tick)
    if tick >= FPS:
        tick = 0
    clock.tick(FPS) # 60 -> 60 fps

# game is over
while have_winner:
    winning_image = pygame.image.load('./Assets/Images/Other/Winner-PNG-Image.png')
    screen.blit(winning_image, (0, 0))
    pygame.display.update()
    clock.tick(30)  # 60 -> 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting program...")
            sys.exit()

        # have a look see if a player one released correct key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                print("Exiting program...from ESC Input")
                sys.exit()

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