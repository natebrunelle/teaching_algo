import java.util.*;


public class Exercise5{
    public static void nfa_example(){
        /*This function gives you and example of
        how to build an nfa. I built an nfa
        for determining whether a given binary
        string represents a natural number that
        is divisible by 8.*/
        // I recommend that, to build an nfa, you:
        // 1) make the alphabet
        // 2) make the state set
        // 3) make the start state
        // 4) make the final state set
        // 5) make an empty transition function
        // 6) make the nfa
        // 7) add the desired transitions
        Set<Character> alphabet = new HashSet<>(Arrays.asList('0', '1'));
        Set<String> states = new HashSet<>(Arrays.asList("start", "one", "zero1", "zero2", "zero3"));
        String start = "start";
        Set<String> finals = new HashSet<>(Arrays.asList("zero3"));
        Map<Tuple,Set<String>> delta = new HashMap<Tuple,Set<String>>();
        NFA the_nfa = new NFA(states, alphabet, delta, start, finals);
        the_nfa.add_transition("start", '0', "start");
        the_nfa.add_transition("start", '1', "start");
        the_nfa.add_transition("start", '1', "one");
        the_nfa.add_transition("one", '0', "zero1");
        the_nfa.add_transition("zero1", '0', "zero2");
        the_nfa.add_transition("zero2", '0', "zero3");
        the_nfa.toDot();
    }
    
    public static void regex_example(){
        /*This demonstrates how you can use the system provided
        for regex matching*/
        String the_regex = "(a|b|c)*d";
        NFA equivalent_nfa = Regex.regex_to_NFA(the_regex);
        String matches = "aaabcacaccaaacccbd";
        String doesnt_match = "daacacc";
        boolean this_is_true = equivalent_nfa.execute(matches);
        boolean this_is_false = equivalent_nfa.execute(doesnt_match);
        System.out.println(this_is_true);
        System.out.println(this_is_false);
    }
    
    public static NFA trivial(){
        /*TODO: 
        Create an NFA which, for the alphabet {0,1}, 
        returns 1 on the empty string (and 0 on all 
        other strings).
        Your nfa should contain no more than
        1 state*/
        Set<Character> alphabet = new HashSet<>(Arrays.asList('0','1'));
        return new NFA();
    }
        
    public static NFA substring0101(){
        /*TODO: 
        Create an NFA which returns 1 on
        all strings from the alphabet {0,1}
        that contain 0101 as a substring
        (and 0 on all other strings).
        Your nfa should contain no more than
        5 states*/
        Set<Character> alphabet = new HashSet<>(Arrays.asList('0','1'));
        return new NFA();
    }
        
    public static NFA zerostar_onestar_zerostar(){
        /*TODO: 
        Create an NFA which returns 1 on
        all strings from the alphabet {0,1}
        that match the regular expression
        0*1*0*
        (and 0 on all other strings).
        Your nfa should contain no more than
        3 states*/
        Set<Character> alphabet = new HashSet<>(Arrays.asList('0','1'));
        return new NFA();
    }
    
    public static String huntingtons(dna_sequence){
        /*TODO: See task description for details*/
        return "at risk";
    }
}
