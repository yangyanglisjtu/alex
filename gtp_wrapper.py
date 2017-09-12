
import go
import utils
from policy import PolicyNetwork
from strategies import GreedyPolicyPlayerMixin

def translate_gtp_colors(color):
    if color == BLACK:
        return go.BLACK
    elif color == WHITE:
        return go.WHITE
    else:
        return go.EMPTY

class BlokusInterface(object):
    def __init__(self):
        self.size = 9
        self.position = None
        self.clear()

    def set_size(self, n):
        self.size = n
        go.set_board_size(n)
        self.clear()

    def clear(self):
        self.position = go.Position()

    def accomodate_out_of_turn(self, color):
        if not translate_gtp_colors(color) == self.position.to_play:
            self.position.flip_playerturn(mutate=True)

    def make_move(self, color, vertex):
        coords = utils.parse_pygtp_coords(vertex)
        self.accomodate_out_of_turn(color)
        self.position = self.position.play_move(coords, color=translate_gtp_colors(color))
        return True

    def get_move(self, color):
        self.accomodate_out_of_turn(color)
        move = self.suggest_move(self.position)
        return utils.unparse_pygtp_coords(move)

#    def should_pass(self, position):
#        # Pass if the opponent passes
#        return position.n > 100 and position.recent and position.recent[-1].move == None

#    def get_score(self):
#        return self.position.result()

#    def suggest_move(self, position):
#        raise NotImplementedError

class GreedyPolicyPlayer(GreedyPolicyPlayerMixin): pass


def begin_game(read_file):
    n = PolicyNetwork(use_cpu=True)
    n.initialize_variables(read_file)
    GreedyPolicyPlayer(n)
    return

