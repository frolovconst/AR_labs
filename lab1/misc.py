from numpy import random,array,arange
import matplotlib.pyplot as plt

def generate_random(length, randomness):
    '''
    Generates an array of length [length] with the level of unsortedness
    specified by [randomness]
    '''
    if randomness > 1. or randomness < 0.:
        raise Exception("Level of randomness should be between 0. and 1.")

    # Generate sorted array
    seq = arange(length)

    # Introduce unsorted elements by random replacement
    replacement_size = int(length * randomness)
    positions = random.choice(seq, replacement_size, replace=True)
    seq[positions] = random.randint(low=0, high=length, size=replacement_size)
    return seq


def generate_figures(collection, xlabel, xrange):

    '''
    Plots the number of calls and execution time vs parameter specified by
    [xlabel] (String) and [xrange] (Array)
    '''

    calls_det,calls_rnd,time_det,time_rnd = collection

    plt.figure()
    plt.plot(xrange,calls_det,label="Deterministic")
    plt.plot(xrange,calls_rnd,label="Randomized")
    plt.ylabel("Number of calls"); plt.xlabel(xlabel); plt.grid(True)
    plt.legend()
    plt.savefig("fig Calls vs "+xlabel+".png")

    plt.figure()
    plt.plot(xrange,time_det,label="Deterministic")
    plt.plot(xrange,time_rnd,label="Randomized")
    plt.ylabel("Time, s"); plt.xlabel(xlabel); plt.grid(True)
    plt.legend()
    plt.savefig("fig Time vs "+xlabel+".png")



def init_gauges_collection():
    '''
    Initializes containers that are used for plotting
    '''
    calls_det = []
    calls_rnd = []
    time_det = []
    time_rnd = []

    return calls_det,calls_rnd,time_det,time_rnd



def append_gauges(collection,gauges):

    calls_det,calls_rnd,time_det,time_rnd = collection

    c_det,c_rnd,t_det,t_rnd = gauges

    calls_det.append(c_det)
    calls_rnd.append(c_rnd)
    time_det.append(t_det)
    time_rnd.append(t_rnd)

    return calls_det,calls_rnd,time_det,time_rnd
