import NFA    

def edit_distance_nfa(match_string, distance):
    """TODO:
    For bioinformatics and network transmission, it's helpful 
    to be able to measure how different various strings are
    from one another. These metrics are often called string
    distance. There are various methods from measuring string
    distance, and which to use mostly depends on what is an
    allowable change. 
    
    For this problem we're asking you to write a function to
    create a NFA to return 1 for all strings that are within 
    a certain edit distance (Levenshtein distance) of another 
    string (the match parameter).
    The Edit distance between two strings is the smallest
    number of single-character substitutions, insertions, or
    deletions that must be made to convert one string into the other.
    
    For example, if we invoked this function on:
    match = "nate"
    distance = 2
    
    The returned automaton should accept:
        nate (distance 0, exact match)
        nater (distance 1, inserting r)
        ate (distance 1, deleting n)
        note (distance 1, substituting a->o)
        ale (distance 2, deleting n and subsituting t->l)

    The automaton should reject:
        a (3 deletions required)
        nono (3 substitutions required)
        hatred (shortest distance is 3 from subtituting n->h, inserting r and d)
    
    To keep your automata from looking too cluttered,
    we restrict our alphabet to be DNA bases (a,t,g,c).
    """
    return NFA.NFA()
