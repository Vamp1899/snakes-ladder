from service import Board

if __name__ == "__main__":
    no_of_players = int(input("Enter the number of players "))
    player_list = []
    while no_of_players:
        name = input("Enter the player Name ")
        player_list.append(name)
        no_of_players -= 1

    board_obj = Board(no_of_players, player_list)

    answer = board_obj.start()
    print(answer)
