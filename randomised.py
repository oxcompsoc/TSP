from random import shuffle
from tsptest import test

def randomised(distances, names, drunk_factor):
    shuffle(names)
    names.append(names[0])
    return names

test(randomised)
