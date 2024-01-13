from player_service import Player
from snakes import Snakes
from ladder import Ladder
from dice import Dice
import Constants


class Board(Player):
    def __init__(self, n, player_list):
        self.n = n
        super().__init__(n, player_list)
        self.snakes_obj = Snakes()
        self.ladder_obj = Ladder()
        self.dice = Dice()
        self.maxi = 0

    def start(self):
        print("Created players successfully")
        while self.maxi != Constants.MAX_POINT:
            for idx, player_name in enumerate(self.player_names):
                dice_count = self.dice.roll()
                last_position = self.get_last_position(player_name)
                final = last_position + dice_count
                if final > Constants.MAX_POINT:
                    print(f"{player_name} couldn't move further ")
                    continue

                if final in self.snakes_obj.get_input():
                    latest_position = self.snakes_obj.return_ending(final)
                    self.maxi = max(self.maxi, latest_position)
                    self.set_position(player_name, latest_position)
                    print(
                        f"{player_name} started from {last_position} moved to {latest_position} bitten by snake, dice count {dice_count}")

                elif final in self.ladder_obj.get_input():
                    latest_position = self.ladder_obj.return_ending(final)
                    self.maxi = max(self.maxi, latest_position)
                    self.set_position(player_name, latest_position)
                    print(
                        f"{player_name} started from {last_position} moved to {latest_position} moving by ladder , dice count {dice_count}")

                else:
                    self.set_position(player_name, final)
                    self.maxi = max(self.maxi, final)
                    print(f"{player_name} started from {last_position} moved to {final}, dice count {dice_count}")

                if self.maxi == Constants.MAX_POINT:
                    return f"{player_name} is the winner while the rest data is {self.get_data()}"
