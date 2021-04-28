
class DFA:
    
    def __init__(self, states=set(), alphabet=set(), delta={}, start="", finals=set()):
        self.states = states
        self.alphabet = alphabet
        self.delta = delta
        self.start = start
        self.finals = finals
        self.delta_domain = [(state, char) for state in states for char in alphabet]
        self.chars_seen = ""
        self.active = start
    
    def step(self, c):
        self.active = self.delta[(self.active, c)]
        self.chars_seen += c
        return self.active in self.finals
    
    def reset(self):
        self.active = self.start
        self.chars_seen = ""
        return self.start in self.finals
    
    def execute(self, input_string):
        result = self.active in self.finals
        for c in input_string:
            result = self.step(c)
        return result
    
    def __str__(self):
        display = "Start state: " + self.start + "\n";
        display += "Current state: " + self.active + "\n";
        display += "delta function: \n";
        for tup in self.delta.keys():
            display += "\t" + str(tup) + " -> " + self.delta[tup] + "\n";
        display += "Final states: \n";
        for state in self.finals:
            display += "\t" + state + "\n";
        return display
    
    def toDot(self):
        '''
        * Prints out a description of the automaton in dot,
        * which is a graph specification language.
        * I recommend going to this url to convert it into
        * an image: https://dreampuf.github.io/GraphvizOnline/
        '''
        print("digraph G {")
        
        start_shape = ""
        if self.start in self.finals:
            start_shape = "doubleoctagon"
        else:
            start_shape = "octagon"
        print("node [shape = " + start_shape + "]; " + self.start + ";")
        
        double_circled = "node [shape = doublecircle];"
        additional_finals = False
        for s in self.finals:
            if (s == self.start):
                continue
            double_circled += " " + s
            additional_finals = True

        if additional_finals:
            print(double_circled + ";")
        
        single_circled = "node [shape = circle];"
        additional_states = False
        for s in self.states:
            if (s == self.start) or (s in self.finals):
                continue
            single_circled += " " + s
            additional_states = True
            
        if additional_states:
            print(single_circled)
        
        for tup in self.delta.keys():
            transition = ""
            transition += tup[0] + " -> " + self.delta[tup] + " [ label = \"" + tup[1] + "\" ];"
            print(transition)
        
        print("}")
        
    
    
