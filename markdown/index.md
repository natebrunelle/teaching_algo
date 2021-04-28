---
title: Algorithms
...

On this page I outline an algorithms course that I taught (with minor modifications) in Fall 2017, Spring 2018, Fall 2018 (co-instructor Robbie Hott), and Fall 2020 (co-instructor David Wu). I drew design inspiration from algorithms classes taught by Abhi Shelat in Spring 2016, by Mark Floryan in Fall 2016, Gabriel Robins in Fall 2015. The textbook which covers the most closely matches the content covered is *Introduction to Algorithms 3rd edition* by Cormen, Leiserson, Rivest, and Stein (aka CLRS). All slides and videos provided on this page come from Fall 2018.

My overall goals when designing this algorithms course are to:
- Develop a skill of algorithm design
- Understand different algorithm design paradigms, including what problem properties lend themselves to different strategies
- Learn how to justify the correctness and efficiency of algorithms
- Include example algorithms and assignments which are relevant to history, pop culture, politics, or science.
- Provide "toy" problems to serve as easy-to-grasp but faithful introductions to each topic

One aspect of the course that I'm particularly proud of are the warm-up questions. Nearly every lecture begins with a warm-up question. These questions are serve to:
- Introduce a key idea,
- Refresh background material,
- Reinforce lessons from a prior week, or
- Cover a "lemma" or other observation that will be relevant later in the same lecture.

The last purpose is particularly impactful, as students will experience a "eureka" moment mid-lecture when they recognize the concept from the warm up. This seems to increase student engagement during lecture, and enable students to understand that they've learned something from lecture before it's even over.

# Course Description

The goal of this course is to build a tool kit to better solve a variety of computational problems, and to evaluate the quality of such solutions. In particular, we will cover:

- Formal metrics for evaluating algorithm complexity (including the asymptotic classes big-oh, big-omega, big-theta, little-oh, and little-omega)
- Evaluating an algorithm's usage of resources (including time and space complexities) by a worst-case analysis, expected-case analysis, and amortized analysis
- Algorithm design strategies (including divide and conquer, dynamic programming, greedy, and reductions)
- The impact of data-structure choice on algorithm design
- Proving algorithm correctness
- Proving worst-case lower bounds on algorithm efficiency
- Discussion of randomized algorithms and expected efficiency
- Algorithms on graphs
- NP-Completeness

## Learning Outcomes

At the conclusion of this course, a successful student will be able to:

- Analyze a pre-written algorithm to determine its resource complexity
- Employ the strategies of divide and conquer, greedy, and dynamic programming (perhaps in concert) to develop novel algorithms
- Prove the correctness of algorithms built using these strategies
- Identify trade-offs in algorithm design (such as time vs. space, average-case vs. worst case, dynamic vs. static)
- Prove lower bounds on algorithm complexity

## Background

This course will assume knowledge of several topics from discrete math (CS2102 at UVA), two semesters of programming experience (through CS2110 at UVA), and data structures (CS2150 at UVA)

In particular, we assume elementary knowledge of:

- Logarithms and identities 
- Sets 
- Functions 
- Proof Techniques inluding: direct proof, proof by contradiction, proof by cases, and induction
- Logic and Notation
- Recursion 
- Trees
- Queues
- Stacks
- Priority Queues
- Hash Tables
- Graphs

# Unit 0: Course Introduction

In the first lecture I cover:

- A definition of the word "algorithm"
- Two algorithms for computing pi, including a discussion for how we can compare the "quality" of the two algorithms
- A paralellizable algorithm for taking attendance
- What to expect in the course

I also typically cover course logistics and some syllabus content. Those have been omitted from the video below.


<center><p>
<iframe width="560" height="315" src="https://youtube.com/embed/bUyWLT5MKEw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe><br>


<div style="display:table-cell; font-size:100%; margin: 1em auto; padding:1ex; box-shadow: 0 1px 10px rgba(0,0,0,.1); border: thin solid #eee; border-radius:1ex; background-image: linear-gradient(to bottom, #ffffff, #f2f2f2);">[Slides (pptx)](https://virginia.zoom.us/j/96370348427?pwd=clQzSEhWRHpnS2xYVGRQU3hHbU5Odz09)</div> <div style="display:table-cell; font-size:100%; margin: 1em auto; padding:1ex; box-shadow: 0 1px 10px rgba(0,0,0,.1); border: thin solid #eee; border-radius:1ex; background-image: linear-gradient(to bottom, #ffffff, #f2f2f2);">[Slides (pdf)](https://virginia.zoom.us/j/96370348427?pwd=clQzSEhWRHpnS2xYVGRQU3hHbU5Odz09)</div></center>

# Unit 1: Divide and Conquer

This unit covers the divide-and-conquer strategy for algorithm design. In my opinion, the strategy is easiest to wield if it's thought of as a recursive strategy. I simply find that defining the algorithm, proving correctness, and running time analysis are all simpler and easier to explain recursively. 

With a recursive definition, the algorithm definition can be broken into four major parts: base case, divide (identifying subproblems), conquer (recursively solving each subproblem), and combine (using subproblem solutions to determine the algorithm's output). The correctness can be proved using induction. The running time analysis 

# Unit 2: Sorting and Searching

# Unit 3: Dynamic Programing

# Unit 4: Greedy

# Unit 5: Reductions and NP-Completeness





