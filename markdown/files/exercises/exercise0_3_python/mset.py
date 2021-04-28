
'''We're going to start with an empty set, then procede to add things into that.'''

def mset_empty():
    """Returns a new empty set."""
    return []


'''We need two built-in operations to define a set: membership test (contains) and insert:'''

def mset_contains(t, x):
    """Returns a Boolean indicating if x is in the set t."""
    return x in t

def mset_insert(s, x):
    """Returns a new set that contains all of the elements of s as well as the new element x."""
    return s + [x]
    
'''Here's an example usage of our mset data structure. Print this and play with contains to see what it looks like and how it behaves (remove all print statements before submitting)'''
s = mset_insert(mset_insert(mset_insert(mset_empty(), 1), 2), 3)


int_in_s = "TODO: assign a value to this variable such mset_contains(s, int_in_s) evaluates to True"
assert(mset_contains(s, int_in_s))
print("Good job!")


int_not_in_s = "TODO: assign an int value to this variable such mset_contains(s, int_not_in_s) evaluates to False"
assert(type(int_not_in_s) is int)
assert(not mset_contains(s, int_not_in_s))
print('Keep it up!')



def mset_subset(s, t):
    """Returns Boolean indicating if set s is a subset of set t. (see TCS definition 1.4.1)"""
    for x in s:
        if not mset_contains(t, x):
            return False
    return True
    

empty_subset_empty = "TODO: Is the empty set a subset of the empty set? If so, set this variable's value to True, otherwise make it False."

assert(mset_subset(mset_empty(), mset_empty()) == empty_subset_empty)
print('One more, you can do it!')

'''TODO: Next implement this function that returns True if the mset s is equivalent to the mset t, and returns False otherwise. The body of this function must be only a single line.'''
def mset_equal(s, t):
    """Returns a Boolean indicating if set s is equal to set t."""
    pass # TODO: replace this line of code with your single-line implementation
    
assert(mset_equal(mset_empty(), mset_empty()))
s1 = mset_insert(mset_empty(), 1)
s2 = mset_insert(s1, 2)
s3 = mset_insert(s2, 3)
assert(mset_equal(s3, s3))
assert(not mset_equal(s2, s3))
assert(not mset_equal(s3, mset_insert(s2, 'dog')))
print("HOORAY!!!! You did it! YIPEEEE")






