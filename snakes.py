from collections import defaultdict


class Snakes:

    def __init__(self):
        self.snakes_arr = {}
        self.set_input()

    def set_input(self):
        number_of_snakes = int(input("Enter the number of snakes "))
        while number_of_snakes:
            head_snake = int(input("Enter the head position of snake "))
            tail_snake = int(input("Enter the tail position of snake "))
            if tail_snake > head_snake:
                raise Exception("Tail can't be greater than head of snake ")
            self.snakes_arr[head_snake] = tail_snake
            number_of_snakes -= 1
        return self.snakes_arr

    def get_input(self):
        return self.snakes_arr

    def return_ending(self, start):
        return self.snakes_arr[start]
