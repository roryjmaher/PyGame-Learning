# TODO : Vectors for x/y
# TODO : Switch current_position_p1 to use Player.x_coordinate
# TODO : animation.py (Class Animation(self, directory)

# TODO : Allow Start with Left OR Right when Speed = NONE
# TODO : Re-factor and allow 4 players
# TODO : Sliding. A slide at the end gives a boost to speed but if you don't make it you are boned.
# TODO : Add win condition/let all players finish but show positions. Add end line.
# TODO : Show all positions during the race in real time.
# TODO : Main Menu / Select Player
# TODO : Starting image of character standing. Winning image ?
# TODO : Add Game Timer to show player score/time.
# TODO : Add AI with levels.
# TODO : Allow Handicap/Stamina.
# TODO : Pick a character. Character Player stats. Top Speed/Stamina.
# TODO : Improve Timing.

#
# NOTE: Main loop -> ( Menu -> Selct Type (race, Hurdles etc...) -> race.run()/hurdles.run() -> Results -> Menu)
#


import os
import sys
import pygame

from player import Player
from input import Input
import controls
from settings import *



def load_images_from_directory(path):
    scaled_images = []
    p1SpriteList = os.listdir(path)
    for image_string in p1SpriteList:
        scaled_images.append(pygame.transform.scale2x(pygame.image.load(path + '/' + image_string).convert_alpha()))
    return scaled_images


def starting_line():
    load_images_from_directory('./Assets/Images/Other/Countdown')
    race_countdown = 5
    race_started = False
    ticks = 0
    pygame.font.init()
    countdown_font = pygame.font.SysFont('Arial', 60)

    # starting line
    while not race_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting program...")
                sys.exit()

        # RENDERING
        screen.fill(WHITE)
        screen.blit(player_one.standing_images[player_one.current_standing_image],
                    (player_one.x + current_position_p1, player_one.y))

        screen.blit(player_two.standing_images[player_two.current_standing_image],
                    (player_two.x + current_position_p2, player_two.y))
        player_one.next_standing_image()
        player_two.next_standing_image()

        if ticks % 10 == 0:
            print (race_countdown)
            race_countdown -= 1

        ticks -= 1
        if race_countdown < 0:
            race_started = True

        clock.tick(10)

        if race_countdown > 0:
            text_surface = countdown_font.render(str(race_countdown), False, (0, 0, 0))
        screen.blit(text_surface, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        pygame.display.update()

# MAIN

# something to store movement
last_input_p1 = Input.NONE
last_input_p2 = Input.NONE
STARTING_X = 50

# Setup the players
player_one = Player(False, 100, 1, 1, 0,
                    load_images_from_directory('./Assets/Images/Brown Bear/Brown Bear Frames/Running'),
                    load_images_from_directory('./Assets/Images/Brown Bear/Brown Bear Frames/Walking'),
                    load_images_from_directory('./Assets/Images/Brown Bear/Brown Bear Frames/Standing'),
                    load_images_from_directory('./Assets/Images/Brown Bear/Brown Bear Frames/Sliding'),
                    STARTING_X, 350,
                    controls.Controls(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RETURN))
player_two = Player(False, 100, 2, 1, 0,
                    load_images_from_directory('./Assets/Images/Cat/Cat Frames/Running'),
                    load_images_from_directory('./Assets/Images/Cat/Cat Frames/Walking'),
                    load_images_from_directory('./Assets/Images/Cat/Cat Frames/Standing'),
                    load_images_from_directory('./Assets/Images/Cat/Cat Frames/Sliding'),
                    STARTING_X, 450,
                    controls.Controls(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE ))

# set the screen size
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set-Up
# set starting frames
current_position_p1 = 0
current_position_p2 = 0

clock = pygame.time.Clock()
total_time = 0.0
time_tracker = 0.0


speed_per_second_p1 = 1
have_p1_key_up = False
speed_per_second_p2 = 1
have_p2_key_up = False




race_started = False
have_winner = False


ticks = 0


# main game loop
print("STARTING RACE")
ticks = 0
go_text = "GO"

pygame.font.init()
countdown_font = pygame.font.SysFont('Arial', 60)

starting_line()
p1_inputs = 0

while not have_winner:
    ticks += 1

    # reset all keyboard movement booleans
    have_p1_key_up = False
    have_p2_key_up = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting program...")
            sys.exit()

        # have a look see if a player one released correct key
        if event.type == pygame.KEYUP:
            p1_inputs += 1
            # Player 1 - LEFT/RIGHT
            if event.key == pygame.K_LEFT:
                have_p1_key_up = True
                if last_input_p1 == Input.RIGHT:
                    speed_per_second_p1 += PIXEL_PER_TICK
                elif last_input_p1 == Input.LEFT:
                    speed_per_second_p1 += (PIXEL_PER_TICK * 0.95)

                last_input_p1 = Input.LEFT

            elif event.key == pygame.K_RIGHT:
                have_p1_key_up = True
                if last_input_p1 == Input.LEFT:
                    speed_per_second_p1 += PIXEL_PER_TICK
                elif last_input_p1 == Input.RIGHT:
                    speed_per_second_p1 += (PIXEL_PER_TICK * 0.95)

                last_input_p1 = Input.RIGHT

            print ('%s : %s' % (p1_inputs, speed_per_second_p1))
            # Player 2 - A = LEFT /D = RIGHT
            if event.key == pygame.K_a:
                have_p2_key_up = True

                if last_input_p2 == Input.RIGHT:
                    speed_per_second_p2 += PIXEL_PER_TICK
                elif last_input_p2 == Input.LEFT:
                    speed_per_second_p2 += (PIXEL_PER_TICK * 0.95)

                last_input_p2 = Input.LEFT

            elif event.key == pygame.K_d:
                have_p2_key_up = True

                if last_input_p2 == Input.LEFT:
                    speed_per_second_p2 += PIXEL_PER_TICK
                elif last_input_p2 == Input.RIGHT:
                    speed_per_second_p2 += (PIXEL_PER_TICK * .95)

                last_input_p2 = Input.RIGHT
                #print ("Speed_per_second : %s : %s" % (speed_per_second_p1, speed_per_second_p2))

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

    if ticks >= FPS:
        print ("1 Second: %s" % time_tracker)

    # if we moved at all then get next sprite frame
    #if speed_per_second > 0:
    if ticks % 5 == 0:
        if speed_per_second_p1 > 0:
            player_one.current_running_image += 1
            if player_one.current_running_image >= len(player_one.running_images):
                player_one.current_running_image = 0
        if speed_per_second_p2 > 0:
            player_two.current_running_image += 1
            if player_two.current_running_image >= len(player_two.running_images):
                player_two.current_running_image = 0

    # RENDERING
    screen.fill(WHITE)

    text_surface = countdown_font.render(go_text, False, (0, 0, 0))
    screen.blit(text_surface, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    # TODO: see if we have a winner. See who actually won.
    if current_position_p1 >= (WINDOW_WIDTH - 100):
        have_winner = True
    elif current_position_p2 >= (WINDOW_WIDTH - 100):
        have_winner = True

    # display new positions
    screen.blit(player_one.running_images[player_one.current_running_image],
                (player_one.x + current_position_p1, player_one.y))
    screen.blit(player_two.running_images[player_two.current_running_image],
                (player_one.x + current_position_p2, player_two.y))
    #print ("%s : %s" % (current_position_p1,current_position_p2))
    pygame.display.update()

    #print (tick)
    if ticks >= FPS:
        ticks = 0
        go_text = ""

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
