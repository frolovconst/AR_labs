from bitarray import bitarray
from math import log2, ceil
from random_generator import bernoulli, randint
from hashes import bitarray_hash, generate_hashes


class CuckooFilter:
    fingerprint_size = 0
    key_size = 0
    bucket_size = 0
    added = 0
    capacity = 0
    _hashes = None

    def __init__(self, expected_n_elements, desired_fpp, work_load=0.95, s_bucket=1, types='numerical'):
        """
        Initialize Cuckoo Filter
        :param expected_n_elements:
        :param desired_fpp:
        :param work_load: determines occupied space in filter
        :param s_bucket: number of cells in the bucket
        :param types: types supported by the filter. Possible values ['numerical','string']
        """
        self._hashes = generate_hashes(2, types)

        # Calculate the size of the fingerprint in bits
        s_fingerprint = ceil(log2(desired_fpp**-1) + log2(2*s_bucket))

        # Calculate the capacity of the filter, i.e. the total number of
        # elements that can fit.
        capacity = ceil(expected_n_elements / work_load)
        # Calculate the size of the filter in bits
        bit_size = capacity * s_fingerprint
        # Calculate the number of buckets
        n_buckets = int(capacity / s_bucket)

        self.key_size = n_buckets
        self.bucket_size = s_bucket
        self.fingerprint_size = s_fingerprint
        self.capacity = capacity

        self.container = bitarray(bit_size)
        self.container.setall(0)

    def add(self, item):
        """
        Adds an element or a list of elements in the filter. Do not check
        whether the list is longer than filter capacity.
        :param item: item or list of items to add
        :return: None
        """
        # make use of method add_item(...)
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
        # Make use of methods _fingerprint, _get_keys, _try_set, _relocate

        # %%% ADD YOUR CODE %%%
        
        
        fp = self._fingerprint(item)
        keys = self._get_keys(item, fp)

        if self._try_set(keys[0], fp) or self._try_set(keys[1], fp):
            pass
        else:
            self._relocate(keys, fp)
        
        # %%%%%%

        if self.added < self.capacity:
            self.added += 1

    def __contains__(self, item):
        """
        Perform a membership test
        :param item:
        :return: membership test result
        """

        # Hint: Make note of how method _try_set works
        # %%% ADD YOUR CODE %%%
        fp = self._fingerprint(item)
        keys = self._get_keys(item, fp)
        
        
        bpe = self.fingerprint_size
        # Convert key to bitarray index
        for key in keys:
            index = self._get_index(key)
            for b in range(self.bucket_size):
                pos_of_interest = index + b * bpe
                # if cell is empty, overwrite
                if self.container[pos_of_interest: pos_of_interest + bpe] == fp:
                    return True
        # %%%%%%
        return False

    # Service functions
    def _fingerprint(self, item):
        combinations = 2 ** self.fingerprint_size
        hashf = self._hashes[0]
        fp = hashf(item) % combinations
        # related to question 10: zero value prohibition.
        if int(fp) == 0:
            fp += 1
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        return self.to_bits(fp)


    def _hash(self, val):
        hashf = self._hashes[1]
        h = hashf(val)
        return h

    def to_bits(self, hash_value):
        temp = bitarray()
        temp.frombytes((hash_value).to_bytes(8, 'big'))
        return temp[-self.fingerprint_size:]

    def _get_index(self, key):
        return key * self.bucket_size * self.fingerprint_size

    def current_fpp(self):
        """
        Calculate the current probability of false positives based on
        the current number of added elements and the filter capacity
        :return: probability of false positives
        """
        # %%% ADD YOUR CODE %%%
        fp_size = self.fingerprint_size
        b = self.bucket_size
        l = self.added / self.capacity
        final_power = 2*b*l
        fpp = 1-(1-2**-fp_size)**final_power
        # %%%%%%
        return fpp

    def _get_keys(self, item, fingerprint):
        """
        Calculate bucket keys for input item
        :param item:
        :param fingerprint:
        :return: shuffled keys
        """
        key_size = self.key_size
        _hash = self._hash

#         i1 = _hash(item) % key_size - previous
        i1 = int(_hash(item) % key_size)
        i2 = (bitarray_hash(fingerprint) ^ i1) % key_size
        

        keys = [i1, i2] if bernoulli() else [i2, i1]
        return keys

    def _try_set(self, key, fingerprint):
        """
        Try write fingerprint to some cell in a bucket. Return False of
        the bucket is full
        :param key:
        :param fingerprint:
        :return: success status
        """
        bpe = self.fingerprint_size
        # Convert key to bitarray index
        index = self._get_index(key)
        for b in range(self.bucket_size):
            pos_of_interest = index + b * bpe
            # if cell is empty, overwrite
            if self.container[pos_of_interest: pos_of_interest + bpe].count() == 0:
                self.container[pos_of_interest: pos_of_interest + bpe] = fingerprint
                return True
        return False

    def _relocate(self, keys, fingerprint):
        """
        Rewrite the value of a random cell from a random bucket
        The overwritten element is lost
        :param keys:
        :param fingerprint:
        :return: None
        """
        bpe = self.fingerprint_size
        b_size = self.bucket_size

        key_ind = bernoulli()
        bucket_ind = randint(b_size)

        index = self._get_index(keys[key_ind])
        pos_of_interest = index + bucket_ind * bpe

        # for the sake of simplisity, the existing value is not reassigned

        self.container[pos_of_interest: pos_of_interest + bpe] = fingerprint
