import NFA

def main():
    states = {'start', 'final'}
    alphabet = {'0', '1'}
    delta = {}
    delta[('start', '0')] = {'final'}
    delta[('start', NFA.epsilon)] = {'final'}
    start = 'start'
    finals = {'final'}
    n1 = NFA.NFA(states, alphabet, delta, start, finals)
    n2 = NFA.NFA(states, alphabet, delta, start, finals)
    n3 = NFA.kleene(n1)
    n3.toDot()
    
main()

