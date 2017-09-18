'''
Features used by AlphaMao, in approximate order of importance.
Feature                 # Notes
Stone colour            5 Player player1; player2; player3;player4;empty
'''

import numpy as np
import go

def stone_color_feature(position):
    board = position.board
    features = np.zeros([go.N, go.N, 5], dtype=np.uint8)
    if position.to_play == go.BLACK:
        features[board == go.BLACK, 0] = 1
        features[board == go.WHITE, 1] = 1
    else:
        features[board == go.WHITE, 0] = 1
        features[board == go.BLACK, 1] = 1

    features[board == go.EMPTY, 2] = 1
    return features



DEFAULT_FEATURES = [
    stone_color_feature
]

def extract_features(position, features=DEFAULT_FEATURES):
    return np.concatenate([feature(position) for feature in features], axis=2)

def bulk_extract_features(positions, features=DEFAULT_FEATURES):
    num_positions = len(positions)
    num_planes = 3
    output = np.zeros([num_positions, go.N, go.N, num_planes], dtype=np.uint8)
    for i, pos in enumerate(positions):
        output[i] = extract_features(pos, features=features)
    return output
