"""
Miscellaneous helper functions
"""

def argmax(l):
    """
    l: list of integers
    Return list of indices equal to max
    """
    m = max(l)
    maxes = []
    for i in range(len(l)):
        if l[i] == m:
            maxes.append(i)
    return maxes

def count_instances(l, obj):
    """
    Count the number of instances of obj in l
    """
    c = 0
    for x in l:
        if x == obj:
            c += 1
    return c

def get_indices(l, obj):
    """
    Get the indices of obj in l
    """
    return [i for i in range(len(l)) if l[i] == obj]

def number_dict(l):
    """
    For hands, get how many of each number
    """
    d = {}
    for obj in l:
        val, suit = obj
        if val not in d:
            d[val] = 0
        d[val] += 1
    return d

def suit_dict(l):
    """
    For hands, get how many of each suit
    """
    d = {}
    for obj in l:
        val, suit = obj
        if suit not in d:
            d[suit] = 0
        d[suit] += 1
    return d

def any_tuples(l):
    """
    Determine if there are any tuples in a list.
    """
    for obj in l:
        if isinstance(obj, tuple):
            return True
    return False

def all_x(l, x):
    """
    Determine whether an iterable contains only the value x
    """
    for obj in l:
        if obj != x:
            return False
    return True

def highest_unpaired(number_dict):
    mx = -1
    for k in number_dict.keys():
        if number_dict[k] == 1 and k > mx:
            mx = k
    return mx