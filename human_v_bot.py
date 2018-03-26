from dlgo import agent
from dlgo import goboard_slow
from dlgo import gotypes
from dlgo.utils import print_board, print_move, point_from_coords



def main():
    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    bot = agent.RandomBot(),

    while not game.is_over():
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = raw_input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard_slow.Move.play(point)
        else:
            move = bot.select_move(game)
            print_move(game.next_player, move)
            game = game.apply_move(game.next_player, move)


if __name__ == '__main__':
    main()
