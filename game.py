# TODO : Vectors for x/y
# TODO : Switch current_position_p1 to use Player.x_coordinate

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
        scaled_images.append(pygame.transform.scale2x(pygame.image.load(path + '/' + image_string)))
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
                    player_one.pos)

        screen.blit(player_two.standing_images[player_two.current_standing_image],
                    player_two.pos)
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
# last_input_p1 = Input.NONE
# last_input_p2 = Input.NONE
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

race_started = False
have_winner = False

# main game loop
print("STARTING RACE")
ticks = 0
go_text = "GO"

pygame.font.init()
countdown_font = pygame.font.SysFont('Arial', 60)

#starting_line()

while not have_winner:
    ticks += 1
    p1_have_key = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting program...")
            sys.exit()

        if event.type == pygame.KEYUP:
            p1_have_key = True
            player_one.update(event.key)

    if not p1_have_key:
        #print ("SLOWING")
        player_one.update_running_speed(0)

    # RENDERING
    screen.fill(WHITE)

    text_surface = countdown_font.render(go_text, False, (0, 0, 0))
    screen.blit(text_surface, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    # display new positions
    screen.blit(player_one.running_images[player_one.current_running_image],
                player_one.pos)
    pygame.display.update()

    #print (tick)
    if ticks >= FPS:
        ticks = 0
        go_text = ""

    clock.tick(FPS) # 60 -> 60 fps
