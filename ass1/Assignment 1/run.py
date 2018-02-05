from numpy.random import seed
from experiments import check_results, check_fails, check_time_performance
from time import time

seed(1)

start = time()
check_results()
check_fails()
check_time_performance()
finish = time()

print("total time in minutes", int((finish - start) / 60))