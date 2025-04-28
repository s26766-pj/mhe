3-partition problem, [wikipedia](https://en.wikipedia.org/wiki/3-partition_problem)

The 3-partition problem is a strongly NP-complete problem in computer science. The problem is to decide whether a given multiset of integers can be partitioned into triplets that all have the same sum. More precisely:

Input: a multiset S containing n positive integer elements.
Conditions: S must be partitionable into m triplets, S1, S2, …, Sm, where n = 3m. These triplets partition S in the sense that they are disjoint and they cover S. The target value T is computed by taking the sum of all elements in S, then divided by m.
Output: whether or not there exists a partition of S such that, for all triplets, the sum of the elements in each triplet equals T.
The 3-partition problem remains strongly NP-complete under the restriction that every integer in S is strictly between T/4 and T/2.
