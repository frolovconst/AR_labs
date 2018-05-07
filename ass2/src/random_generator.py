from numpy import random
import numpy as np

# Implements buffered random variables

buffer_size = 1000

binomial_buffer = np.zeros(buffer_size)
binomial_buffer_position = buffer_size

int_buffer = np.zeros(buffer_size)
int_buffer_position = buffer_size
int_buffer_range = 1


def bernoulli():
    """
    Draws single value of Bernoulli random variable from buffer
    :return: 0 or 1
    """
    global binomial_buffer, binomial_buffer_position

    if binomial_buffer_position == buffer_size:
        binomial_buffer = random.randint(2, size=buffer_size)
        binomial_buffer_position = 0

    val = binomial_buffer[binomial_buffer_position]
    binomial_buffer_position += 1

    return val


def randint(int_range):
    """
    Draws single value of a uniform discrete random variable
    defined on range [0,range] from buffer
    :param int_range: maximum value of uniform random variable
    :return: number from range [0, range]
    """
    global int_buffer, int_buffer_position, int_buffer_range

    if int_buffer_position == buffer_size or int_buffer_range != int_range:
        int_buffer = random.randint(int_range, size=buffer_size)
        int_buffer_position = 0

    val = int_buffer[int_buffer_position]
    int_buffer_position += 1

    return val
