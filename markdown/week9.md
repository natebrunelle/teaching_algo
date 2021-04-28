---
title: Week 9 Guide
...


# Goals

Last week, we used a counting argument to show that there must be some
uncomputable functions ("some" here means infinitely many), but we
didin't find a specific uncomputable function. This week, we prove
that a particular function is uncomputable, and explore the
implications of finding an uncomputable function.

The main goals for Week 9 are to:

- Understand what cannot be computed by a finite automaton and why.
- Use and understand Turing Machines as a model of computing.
- Study a definition of computability.
- Explore the powers and limitations of Turing Machines.
- Understand why some numbers are _uncomputable_, and what this means.
- Learn different variations on Turing Machines and how they can be transformed.


# Schedule


|       Day       | "Tuesday" Cohort | "Wednesday" Cohort | "Thursday" Cohort  |  "Friday" Cohort   |   "Sunday" Cohort  |
| :-------------: | :--------------: | :----------------: | :----------------: | :----------------: | :----------------: |
|**Thurs** 01 Apr|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|
|**Fri** 02 Apr|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|
|**Sat** 03 Apr|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|Preparation|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|
|**Sun** 04 Apr|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|Preparation|Preparation|<font color="lightgray">(Week 8)</font>|
|**Mon** 05 Apr|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|Preparation|Preparation|<font color="lightgray">(Week 8)</font>|
|**Tues** 06 Apr|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|**Prep Cohort Meeting**|Preparation|Preparation|
|**Wed** 07 Apr|<font color="lightgray">(Week 8)</font>|<font color="lightgray">(Week 8)</font>|Revision|**Prep Cohort Meeting**|Preparation|
|**Thurs** 08 Apr|Preparation|<font color="lightgray">(Week 8)</font>|<font color="red">**Assessed Meeting**</font>|Revision|Preparation|
|**Fri** 09 Apr|Preparation|Preparation|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|**Prep Cohort Meeting**|
|**Sat** 10 Apr|Preparation|Preparation|<font color="lightgray">(Week 10)</font>|**Writeup Due**|Revision|
|**Sun** 11 Apr|**Prep Cohort Meeting**|Preparation|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="red">**Assessed Meeting**</font>|
|**Mon** 12 Apr|Revision|**Prep Cohort Meeting**|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|**Writeup Due**|
|**Tues** 13 Apr|<font color="red">**Assessed Meeting**</font>|Revision|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|
|**Wed** 14 Apr|**Writeup Due**|<font color="red">**Assessed Meeting**</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|
|**Thurs** 15 Apr|<font color="lightgray">(Week 10)</font>|**Writeup Due**|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|<font color="lightgray">(Week 10)</font>|

# Cohort Problems

These are the problems you should discuss in your Cohort Meeting, and
everyone in your cohort should be prepared to present and discuss
solutions to at the Assessed Cohort Meeting:

- [Cohort Problems for Week 9 [PDF]](/files/ps/week9_blank.pdf)
- [LaTeX Template for Week 9 [ZIP]](/files/ps/week9.zip)

The problems are posted here and we think its a good idea to look at
them early, but you're not expected to be able to solve them until
after doing the readings and watching the videos below.

There is no programming portion for this week.

# Reading

[Chapter 9: _Universality and uncomputability_](https://introtcs.org/public/lec_08_uncomputability.html) [[PDF](https://files.boazbarak.org/introtcs/lec_08_uncomputability.pdf)]

You should read through the end of Section 9.3 (including the "optional" section 9.3.2). (We will cover Section 9.4 and 9.5 next week.)

The material in Sections 9.1 &ndash; 9.3 covers the same concepts as
we do in the lectures, but in a somewhat different order and with a
focus on <em>HALT</em> rather than <em>ACCEPTS</em>. You should
consider how similar and different these two functions are, and
compare the proof that <em>ACCEPTS</em> is uncomputable from the
lectures to the one in the book that <em>HALT</em> is uncomputable.

# Videos

You can play all the videos using this playlist, but don't forget to take breaks: [Week 9 Playlist](https://youtube.com/playlist?list=PLZ9Gk_8DtbmErIKSl3pEl6KhZfKZWhezW)
<p>
This week's content is most similar to that of these previous-semester's cs3102 classes:

- (Fall 2019) [Class 14: Computability](https://uvatoc.github.io/f19/class14/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e086e67f-71aa-45e1-a59d-aaed01412ded), [Slides](https://www.dropbox.com/s/nw9zh8a0vahvaqy/class14-inked.pdf?dl=0) (just part of the _Self-Rejection (An Uncomputable Function)_ video)

- (Fall 2019) [Class 15: Universality and Uncomputability](https://uvatoc.github.io/f19/class15/): [Full Video](https://uva.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=c8ce23af-8a26-44b4-9678-aaef01410d8e), [Slides](https://www.dropbox.com/s/iibngc72d0snb0f/class15-inked.pdf?dl=0)


<p>Introduction (3:20) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Zqqv8MWnC6c' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>Self-Rejection (An Uncomputable Function) (17:13) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/qRNIK4qaNTA' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>An Uncomputable Problem in Python (8:10) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Bit7FvUzcMU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Universal Turing Machines (8:54) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/Ij01xiZDN8k' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>


<p>ACCEPTS, Practical but Uncomputable (15:53) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/L-MkPxn5r_s' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>

<p>Computability in Theory vs Practice (8:50) <br><iframe width='800' height='450' src='https://www.youtube-nocookie.com/embed/YbrFeIC3jXo' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe><br></p>



