import DFA

def XOR():
    alphabet = {'0', '1'}
    states = {"E", "O"}
    finals = {"O"}
    start = "E"
    delta = {}
    
    delta[("E", "0")] = "E"
    delta[("E", "1")] = "O"
    delta[("O", "0")] = "O"
    delta[("O", "1")] = "E"
    
    return DFA.DFA(states, alphabet, delta, start, finals)


def AND():
    alphabet = {'0', '1'}
    states = {"start", "No0s", "Some0s"}
    finals = {"No0s"}
    start = "start"
    delta = {}
    
    delta[("start", "0")] = "Some0s"
    delta[("start", "1")] = "No0s"
    delta[("No0s", "0")] = "Some0s"
    delta[("No0s", "1")] = "No0s"
    delta[("Some0s", "0")] = "Some0s"
    delta[("Some0s", "1")] = "Some0s"
    
    return DFA.DFA(states, alphabet, delta, start, finals)

def oneEvenZeroOdd():
        '''TODO
        * Build a DFA which, when given a binary string, 
        * returns true if it either starts with a 1 and has
        * even length, or starts with a 0 and has odd length.
        * 
        * For example, it should return true for:
        * 10
        * 11
        * 100000
        * 0
        * 000
        * 010
        *
        * It should return false for:
        * the empty string
        * 1
        * 00
        * 01
        * 110
        '''
        alphabet = {'0', '1'}
        states = {}
        finals = {}
        start = ""
        delta = {}
        
        return DFA.DFA(states, alphabet, delta, start, finals)

def div8():
        '''TODO
        * Build a DFA which, when given a binary string
        * representing a natural number, determines whether
        * that number is divisible by 8.
        '''
        alphabet = {'0', '1'}
        states = {}
        finals = {}
        start = ""
        delta = {}
        
        return DFA.DFA(states, alphabet, delta, start, finals)
        
def hammingDistance(match_string, distance):
        ''' TODO
        * For bioinformatics and network transmission, it's helpful 
        * to be able to measure how different various strings are
        * from one another. These metrics are often called string
        * distance. There are various methods from measuring string
        * distance, and which to use mostly depends on what is an
        * allowable change. 
        * For this problem we're asking you to write a function to
        * accept all strings that are within a certain Hamming
        * distance of another string (the match parameter).
        * The Hamming distance between two strings is the smallest
        * number of single-character substitutions that must be 
        * made to convert one string into the other.
        *
        * For example, if we invoked this function on:
        * match = "nate"
        * distance = 2
        *
        * The automaton should return true for:
        * nate (distance 0, exact match)
        * gate (distance 1, substituting n->g)
        * note (distance 1, substituting a->o)
        * hath (distance 2, substituting n->h and e->h)
        * pale (distance 2, substituting n->p and t->l)
        *
        * The automaton should return false for:
        * math (3 substitutions required)
        * rich (4 substitutions required)
        * naters (cannot be converted by substitution alone)
        *
        * To keep your automata from looking too cluttered,
        * we restrict our alphabet to be DNA bases (a,t,g,c).
        '''
        alphabet = {'a', 't', 'g', 'c'}
        states = {}
        finals = {}
        start = ""
        delta = {}
        
        return DFA.DFA(states, alphabet, delta, start, finals)
    

def xor_example():
    xor = XOR() # make the xor automaton
    print(xor) # you can see the definition of this automaton
    xor.step('0') # the automaton will transition on a 0
    print(xor.active) # you'll see that the active state is still the start state
    xor.step('1') # the automaton will transition on a 1
    print(xor.active) # now the active state has changed
    xor.reset() # resets the automaton so you can run it on another input string
    print(xor.execute('1101011')) # run the automaton on the given input string, 
                                  # returns True/False for 1/0 (this should be True)


def and_example():
    and_dfa = AND()  # make the and automaton
    and_dfa.toDot()  # prints a dot description of the automaton
                     # paste the text produced here:  https://dreampuf.github.io/GraphvizOnline/

#xor_example()
and_example()
