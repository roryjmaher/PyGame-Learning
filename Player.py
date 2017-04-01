from enum import Enum


class Player(object):
    """
    """

    def __init__(self, is_ai, player_number, base_speed, current_position, running_images, walking_images,
                 standing_images, x_coordinate):
        self.is_ai = False
        self.player_number = player_number
        self.current_position = current_position
        self.base_speed = base_speed
        self.running_images = running_images
        self.walking_images = walking_images
        self.standing_images = standing_images
        self.current_running_image = 0
        self.current_walking_image = 0
        self.current_standing_image = 0
        self.is_winner = False
        self.x_coordinate = x_coordinate
        self.last_input = Input.NONE

    def next_standing_image(self):
        self.current_standing_image += 1
        if self.current_standing_image >= len(self.standing_images):
            self.current_standing_image = 0

# enum for input detection
class Input(Enum):
    NONE = 1
    LEFT = 2
    RIGHT = 3