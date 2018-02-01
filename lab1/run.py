from numpy import random,arange
from time import time

from quicksort import do_quicksort, do_r_quicksort
from misc import generate_random, generate_figures, init_gauges_collection, append_gauges


def measure_qs(data, sorting_function):
    '''
    Measure the execution time of sorting function [sorting_function]
    and return the number of calls for partition sorting
    '''
    t_start = time()
    calls = sorting_function(data)
    t_end = time()
    e_time = t_end - t_start
    return e_time,calls

def gauge_functions(data_size, unsortedness, repeats = 100):
    '''
    You need to measure the average execution time of a sorting function.
    The function measure_qs performs the evaluation of run time performance.
    Usage: measure_qs( data_to_sort, sorting_function)
              sorting_function: do_quicksort or do_r_quicksort
           returns: execution_time, number_of_sorting_function_calls
    '''

    # Gauges for deterministic algorithm
    det_e_time_avg=0.; det_calls_avg=0.;
    # Gauges for randomized algorithm
    rnd_e_time_avg=0.; rnd_calls_avg=0.

    for i in range(repeats):
        # For fair comparison you should feed the same data to different
        # sorting algorithms
        data = generate_random(data_size,unsortedness)

        # %%% START YOUR CODE HERE %%%

    # %%% END YOUR CODE HERE %%%
    return det_calls_avg, rnd_calls_avg, det_e_time_avg, rnd_e_time_avg


# Fix the seed to obtain comparable results
random.seed(0)
init_state = random.get_state()


##########
# Test the correctness of the quicksort algorithm
test_data = random.randint(0,10,size=10)

print("\nOriginal",test_data)

data_1 = test_data.copy()
do_quicksort(data_1)
print("Deterministic sort",data_1)

data_2 = test_data.copy()
do_r_quicksort(data_2)
print("Randomized sort",data_2,"\n")

random.set_state(init_state)



##########
# On the first stage evaluate the impact of the dataset size on the sorting
# performance
gauges_collection = init_gauges_collection()

# Array of possible dataset sizes
data_size_rng = arange(100, 1000, 100)
x_points = len(data_size_rng)

# Fixed level of data unsortedness
unsortedness = 0.3

for ind,data_size in enumerate(data_size_rng):
    gauges = gauge_functions(data_size, unsortedness)
    append_gauges(gauges_collection, gauges)
    print("\rTesting against dataset size %d/%d" % (ind+1, x_points), end="")

generate_figures(gauges_collection, xlabel = "Input Size",xrange = data_size_rng)
##########


print("")


##########
# Evaluate the impact of the unsortedness level on the sorting performance
gauges_collection = init_gauges_collection()

# Array of possible unsortedness levels
unsortedness_level = arange(.1, 1.1, .1)
x_points = len(unsortedness_level)

# Fixed level of dataset size
data_size = 1000

for ind,unsortedness in enumerate(unsortedness_level):
    gauges = gauge_functions(data_size, unsortedness)
    append_gauges(gauges_collection, gauges)
    print("\rTesting against unsortedness level %d/%d" % (ind+1, x_points), end="")

generate_figures(gauges_collection, xlabel = "Unsortedness", xrange = unsortedness_level)
##########


print("\nFinished\n")
