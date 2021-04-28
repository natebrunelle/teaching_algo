import NFA
import copy


def merge(nfa1, nfa2, suffix1 = "_1", suffix2 = "_2"):
    """
    creates a new nfa from two source nfas. This new nfa has all the states
    and transitions from the original 2 nfas (with distinct suffixes added
    to each state label to guarantee unique names). The start state is set
    as the start state from the first nfa given. The nfa has no final
    states.
    """
    states = set()
    finals = set()
    for state in nfa1.states:
        states.add(state + suffix1)
    for state in nfa1.finals:
        states.add(state + suffix1)
    for state in nfa2.states:
        states.add(state + suffix2)
    for state in nfa2.finals:
        states.add(state + suffix2)
    alphabet = nfa1.alphabet | nfa2.alphabet
    delta = {}
    for match, destinations in nfa1.delta.items():
        state, char = match
        match = (state + suffix1, char)
        delta[match] = set()
        for dest in destinations:
            delta[match].add(dest + suffix1)
    for match, destinations in nfa2.delta.items():
        state, char = match
        match = (state + suffix2, char)
        delta[match] = set()
        for dest in destinations:
            delta[match].add(dest + suffix2)
    start = nfa1.start + suffix1
    return NFA.NFA(states, alphabet, delta, start, finals)
        

def union(nfa1, nfa2, suffix1="_1", suffix2="_2"):
    merged = merge(nfa1, nfa2, suffix1, suffix2)
    merged.start = "new"
    merged.delta[("new", NFA.epsilon)] = {nfa1.start + suffix1, nfa2.start + suffix2}
    for state in nfa1.finals:
        merged.finals.add(state + suffix1)
    for state in nfa2.finals:
        merged.finals.add(state + suffix2)
    return merged

def concat(nfa1, nfa2,  suffix1="_1", suffix2="_2"):
    merged = merge(nfa1, nfa2, suffix1, suffix2)
    merged.start = nfa1.start + suffix1
    for state in nfa1.finals: 
        state += suffix1
        merged.add_transition(state, NFA.epsilon, nfa2.start + suffix2)
    for state in nfa2.finals:
        merged.finals.add(state + suffix2)
    return merged
    
def copy_nfa(nfa1):
    states = set(nfa1.states)
    alphabet = set(nfa1.alphabet)
    delta = copy.deepcopy(nfa1.delta)
    start = nfa1.start
    finals = set(nfa1.finals)
    return NFA.NFA(states, alphabet, delta, start, finals)

def kleene(nfa1):
    copy = copy_nfa(nfa1)
    eps_state = 'eps_state'
    for final in nfa1.finals:
        copy.add_transition(final, NFA.epsilon, copy.start)
    copy.states.add(eps_state)
    copy.add_transition(copy.start, NFA.epsilon, eps_state)
    copy.finals.add(eps_state)
    return copy



