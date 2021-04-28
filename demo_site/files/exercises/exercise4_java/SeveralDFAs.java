import java.util.*;

public class SeveralDFAs{

    public static DFA XOR(){
        /*
        * This is the automaton for the XOR language from class.
        */
        
        // I recommend that all implementations include these first 4 lines verbatim
        Set<Character> alphabet = new HashSet<Character>();
        Set<String> states = new HashSet<String>();
        Set<String> finals = new HashSet<String>();
        Map<Tuple, String> delta = new HashMap<Tuple, String>();
        
        
        // I recommend you include these 4 as well, adapted for each automaton
        Collections.addAll(alphabet, '0', '1');
        Collections.addAll(states, "E", "O");
        Collections.addAll(finals, "O");
        String start = "E";
        
        
        // Then you should add all transitions to delta
        delta.put(new Tuple("E",'1'), "O"); // when in state E, transition to state O on input 1
        delta.put(new Tuple("E",'0'), "E");
        delta.put(new Tuple("O",'1'), "E");
        delta.put(new Tuple("O",'0'), "O");
        
        // And finally you should make the DFA
        return new DFA(states, alphabet, delta, start, finals);
    }
    
    public static DFA AND(){
        /*
        * This is an implementation of infinite AND from class (it returns 0 on the empty string)
        */
        
        Set<Character> alphabet = new HashSet<Character>();
        Set<String> states = new HashSet<String>();
        Set<String> finals = new HashSet<String>();
        Map<Tuple, String> delta = new HashMap<Tuple, String>();
        
        Collections.addAll(alphabet, '0', '1');
        Collections.addAll(states, "start", "No0s", "Some0s");
        Collections.addAll(finals, "No0s");
        String start = "start";
        
        delta.put(new Tuple("start", '0'), "Some0s");
        delta.put(new Tuple("start", '1'), "No0s");
        delta.put(new Tuple("Some0s", '0'), "Some0s");
        delta.put(new Tuple("Some0s", '1'), "Some0s");
        delta.put(new Tuple("No0s", '0'), "Some0s");
        delta.put(new Tuple("No0s", '1'), "No0s");
        
        return new DFA(states, alphabet, delta, start, finals);
    }
    
    public static DFA oneEvenZeroOdd(){
        /*TODO
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
        *
        * I've given you some code to start with, feel free
        * to change it if you'd prefer to do something else.
        */
    
        Set<Character> alphabet = new HashSet<Character>();
        Set<String> states = new HashSet<String>();
        Set<String> finals = new HashSet<String>();
        Map<Tuple, String> delta = new HashMap<Tuple, String>();
        
        Collections.addAll(alphabet, '0', '1');
        
        return new DFA();
    }
    
    public static DFA div8(){
        /*TODO
        * Build a DFA which, when given a binary string
        * representing a natural number, determines whether
        * that number is divisible by 8.
        *
        * I've given you some code to start with, feel free
        * to change it if you'd prefer to do something else.
        */
        Set<Character> alphabet = new HashSet<Character>();
        Set<String> states = new HashSet<String>();
        Set<String> finals = new HashSet<String>();
        Map<Tuple, String> delta = new HashMap<Tuple, String>();
        
        Collections.addAll(alphabet, '0', '1');
        
        return new DFA();
    }

    
    
    public static DFA hammingDistance(String match, int distance){
        /* TODO
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
        */
        Set<Character> alphabet = new HashSet<Character>();
        Set<String> states = new HashSet<String>();
        Set<String> finals = new HashSet<String>();
        Map<Tuple, String> delta = new HashMap<Tuple, String>();
        
        Collections.addAll(alphabet, 'a', 't', 'g', 'c');
        
        return new DFA();
    }
    
    public static void main(String[] args){
        /*DFA xor = XOR();  // make the xor automaton
        System.out.println(xor);  //  you can see the definition of this automaton
        xor.step('0');  // the automaton will transition on a 0
        System.out.println(xor.active);  // you'll see that the active state is still the start state
        xor.step('1');  // the automaton will transition on a 1
        System.out.println(xor.active);  // now the active state has changed
        xor.reset();  // resets the automaton so you can run it on another input string
        System.out.println(xor.execute("1101011"));  // run the automaton on the given input string, 
                                                    // returns true/false for 1/0 (this should be true)
        */
        
        DFA and = AND();  // make the and automaton
        and.toDot();  // prints a dot description of the automaton
                        // paste the text produced here:  https://dreampuf.github.io/GraphvizOnline/

    }
}
