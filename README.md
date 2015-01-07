IBM Ponder This Challenge / December 2014
=========================================

http://domino.research.ibm.com/Comm/wwwr_ponder.nsf/Challenges/December2014.html

While the solution appeared to be very simple,
I had started with much much more complex approaches :)

I first tried different ways to bruteforce it (or at
least part of it), looking for various ways to reduce
dimensionality of solution space: to use symmetry of all
kinds, etc.

After several days like this I gave up and decided to look
at some examples (this is actually what I should've start with).
So I wrote the script which was enumerating all possible matrices 
for some small dimensions and grouping them by horizontal/vertical
sums to see how many matrices (and which exactly) produce this exact
pair of sums.

After staring at several examples for some minutes I more or less 
quickly found this interesting pattern:

1 0 
1 0
0 1

1 0 0
1 0 0 
0 1 1

The first matrice belongs to the set of exactly 3 matrices that produces
(1, 1, 2), (2, 1) sums. The second one, made from the first by duplicating second
column belongs to the set with 5 solutions. I checked it out with my script and
at came out that we can build the matrices like this:

1 0 0 ... 0
1 0 0 ... 0
0 1 1 ... 1

to repesent any odd number.

The matrice for "29" will contain 15 columns, have sums like this:

1 1 14
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 

and have 3 * 15 = 45 < 50 elements. So we win :) ■

