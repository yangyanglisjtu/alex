import go
import draw
import tensorflow as tf
import numpy as np
def select_most_likely(chessmen, move_probabilities):
    mostpossibities = 0
    move=[]
    for key in chessmen:
        chesses =chessmen[key]
        for i in len(chesses):
            chess = chesses[i]
            w= tf.reshape(chess,[5,5,1,1])
            h_conv = tf.nn.conv2d(move_probabilities,w, strides=[1, 1, 1, 1], padding="SAME")
            possibilities = tf.reshape(h_conv, [-1, go.N ** 2])
            maxindex = np.argmax(possibilities)
            if(possibilities[maxindex] > mostpossibities):
                move = [maxindex//go.N,maxindex%go.N]
                selectchess = key
    if(len(move) != 0):
        chessmen.pop(selectchess,0)
    return chess,move
class GreedyPolicyPlayerMixin:
    def __init__(self, policy_network,chessmen):
        self.policy_network = policy_network
        self.chessmen = draw.x
        super().__init__()

    def suggest_move(self, position):
        move_probabilities = self.policy_network.run(position)
        return select_most_likely(self.chessmen,move_probabilities)



