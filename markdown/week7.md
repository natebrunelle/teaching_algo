---
title: Week 7 Guide
...

## Peer Eval

Please complete your second peer evaluation survey [https://forms.gle/9KGfo25j6fpLcC7n7](https://forms.gle/9KGfo25j6fpLcC7n7) after your week 6 assessed meeting and before your week 7 assessed meeting.

The rubric you should use is the same as we had for the last evaluation, which you can find here:
http://www.cs.virginia.edu/~njb2b/cstheory/s2021/peer_eval.html

Please, if something is amiss with your cohort, bring it up in your evaluation. Your comments will not cause a student to receive a lower grade unless those comments are corroborated by other cohort members' comments, and the issues persist across several weeks.

There have been several situations (between last semester and this semester) where students have reached out to me or a TA regarding an ineffective or toxic cohort-member, but they gave glowing ratings in the peer eval form. When this happens, trying to address the situation is much harder (the cohort-members are telling each other one thing, and the professor something else), and takes much more time. 

If something is going wrong, please say something. I'm here to help you and your cohort work through it, but it's easier if the air is cleared. If you want to say something, but are unsure of how to tactfully phrase it in the form, send me a DM and I'd be happy to help you work through it.

# Goals

The main goals for Week 7 are to:

- Understand the proof that Regular Expressions are equivalent in power to Deterministic Finite Automata. This is a long proof, split over 4 videos, but is something we hope everyone understands in detail. The methods used in the proof are similar to ones we have seen before in showing equivalence of NAND-Circ and Boolean circuits, but is a fair bit more complex. This general method of showing equivalence is something we will see again in this class, and you will encounter many more times in other classes and work that you will do.

- Become familiar with the power and strangeness of nondeterminism. For finite automata, we prove this week that despite is seeming super-power, nondeterministic finite automata cannot compute any functions (or recognize any languages) that cannot be computed by deterministic finite automata. The main topic for Weeks 8-11 will be considering this question for more powerul computing models (which is the most famous open problem in computer science).

# Schedule


|       Day       | "Tuesday" Cohort | "Wednesday" Cohort | "Thursday" Cohort  |  "Friday" Cohort   |   "Sunday" Cohort  |
| :-------------: | :--------------: | :----------------: | :----------------: | :----------------: | :----------------: |
|**Thurs** 18 Mar|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|
|**Fri** 19 Mar|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|
|**Sat** 20 Mar|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|Preparation|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|
|**Sun** 21 Mar|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|Preparation|Preparation|<font color="lightgray">(Week 6)</font>|
|**Mon** 22 Mar|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|Preparation|Preparation|<font color="lightgray">(Week 6)</font>|
|**Tues** 23 Mar|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|**Prep Cohort Meeting**|Preparation|Preparation|
|**Wed** 24 Mar|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|Revision|**Prep Cohort Meeting**|Preparation|
|**Thurs** 25 Mar|Preparation|<font color="lightgray">(Week 6)</font>|<font color="red">**Assessed Meeting**</font>|Revision|Preparation|
|**Fri** 26 Mar|Preparation|Preparation|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|**Prep Cohort Meeting**|
|**Sat** 27 Mar|Preparation|Preparation|<font color="lightgray">(Week 8)</font>|**Writeup Due**|Revision|
|**Sun** 28 Mar|**Prep Cohort Meeting**|Preparation|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|<font color="red">**Assessed Meeting**</font>|
|**Mon** 29 Mar|Revision|**Prep Cohort Meeting**|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|**Writeup Due**|
|**Tues** 30 Mar|<font color="red">**Assessed Meeting**</font>|Revision|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|
|**Wed** 31 Mar|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|
|**Thurs** 01 Apr|<font color="lightgray">(Week 8)</font>|**Writeup Due**|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|

# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

- [Cohort Problems for Week 7 [PDF]](/files/ps/week7_blank.pdf)
- [LaTeX Template for Week 7 [ZIP]](/files/ps/week7.zip)

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

## Programming

Before you begin on this assignment, you will need to download three python files and place them in the same project:

- [NFA.py](/files/ps/NFA.py)
- [regex.py](/files/ps/regex.py)
- [week7.py](/files/ps/week7.py)


The `NFA` program implements nfa simulation and various closure constructions. The `regex` program defines a class that reads regular expressions and converts them to NFAs. The `week7` program contains example uses of the `NFA` and `regex` functionality, and also contains the stub for the `huntingtons` function you must implement.

You'll need to use the following functions (example usage of all of them are in `week7.py`):

- `regex.regex_to_NFA(the_regex)`: If `the_regex` is a string, the function `regex_to_NFA` found in `regex.py` returns and NFA that computes the language indicated by `the_regex`
- `the_nfa.execute(the_string)`: If `the_nfa` is an instance of the `NFA` class defined in `NFA.py`, then invoking the class method `execute` on string `the_string` will return a Boolean value indicating whether or not `the_string` belonged to the language of the NFA.
- `the_nfa.toDot()`: If `the_nfa` is an instance of the `NFA` class defined in `NFA.py`, then invoking the class method `toDot()` will result in a dot (which is a graph specification language) description of the NFA being printed to standard out. You can then copy-paste that description here to see the actual NFA: [https://dreampuf.github.io/GraphvizOnline/](https://dreampuf.github.io/GraphvizOnline/)

### What to do

First, read through all of `week7.py` and follow the instructions therein to make sure you understand what's going on. After this you'll implement the `huntingtons` function.

For the `huntingtons` function you're asked to implement, the idea is for you to use regular expressions to diagnose whether a person has Huntington's disease by looking at their genome.

A dna sequence is a string of the characters a, t, g, c, representing the sequence of nucleotides that comprise an individual's dna molecules. Very often, the human genome has regions where the same nucleotide sequences repeat many times. Sometimes, certain numbers of these repeats will result in a genetic disorder.
        
Huntington's Disease is caused by having too many consecutive copies of the sequence "cag". By looking at a dna sequence, we can categorize how a person might be affected by Huntington's in the following way:
        
- An individual with less than 26 sequential repeats of "cag" in their genome is considered to be "normal".
- An individual with between 26 and 35 repeats of "cag" is considered to be a "carrier", and may give the disease to their children.
- An individual with between 36 and 39 repeats is said to be "at risk", and may or may not ever show symptoms.
- An individual with 40 or more repeats is said to be "affected", and will eventually show symptoms of the disease.

Your `huntingtons` function should take a dna sequence (a string from the alphabet a,g,t,c) and determine the classification for the individual (i.e. normal, carrier, at risk, or affected). To do this, define a regex for each category, convert each to a nfa, then check which category the given dna sequence falls into. Once you have determined the category, the function should return the appropriate string of: "normal", "carrier", "at risk", or "affected"
        
Note that the dna sequence may have characters before/after the "cag" repeats.
            
[Source describing Huntingtons](https://en.wikipedia.org/wiki/Huntington%27s_disease).


# Reading

This week continues with the material in [Chapter 6: Functions with
Infinite domains, Automata, and Regular
expressions](https://introtcs.org/public/lec_05_infinite.html) that we
started on last week.

[Section 6.4.2](https://introtcs.org/public/lec_05_infinite.html#regdfaequivsec)
of the book includes a proof that regular expressions are equivalent
in power to deterministic finite automata, but it is quite different
from the proof we do in the videos. Ambitious students are encouraged
to understand both proofs, and to consider the advantages and
disadvantages of the approach taken in the book compared to our
approach (which is the one done more traditionally in theory of
computation courses, at least going back to Mike Sipser's courses in
the 1980s).

There are many books (and other videos) that do present material
similar to what is in the videos this week, but we are not assigning
any additional readings.


# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 7 Playlist](https://www.youtube.com/playlist?list=PLZ9Gk_8DtbmESvxHPmmNcWY3kkMatxKc0)
<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Spring 2020) Nondeterminism: [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0f798579-372f-45ca-bef6-ab730151cf45), [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/non-determinism_written.pdf)
- (Spring 2020) FSA Equivalent to Regular Expressions: [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=65c2b08e-1ce7-4e25-a257-ab75015297b1), [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/fsa_equals_regex.pdf)

</p>

<p>Nondeterministic Nathans (1:23) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/hd809qBaNYY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Warm-Up: Complementing the XOR Language (5:54) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Se4LhD_NTk8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Equivalence of Regular Expressions and FSAs (6:12) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Vcv6dR3__g8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Proving FSAs are as Powerful as Regular Expressions (Part 1: Proof Strategy) (4:35) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/IGPKOmACoes' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Proving FSAs are as Powerful as Regular Expressions (Part 2: Bases, Union) (22:55) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/aA47ceLSuoc' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Nondeterminism (11:14) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Qu8NsFh2Ss4' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Nondeterministic Finite Automata (NFAs) (13:48) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/5fk2ej5jU8c' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Equivalence of NFAs and DFAs (10:01) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/iO-0KWSJs3A' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Proving FSAs are as Powerful as Regular Expressions (Part 3: Concatenation) (14:58) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/84tXODX8RGo' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Proving FSAs are as Powerful as Regular Expressions (Part 4: Kleene Star) (8:21) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/xV7nnli95tw' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>



