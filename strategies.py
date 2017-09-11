
import go



def sorted_moves(probability_array):
    coords = [(a, b) for a in range(go.N) for b in range(go.N)]
    coords.sort(key=lambda c: probability_array[c], reverse=True)
    return coords



def select_most_likely(position, move_probabilities):
    for move in sorted_moves(move_probabilities):
        return move

class GreedyPolicyPlayerMixin:
    def __init__(self, policy_network):
        self.policy_network = policy_network
        super().__init__()

    def suggest_move(self, position):
        move_probabilities = self.policy_network.run(position)
        return select_most_likely(position, move_probabilities)



