from numpy.random import random, randint
from numpy import median
from median import median_r, median_s
from time import time

from misc import append_gauges, generate_figures, measure_time


def check_results():
    sorting_vs_random = []
    numpy_vs_random = []
    sizes = randint(500000, size=10)*2-1

    for size in sizes:
        sorting_vs_random_on_size = 0
        numpy_vs_random_on_size = 0
        for i in range(100):
            data = random(size)
            rnd_res = median_r(data)
            sort_res = median_s(data)
            nmp_med = median(data)
            if rnd_res == None:
                sorting_vs_random_on_size += 1
                numpy_vs_random_on_size += 1
            else:
                sorting_vs_random_on_size += (rnd_res!=sort_res)
                numpy_vs_random_on_size += (rnd_res!=nmp_med)
        sorting_vs_random.append(sorting_vs_random_on_size)
        numpy_vs_random.append(numpy_vs_random_on_size)
    print("sorting vs random different results", sorting_vs_random)
    print("numpy vs random different results", numpy_vs_random)


def check_fails():
    """
    This function checks how often randomized algorithm fails
    """
    fails_number = []
    sizes = []
    for zeros in range(1,9):
        size = 10**zeros
        sizes.append(size)
    for size in sizes:
        fails_on_size = 0
        for i in range(100):
            data = random(size)
            # %%% START YOUR CODE HERE %%%
            rnd_res = median_r(data)
            if rnd_res == None:
                fails_on_size += 1
            # %%% END YOUR CODE HERE %%%
        fails_number.append(fails_on_size)
    print("numbers of fails", fails_number)


def gauge_algorithms(data_size, repeats=100):
    sorting_avg = 0.
    np_avg = 0.
    randomized_avg = 0.
    count = 0
    for i in range(repeats):
        data = random(data_size)
        
        dur = time()
        reslt = median_r(data)
        randomized_avg += (reslt!=None)*(time()-dur)
        count += reslt!=None
        
        dur = time()
        reslt = median(data)
        np_avg += time()-dur
        
        dur = time()
        reslt = median_s(data)
        sorting_avg += time()-dur
        
    return sorting_avg/repeats, np_avg/repeats, randomized_avg/count


def check_time_performance():
    sizes = []
    for zeros in range(1,8):
        size = 10**zeros
        sizes.append(size)

    gauges_collection = ([], [], [])
    for size in sizes:
        gauge = gauge_algorithms(size)
        append_gauges(gauges_collection, gauge)
    generate_figures(gauges_collection, "size", sizes)
