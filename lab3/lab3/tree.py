from numpy.random import binomial
from math import ceil,floor


class node:
    children = None # list of references to child nodes
    parent = None # reference to the parent node
    is_leaf = False
    value = 0

    def __init__(self):
        value = 0
        self.children = []

class leaf(node):
    def __init__(self,value):
        self.value = value
        self.is_leaf = True


def generate_terminal_level(number_of_leaves, prob):
    values = binomial(1,p=prob,size=number_of_leaves)
    leafs = list(map(leaf,values))
    return leafs

def generate_level(prev_level, fanout):
    prev_level_size = len(prev_level)
    new_level_size = ceil(len(prev_level)/fanout)
    new_level = [node() for i in range(new_level_size)]

    for n_id in range(prev_level_size):
        p_id = floor(n_id / fanout)
        new_level[p_id].children.append(prev_level[n_id])

    return new_level


def generate_tree(terminal_size, fanout = 2, p = 0.5):
    levels = [generate_terminal_level(terminal_size, p)]
    while(len(levels[-1])>1):
        levels.append(generate_level(levels[-1], fanout))

    return levels[-1][0]
