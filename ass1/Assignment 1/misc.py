from time import time
import matplotlib.pyplot as plt


def generate_figures(collection, xlabel, xrange):
    """
    Plots execution time vs parameter specified by
    [xlabel] (String) and [xrange] (Array)
    """
    sorting_avg, np_avg, randomized_avg = collection
    print("sorting average time", sorting_avg)
    print("numpy average time", np_avg)
    print("randomized average time", randomized_avg)
    plt.figure()
    plt.plot(xrange, sorting_avg, label="Sorting")
    plt.plot(xrange, np_avg, label="Numpy")
    plt.plot(xrange, randomized_avg, label="Randomized")
    plt.ylabel("Time, s")
    plt.xlabel(xlabel)
    plt.grid(True)
    plt.legend()
    plt.savefig("fig Time vs "+xlabel+".png")


def append_gauges(collection, gauges):
    for i in range(len(collection)):
        collection[i].append(gauges[i])
    return collection


def measure_time(data, algorithm):
    t_start = time()
    algorithm(data)
    t_end = time()
    e_time = (t_end - t_start)
    return e_time
