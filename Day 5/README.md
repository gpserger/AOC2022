# Day 5 Reflections

## Part 1
Parsing the stacks was a bit tedious, especially since I had the wrong approach at the start.
I was trying to use string replace to detect empty spaces but that doesn't work very well.
Then I switched to traversing the string in 4-character wide sections and that worked very well.

To represent the ship's cargo I used queue.LiFoQueue, as stacks.

## Part 2