from input import Input
import settings
from controls import Controls
import pygame
import pygame as pg
vec = pg.math.Vector2
from enum import Enum

#
class State(Enum):
    NONE = 0
    IN_MENU = 1
    IN_RUNNING_GAME = 2
    IN_HURDLES_GAME = 3
    GAME_OVER = 4


# enum for possible Animation States
class AnimationState(Enum):
    NONE = 0
    WALKING = 1
    RUNNING = 2
    SLIDING = 3
    JUMPING = 4


class Player(object):
    """
    """

    def __init__(self, is_ai, ai_skill, player_number, base_speed, current_position, running_images, walking_images,
                 standing_images, sliding_images, x_coordinate, y_coordinate, controls):
        self.is_ai = is_ai
        self.ai_skill = ai_skill
        self.is_taking_part = False
        self.player_number = player_number

        self.running_images = running_images
        self.walking_images = walking_images
        self.standing_images = standing_images
        self.sliding_images = sliding_images
        self.current_running_image = 0
        self.current_walking_image = 0
        self.current_standing_image = 0
        self.current_sliding_image = 0
        self.is_winner = False

        self.current_position = current_position
        self.base_speed = base_speed
        self.velocity = 1
        self.x = x_coordinate
        self.y = y_coordinate
        self.pos = vec(x_coordinate, y_coordinate)
        self.vel = vec(0,0)
        self.acc = vec(0,0)


        self.last_input = Input.NONE
        self.controls = controls
        self.state = State.NONE
        self.game_state = AnimationState.NONE
        self.state = State.IN_RUNNING_GAME

    def next_standing_image(self):
        self.current_standing_image += 1
        if self.current_standing_image >= len(self.standing_images):
            self.current_standing_image = 0

    def next_walking_image(self):
        self.current_walking_image += 1
        if self.current_walking_image >= len(self.walking_images):
            self.current_walking_image = 0

    def next_running_image(self):
        self.current_running_image += 1
        if self.current_running_image >= len(self.running_images):
            self.current_running_image = 0

    def next_sliding_image(self):
        self.current_sliding_image += 1
        if self.current_sliding_image >= len(self.sliding_images):
            self.current_sliding_image = 0

    " gets the next x position of the player based on the current x_coordinate and the velocity "
    def get_new_position(self):
        # do some calculations
        print (self.pos.x)

    " take an input and update the velocity depending on previous inputs "
    def update_velocity(self, input):
        print (input)
        if self.is_ai:
            print ("AI: Auto calculate based on ai skill")

    def update_running_speed(self, x_acc):
        # update the position based on current speed
        self.acc += self.vel * settings.PLAYER_FRICTION
        self.vel.x += x_acc

        # enforce a speed limit
        if self.vel.x > 10:
            self.vel.x = 10
        if self.vel.x < 0:
            self.vel.x = 0

        print (self.vel + 0.5 * self.acc)
        self.pos += self.vel + 0.5 * self.acc
        #print("pos (%s) vel (%s) acc(%s)" % (self.pos, self.vel, self.acc))

    def update(self, user_input):
        print ('Player State is %s' % self.state)
        print ('%s got input %s' % (self.player_number, user_input))

        if self.state == State.IN_MENU:
            print ('handle input MENU')
            # have a look see if a player one released correct key
            if user_input == self.controls.left:
                print('handle input LEFT')
            elif user_input == self.controls.right:
                print('handle input RIGHT')
            elif user_input == self.controls.up:
                print('handle input UP')
            elif user_input == self.controls.down:
                print('handle input DOWN')
            elif user_input == self.controls.select:
                print('handle input SELECT')
            else:
                print('%s got UNSUPPORTED input %s' % (self.player_number, user_input))

        elif self.state == State.IN_RUNNING_GAME:
            print('handle input RUNNING')
            # have a look see if a player one released correct key
            if user_input == self.controls.left:
                print('handle input LEFT')
                if self.last_input == self.controls.right:
                    self.acc.x += settings.PLAYER_ACC
                elif self.last_input == self.controls.left:
                    self.acc.x += 0.1
            elif user_input == self.controls.right:
                print('handle input RIGHT')
                if self.last_input == self.controls.left:
                    self.acc.x += settings.PLAYER_ACC
                elif self.last_input == self.controls.right:
                    self.acc.x += 0.1
            else:
                print('%s got UNSUPPORTED input %s' % (self.player_number, user_input))

            # save this input
            self.last_input = user_input

            # update the position based on current speed
            self.update_running_speed(self.acc.x)





