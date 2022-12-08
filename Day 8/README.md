# Day 8 Reflections

Initially this looks like a recursive search to me, 
but I think I can do part 1 by just looping over the array and checking if all trees in any direction are shorter.

## Part 1
Yes that worked, pretty easy.

## Part 2
This should also be pretty easy, we just have to find the max view distance from each tree and multiply them together.

Forgot the case where the view is not obstructed at all in a direction, but otherwise no problem.