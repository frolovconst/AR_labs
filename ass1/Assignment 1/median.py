from numpy import sort
from numpy.random import choice

def median_r(data):
    n = data.size
    sub_n = int(n**.75)+1
    subset = choice(data, sub_n)
    subset.sort()
    index_d = max(0,int(.5*n**.75-n**.5)-1)
    d = subset[index_d]
    index_u = min(int(.5*n**.75+n**.5)-1,int(n**.75))
    u = subset[index_u]
    
    C = data[(data>=d) & (data<=u)] #.copy()
    
    
    ld = data[data<d].size
    lu = data[data>u].size
    
    if ld>n/2 or lu>n/2:
        return None
    Csize = C.size
    if Csize <= 4*n**.75:
        C.sort()
        
    else:
        return None
    mdn_idx = min(int(n/2 - ld), Csize-1)
    return C[mdn_idx]


def median_s(data):
    sorted = sort(data)
    return sorted[len(data) // 2]

