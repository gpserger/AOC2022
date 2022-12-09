# Day 9 Reflections

This problem was not that familiar to me but it doesn't seem that difficult.
I just need to keep track of the coordinates for both the head and tail,
and update the tail position according to how the headmoves.

# Part 1
This part just storing a set of all the coordinates the tail has visited and printing the length

# Part 2
I change the rope from 2 tuples to a list of tuples where the first is the head.
Then for each following knot, I calculate its next position using the preceding knot as the head.

Glad I got away with not having to print a visualization or use the second sample input.
