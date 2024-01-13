class Ladder:
    def __init__(self):
        self.ladder_arr = {}
        self.set_input()

    def set_input(self):
        number_of_ladders = int(input("Enter the number of ladders "))
        while number_of_ladders:
            start_ladder = int(input("Enter the starting position of ladder "))
            end_ladder = int(input("Enter the ending position of ladder "))
            if start_ladder > end_ladder:
                raise Exception("End can't be greater than Start ")
            self.ladder_arr[start_ladder] = end_ladder
            number_of_ladders -= 1
        return self.ladder_arr

    def get_input(self):
        return self.ladder_arr

    def return_ending(self, start):
        return self.ladder_arr[start]
