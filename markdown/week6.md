---
title: Week 6 Guide
...

# Goals

The main goals for Week 6 are to:

- Synthesize what we have learned about finite computation in the first 5 weeks, and start exploring unbounded computation.

- Appreciate the connection between functions and languages, and the different ways of talking about computation.

- Understand and be able to formally define a Finite State Automaton, and to reason about the language accepted (or function computed) by a Deterministic Finite Automaton.

- Be able to reason about the power of a DFA and understand deeply the proof that DFAs are strictly more powerful than Boolean circuits.

- Understand how to interpret Regular Expressions, define them formally, and reason about their capabilities.


# Schedule


|       Day       | "Tuesday" Cohort | "Wednesday" Cohort | "Thursday" Cohort  |  "Friday" Cohort   |   "Sunday" Cohort  |
| :-------------: | :--------------: | :----------------: | :----------------: | :----------------: | :----------------: |
|**Thurs** 11 Mar|<font color="lightgray">(Break)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|
|**Fri** 12 Mar|<font color="lightgray">(Break)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|
|**Sat** 13 Mar|<font color="lightgray">(Break)</font>|<font color="lightgray">(Week 4)</font>|Preparation|<font color="lightgray">(Week 4)</font>|<font color="lightgray">(Week 4)</font>|
|**Sun** 14 Mar|<font color="lightgray">(Break)</font>|<font color="lightgray">(Week 4)</font>|Preparation|Preparation|<font color="lightgray">(Week 4)</font>|
|**Mon** 15 Mar|<font color="lightgray">(Break)</font>|<font color="lightgray">(Week 4)</font>|Preparation|Preparation|<font color="lightgray">(Week 4)</font>|
|**Tues** 16 Mar|<font color="lightgray">(Break)</font>|<font color="lightgray">(Week 4)</font>|**Prep Cohort Meeting**|Preparation|Preparation|
|**Wed** 17 Mar|<font color="lightgray">(Break)</font>|<font color="lightgray">(Week 4)</font>|Revision|**Prep Cohort Meeting**|Preparation|
|**Thurs** 18 Mar|Preparation|<font color="lightgray">(Week 4)</font>|<font color="red">**Assessed Meeting**</font>|Revision|Preparation|
|**Fri** 19 Mar|Preparation|Preparation|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|**Prep Cohort Meeting**|
|**Sat** 20 Mar|Preparation|Preparation|<font color="lightgray">(Week 6)</font>|**Writeup Due**|Revision|
|**Sun** 21 Mar|**Prep Cohort Meeting**|Preparation|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="red">**Assessed Meeting**</font>|
|**Mon** 22 Mar|Revision|**Prep Cohort Meeting**|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|**Writeup Due**|
|**Tues** 23 Mar|<font color="red">**Assessed Meeting**</font>|Revision|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|
|**Wed** 24 Mar|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|
|**Thurs** 25 Mar|<font color="lightgray">(Week 6)</font>|**Writeup Due**|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|<font color="lightgray">(Week 6)</font>|

# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

- [Cohort Problems for Week 6 [PDF]](/files/ps/week6_blank.pdf)
- [LaTeX Template for Week 6 [ZIP]](/files/ps/week6.zip)

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

There is no programming problem this week.

# Reading

This week focuses on material in [Chapter 6: Functions with Infinite
domains, Automata, and Regular
expressions](https://introtcs.org/public/lec_05_infinite.html). Our
presentation in the videos differs from how things are presented in
the textbook (our way of defining a DFA is closer to the Alternate
Definition mentioned in Remark 6.3 than the way Definition 6.2 defines
a DFA; the book's presentation on regular expressions is similar to
ours, but not identical). Astute readers and viewers are encouraged to
look for places where the differences matter, or if they are only
cosmetic.

# Videos

<p>
These videos are edited from these cs3102 classes (we don't generally recommend watching the unedited versions, but they are available if you want to):

- (Spring 2020) Automata - [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=432abfa8-cdd8-4587-b2b7-ab6c0151eeb2), [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/automata_written.pdf)
- (Spring 2020) Regular Expressions and Closure - [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=34e95fad-c0b8-4c9f-adcf-ab6e0151e00c), [Slides](https://www.cs.virginia.edu/~njb2b/cstheory/s2020/files/slides/regex_written.pdf)

</p>

You can play all the videos using this playlist, but don't forget to take breaks: [Week 5 Playlist](https://www.youtube.com/playlist?list=PLZ9Gk_8DtbmEusKzGfXyNh0VNX0DCS1Vx)

<p>Week 6 Intro (12:28) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/73FNVUv0CUA' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Warm-up: Questions about Strings (4:01) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/O5aonOdyxec' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Functions and Languages (11:16) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/VvdjLr5GNsg' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>



<p>Beyond Finite Functions (8:23) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/YMgUTfl1718' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Finite Automaton for XOR (6:28) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Us4zrlmIOaY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
<p>Formalizing Finite State Automata (3:29) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/kgTxZlRPGqw' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Power of Deterministic Finite Automata (8:15) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/FMi_pZp6NrY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Regular Expressions (17:27) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/LE9Jns4DUnU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Optional Bonus Video: The Lasagna Language (7:00) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/xeKX-WsINbw' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>



