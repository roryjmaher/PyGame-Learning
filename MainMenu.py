from Player import Player
import pygame
import os


class MainMenu(object):
    """
    """

    def __init__(self):
        self.all_selected = False
        # create our list of all possible players
        self.create_all_players()


    def menu_loop(self):
        self.display_menu()
        while True:
            self.get_inputs()
            # redraw


    def display_menu(self):
        print ("display_menu")


    def get_inputs(self):
        print ("get_inputs")


    def load_images_from_directory(self, path):
        scaled_images = []
        p1SpriteList = os.listdir(path)
        for image_string in p1SpriteList:
            scaled_images.append(pygame.transform.scale2x(pygame.image.load(path + '/' + image_string)))
        return scaled_images


    def create_all_players(self):
        STARTING_X = 50
        players = []
        players.append(
            Player(False, 100, 1, 1, 0,
                   self.load_images_from_directory('./Assets/Images/Brown Bear/Brown Bear Frames/Running'),
                   self.load_images_from_directory('./Assets/Images/Brown Bear/Brown Bear Frames/Walking'),
                   self.load_images_from_directory('./Assets/Images/Brown Bear/Brown Bear Frames/Standing'),
                   STARTING_X))
        players.append(Player(False, 100, 2, 1, 0,
                   self.load_images_from_directory('./Assets/Images/Cat/Cat Frames/Running'),
                   self.load_images_from_directory('./Assets/Images/Cat/Cat Frames/Walking'),
                   self.load_images_from_directory('./Assets/Images/Cat/Cat Frames/Standing'),
                   STARTING_X))
