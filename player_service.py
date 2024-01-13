from collections import defaultdict
import random


class Player:

    def __init__(self, no_of_players, player_list):
        self.n = no_of_players
        self.counter = 45
        self.player_arr = defaultdict()
        self.player_names = player_list
        self.set_input()

    def set_input(self):
        for player in self.player_names:
            self.player_arr[player] = {"last_position": 0, "id": self.counter}
            self.counter+=1

    def get_last_position(self, name):
        return self.player_arr[name]["last_position"]

    def set_position(self, name, position):
        self.player_arr[name]["last_position"] = position

    def get_data(self):
        return self.player_arr
