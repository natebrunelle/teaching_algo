import regex
import NFA
    
def nfa_example():
    """
    This function gives you and example of
    how to build an nfa. I built an nfa
    for determining whether a given binary
    string represents a natural number that
    is divisible by 8."""
    # I recommend that, to build an nfa, you:
    # 1) make the alphabet
    # 2) make the state set
    # 3) make the start state
    # 4) make the final state set
    # 5) make an empty transition function
    # 6) make the nfa
    # 7) add the desired transitions
    alphabet = {'0', '1'}
    states = {'start', 'one', 'zero1', 'zero2', 'zero3'}
    start = 'start'
    finals = {'zero3'}
    delta = {}
    the_nfa = NFA.NFA(states, alphabet, delta, start, finals)
    the_nfa.add_transition('start', '0', 'start')
    the_nfa.add_transition('start', '1', 'start')
    the_nfa.add_transition('start', '1', 'one')
    the_nfa.add_transition('one', '0', 'zero1')
    the_nfa.add_transition('zero1', '0', 'zero2')
    the_nfa.add_transition('zero2', '0', 'zero3')
    the_nfa.toDot()
    matches = "110010101000"
    doesnt_match = "111111111100"
    this_is_true = the_nfa.execute(matches)
    this_is_false = the_nfa.execute(doesnt_match)
    
    
def regex_example():
    """ This demonstrates how you can use the system provided
    for regex matching"""
    the_regex = "(a|b|c)*d"
    equivalent_nfa = regex.regex_to_NFA(the_regex)
    matches = "aaabcacaccaaacccbd"
    doesnt_match = "daacacc"
    this_is_true = equivalent_nfa.execute(matches)
    this_is_false = equivalent_nfa.execute(doesnt_match)
    print(this_is_true)
    print(this_is_false)
    regex.regex_to_NFA("(a|b|c)").toDot()
regex_example()

def trivial():
    """TODO: 
    Create an NFA which, for the alphabet {0,1}, 
    returns 1 on the empty string (and 0 on all 
    other strings).
    Your nfa should contain no more than
    1 state"""
    alphabet = {'0','1'}
    return NFA.NFA()

def substring0101():
    """TODO: 
    Create an NFA which returns 1 on
    all strings from the alphabet {0,1}
    that contain 0101 as a substring
    (and 0 on all other strings).
    Your nfa should contain no more than
    5 states"""
    alphabet = {'0','1'}
    return NFA.NFA()

def zerostar_onestar_zerostar():
    """TODO: 
    Create an NFA which returns 1 on
    all strings from the alphabet {0,1}
    that match the regular expression
    0*1*0*
    (and 0 on all other strings).
    Your nfa should contain no more than
    3 states"""
    alphabet = {'0','1'}
    return NFA.NFA()


def huntingtons(dna_sequence):
    """TODO: see task description for details """
    return "at risk"
    
