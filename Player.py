from Input import Input


class Player(object):
    """
    """

    def __init__(self, is_ai, ai_skill, player_number, base_speed, current_position, running_images, walking_images,
                 standing_images, x_coordinate):
        self.is_ai = is_ai
        self.ai_skill = ai_skill
        self.is_taking_part = False
        self.player_number = player_number
        self.current_position = current_position
        self.base_speed = base_speed
        self.velocity = 1
        self.running_images = running_images
        self.walking_images = walking_images
        self.standing_images = standing_images
        self.sliding_images = sliding_images
        self.current_running_image = 0
        self.current_walking_image = 0
        self.current_standing_image = 0
        self.current_sliding_image = 0
        self.is_winner = False
        self.x_coordinate = x_coordinate
        self.last_input = Input.NONE

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
        print (self.x_coordinate)

    " take an input and update the velocity depending on previous inputs "
    def update_velocity(self, input):
        print (input)
        if self.is_ai:
            print ("AI: Auto calculate based on ai skill")
