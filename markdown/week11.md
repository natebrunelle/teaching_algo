---
title: Week 11 Guide
...

# Goals

This week we arrive at the most famous and foundational open problem
in Computer Science (and, arguably, in all of Mathematics, and more
questionably, perhaps of all human creative endeavor): _is it
substantially easier to verify the solution to a (certain very broad
and common type of) problem, than it is to find that solution?_
(stated more formally in computer science as "P = NP?".

The main goals for Week 11 are to:

- Understand how to talk about the hardness ("difficulty") of computing functions.
- Learn about a few examples of problems that appear to have surprisingly different difficulties.
- Be able to talk about the _tractability_ of problems, and understand what computer scientists categorize problems as tractable and intractable the way we do.
- Understand precisely the definition of the complexity class NP, and two different ways of defining it.
- Be able to prove a problem is in class NP.
- Understand the P=NP question and its significance.
- See how we might be able to make progress on determining if P=NP, and understand the Cook-Levin Theorem and the main idea behind its proof.

# Schedule

|       Day       | "Tuesday" Cohort | "Wednesday" Cohort | "Thursday" Cohort  |  "Friday" Cohort   |   "Sunday" Cohort  |
| :-------------: | :--------------: | :----------------: | :----------------: | :----------------: | :----------------: |
|**Sun** 18 Apr|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|Preparation|<font color="lightgray">(Week 10)</font>|
|**Mon** 19 Apr|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|Preparation|<font color="lightgray">(Week 10)</font>|
|**Tues** 20 Apr|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|Preparation|Preparation|
|**Wed** 21 Apr|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|**Prep Cohort Meeting**|Preparation|
|**Thurs** 22 Apr|Preparation|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|Revision|Preparation|
|**Fri** 23 Apr|Preparation|Preparation|<font color="lightgray">(Week 10)</font>|<font color="red">**Assessed Meeting**</font>|**Prep Cohort Meeting**|
|**Sat** 24 Apr|Preparation|Preparation|Preparation|**Writeup Due**|Revision|
|**Sun** 25 Apr|**Prep Cohort Meeting**|Preparation|Preparation|<font color="lightgray">(Week 12)</font>|<font color="red">**Assessed Meeting**</font>|
|**Mon** 26 Apr|Revision|**Prep Cohort Meeting**|Preparation|<font color="lightgray">(Week 12)</font>|**Writeup Due**|
|**Tues** 27 Apr|<font color="red">**Assessed Meeting**</font>|Revision|**Prep Cohort Meeting**|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|
|**Wed** 28 Apr|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|Revision|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|
|**Thurs** 29 Apr|<font color="lightgray">(Week 12)</font>|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|
|**Fri** 30 Apr|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|**Writeup Due**|<font color="lightgray">(Week 12)</font>|<font color="lightgray">(Week 12)</font>|

# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

- [Cohort Problems for Week 11 [PDF]](/files/ps/week11_blank.pdf)
- [LaTeX Template for Week 11 [ZIP]](/files/ps/week11.zip)

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

There is no programming portion for this week.

# Reading

This week's content is covered in several chapters in the TCS
book. This is a lot of reading material, but you should consider it
all "optional" this week - you are not expected to read these in
detail, but should find the textbook a useful complement to the
lecture content to have an alternate presenation of the materials and
a refernce for some of the technical details that we do not cover in
depth in the lectures.

[Chapter 12: _Efficient computation: An informal introduction_](https://introtcs.org/public/lec_10_efficient_alg.html) [[PDF](https://files.boazbarak.org/introtcs/lec_10_efficient_alg.pdf)]

[Chapter 13: _Modeling running time_](https://introtcs.org/public/lec_11_running_time.html) [[PDF](https://files.boazbarak.org/introtcs/lec_11_running_time.pdf)]

[Chapter 14: _Polynomial-time reducations_](https://introtcs.org/public/lec_12_NP.html) [[PDF](https://files.boazbarak.org/introtcs/lec_12_NP.pdf)]

[Chapter 15: _NP, NP completeness, and the Cook-Levin Theorem_](https://introtcs.org/public/lec_13_Cook_Levin.html) [[PDF](https://files.boazbarak.org/introtcs/lec_13_Cook_Levin.pdf)]

[Chapter 16: _What if P equals NP?_](https://introtcs.org/public/lec_14_PvsNP.html) [[PDF](https://files.boazbarak.org/introtcs/lec_14_PvsNP.pdf)]




# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 11 Playlist](https://www.youtube.com/playlist?list=PLZ9Gk_8DtbmEoyPsllwtPpuh3EhTbvdS8)

<p>
You can find recordings of the past cs3102 classes with most similar content here:

- (Fall 2019) [Class 19: Turing Machine running time](https://uvatoc.github.io/f19/class19/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=3e454df5-59af-4a8b-a257-ab020151ee1b), [Slides](https://www.dropbox.com/s/vcsuqjrnqld3lhk/class19_written.pptx?dl=0)

- (Fall 2019) [Class 20: Polynomial-Time Reductions](https://uvatoc.github.io/f19/class20/) (: [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5502d967-a9a6-402b-842e-ab040151b68a), [Slides](https://www.dropbox.com/s/u79nw0c5dpgkb22/class20_written.pptx?dl=0)

- (Fall 2019) [Class 21: Is Omniscience Helpful?](https://uvatoc.github.io/f19/class21/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2065c1c3-8d0f-4fbd-8005-ab0901519772), [Slides](https://www.dropbox.com/s/84jpjahs7afgvfv/class21-post.pdf?dl=0)

- (Fall 2019) [Class 22: NP Completeness](https://uvatoc.github.io/f19/class22/): [Fall Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=cb91d06d-83f5-47d8-a05c-ab0b0151a8de), [Slides](https://www.dropbox.com/s/rqtkwlp6hk9m7vo/class22-post.pdf?dl=0)


<p>"Difficulty" of Functions (9:13) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/PosxxVwgggI' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>RAM Model (7:00) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/tcjSV1QSdn8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Shortest and Longest Path (11:16) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/g5Zpffr4Wog' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Satisfiability (14:45) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/cMEKwh614mk' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Tractable and Intractable Problems (6:38) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/SspCMbUF6Xs' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Polynomial Time Reductions (13:25) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/rDzdsvVqaDc' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Reducing 3SAT to LongestPath (16:54 total, with 9:30 of that optional [you may skip the proof from 3:35-13:05]) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/KgJnNZm8YuA' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Longest Path Decision Problem (4:11) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/CPqsKxjPFCo' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Nondeterministic TMs and the class NP (23:25) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/ot-H1BKK2ss' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Why do we care whether P=NP? (5:38) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/XSb4E8pJz2M' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>NP Completeness (15:51) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/2MqgnyhhCq8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>
