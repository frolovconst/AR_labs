from bitarray import bitarray
from math import ceil, log, log2, e
from hashes import generate_hashes


class BloomFilter:
    container = None
    n_hashes = 1
    added = 0
    capacity = 0
    types = None
    hash_transforms = []
    N = 0

    def __init__(self, expected_n_elements, desired_fpp, work_load=.95, types='numerical'):
        """
        Initializes Bloom Filter
        :param expected_n_elements:
        :param desired_fpp:
        :param work_load: determines occupied space in filter
        :param types: types supported by the filter. Possible values ['numerical','string']
        """

        # Calculate the capacity of the filter, i.e. the total number of
        # elements that can fit.
#         capacity = ceil((log2(e) * log2(desired_fpp**-1)) * expected_n_elements / work_load)
        capacity = ceil(expected_n_elements / work_load)
#         print('cap=', capacity)

        # Calculate the number of bits required to store one element
        bpe = ceil(log2(e) * log2(desired_fpp**-1))
        s_complexity = bpe
#         self.aux_bpe = ((log2(e) * log2(desired_fpp**-1)) * expected_n_elements / work_load)/(log2(e) * log2(desired_fpp**-1))

        # Calculate the number of hashes that minimizes FPP for given
        # number of bits per entry
        self.N = ceil((log2(e) * log2(desired_fpp**-1)) * expected_n_elements / work_load)
        n_hashes = ceil(log(2) * self.N / expected_n_elements)
#         print('n_hashes =', n_hashes)

        self.n_hashes = n_hashes
        self.capacity = capacity
        self.hash_transforms = generate_hashes(n_hashes, types)

#         self.container = bitarray(s_complexity) - originally
        self.container = bitarray(self.N)
        self.container.setall(0)

    def add(self, item):
        """
        Adds an element or a list of elements in the filter. Do not check
        whether the list is longer than filter capacity.
        :param item: item or list of items to add
        :return: None
        """
        # create behavior similar to set()
        if isinstance(item, list):
            for i in item:
                self.add_item(i)
        else:
            self.add_item(item)

    def add_item(self, item):
        """
        Adding an item to the filter
        :param item:
        :return: None
        """
        # use the set of hash transforms self.hash_transforms
        # to calculate item hashes.
        # Obtain the keys from range [0, filter size]
        # using operator '%'

        # %%% ADD YOUR CODE %%%
        for h_func in self.hash_transforms:
            self.container[h_func(item) % self.N] = '1'
#             print(h_func(item) % self.capacity)
#         print(self.container)
        # %%%%%%

        if self.added < self.capacity:
            self.added += 1

    def __contains__(self, item):
        """
        Perform a membership test
        :param item:
        :return: membership test result
        """
        # use the set of hash transforms self.hash_transforms
        # to calculate item hashes.
        # Obtain the keys from range [0, filter size]
        # using operator '%'

        # %%% ADD YOUR CODE %%%
        res = True
#         print(self.container)
        for h_func in self.hash_transforms:
            if self.container[h_func(item) % self.N] == 0:
                res = False
                break
        # %%%%%%

        return res

    def current_fpp(self):
        """
        Calculate the current probability of false positives based on
        the number of currently added elements and the filter capacity
        :return: probability of false positives
        """

        # %%% ADD YOUR CODE %%%
        FPP = (1-(1-self.N**-1)**(self.added*self.n_hashes))**self.n_hashes
        # %%%%%%

        return FPP
