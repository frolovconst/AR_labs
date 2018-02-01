from numpy.random import randint,choice,seed
from math import ceil,floor
from numpy import mean,var,std,arange,array,concatenate
from tree import generate_tree
import matplotlib.pyplot as plt

leaf_counter = 0

# The gametree is generated in the following fashion:
# 1. A number of leaves is calculated for the case fanout=2, depth=2*k
# 2. Then, balanced binary tree is generated using the function 'generate_tree'
# The parameters are:
#     terminal_size = d**(2*k)
#     fanout = 2
#     p - the parameter of binomial distribution that determines the distribution
#     0 and 1 in the last level of the tree
#
# You need to implement a function 'evaluate' that has the following properties:
# 1. The input to the function is the current tree node
# and the strategy ("min" or "max")
# 2. The function should perform in a recursive fashion, i.e. evaluation of the
# current node is performed by evaluating child nodes
# 3. The order of evaluating child nodes is random
# 4. The strategy flips upon every recursive call, i.e. the even levels of tree
# are evaluated with "max" strategy, and odd levels are evaluated with "min"
# strategy
# 5. The recursion terminates when leaf node is reached, and the value of the
# node returned (node.value)
#
# Write a function 'evaluate_tree_instance' that accepts a root tree as the
# input, and measures the number of leaves visited during the tree evaluation.
# Hint: use global variable and modify its value when leaf node is reached in
# 'evaluate' procedure
#
# Perform following experiments:
# 1. Vary the value of k = 2:7 and measure the number of evaluated leaves
# 2. Vary the value of p = .1:.9 and measure the number of evaluated leaves
# 3. Perform the comparison randomized and deterministic versions of the
# algorithm

def evaluate(...):


def evaluate_tree_instance(...):


d = 2 # Fanout

for p in arange(...):
    for k in range(2,8): # number of turns in the game tree
        number_of_leaves = d**(2*k)
