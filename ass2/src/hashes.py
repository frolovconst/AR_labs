from struct import pack


def generate_hashes(n, types='numerical'):
    """
    Generate n hash functions for specified type
    :param n: number of hash functions to generate
    :param types: type of the input data for hash functions. Possible values ['numerical','string']
    :return: list of hash functions
    """
    if types == 'numerical':
        item_repr = lambda x: pack("f", x)
    elif types == "string":
        item_repr = lambda x: pack("s", x)
    else:
        raise TypeError("Types: ", types, " not supported")

    hashes = []
    for i in range(1, n+1):
        seed_hashf = lambda seed: lambda item: hash(item_repr(item) + (seed).to_bytes(1, "big"))
        hashf = seed_hashf(i)
        hashes.append(hashf)

    return hashes


def bitarray_hash(ba):
    return hash(ba.tobytes())
