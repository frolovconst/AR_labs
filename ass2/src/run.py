from bloomfilter import BloomFilter
from cuckoofilter import CuckooFilter
from numpy.random import randint
from numpy import array, random
import matplotlib.pyplot as plt
from numpy import geomspace

random.seed(1)

# Set up parameters
expected = 30
d_FPP = .01
trials = 100
elements_to_add = int(expected * 1.3)
added_elements = set()

# Sanity check
bf = BloomFilter(expected_n_elements=10, desired_fpp=.05)
assert 1 not in bf
bf.add(1)
assert bf.n_hashes == 5
assert bf.capacity == 11
assert 1 in bf

cf = CuckooFilter(expected_n_elements=10, desired_fpp=.05)
assert 1 not in cf
cf.add(1)
assert cf.key_size == 11
assert cf.fingerprint_size == 6
assert 1 in cf


# Prepare storage for FPP
fpp_bloom_emp = []
fpp_bloom_theor = []
fpp_cuckoo_emp = []
fpp_cuckoo_theor = []


bf = BloomFilter(expected_n_elements=expected, desired_fpp=d_FPP)


# Begin test
for added_size in range(elements_to_add):
    FP_bf = 0  # FPP of Bloom filter
    FP_cf = 0  # FPP of Cuckoo filter
    for t in range(trials):
        bf = BloomFilter(expected_n_elements=expected,
                         desired_fpp=d_FPP)

        cf = CuckooFilter(expected_n_elements=expected,
                          desired_fpp=d_FPP)

        test_set_size = int(1/d_FPP)*10
        test_set_range = test_set_size * 10000
        to_add = randint(test_set_range, size=added_size).tolist()

        bf.add(to_add)
        cf.add(to_add)
        added_elements = set(to_add)  # keep track of all added elements

        test_set = randint(test_set_range, size=test_set_size)
        for test_element in test_set:
            present = test_element in added_elements
            if test_element in bf and not present:
                FP_bf += 1
            if test_element in cf and not present:
                FP_cf += 1

    FPP_bf = FP_bf / (trials * test_set_size)
    FPP_cf = FP_cf / (trials * test_set_size)

    fpp_bloom_emp.append(FPP_bf)
    fpp_bloom_theor.append(bf.current_fpp())
    fpp_cuckoo_emp.append(FPP_cf)
    fpp_cuckoo_theor.append(cf.current_fpp())

    print("\rIterations %d/%d complete" % (added_size + 1, elements_to_add), end="")

print("")
legend = ['Bloom', 'Bloom Theor.', 'Cuckoo', 'Cuckoo Theor.']

to_plot = array([fpp_bloom_emp, fpp_bloom_theor, fpp_cuckoo_emp, fpp_cuckoo_theor]).T

plt.plot(to_plot)
plt.legend(legend)
plt.grid(True)
plt.title("FPP: %.3f, Expected elem.: %d, Work load: %.2f" % (d_FPP, expected, .95))
plt.savefig("fpp.eps")


plt.figure(figsize=[15,10])
cf_sizes = []
bf_sizes = []
for fpp in geomspace(1e-5, 1, 6):
    cf = CuckooFilter(expected_n_elements=10, desired_fpp=fpp)
    size = cf.capacity * cf.fingerprint_size
    cf_sizes += [size,]
    
    bf = BloomFilter(expected_n_elements=10, desired_fpp=fpp)
    size = bf.N 
    bf_sizes += [size,]
plt.semilogx(geomspace(1e-5, 1, 6), cf_sizes, label='Cuckoo')
plt.semilogx(geomspace(1e-5, 1, 6), bf_sizes, label='Bloom')
plt.grid()
plt.xlabel('log(FPP)')
plt.ylabel('space')
plt.legend()
plt.show()
