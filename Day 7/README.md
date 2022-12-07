# Day 7 Reflections

Probably the first moderately "difficult" one as it is probably easiest to do with recursion.

I used a nested dictionary structure to represent the filesystem.
I first set up a function to parse the commands and populate the filesystem.
Each file/dir is a dict with a size and parent key. Dirs have a children key.

Then I made a functions to recurse down the filesystem and sum of the sizes of the files in the directory.
It is also passed an array to put references to each folder object.

# Part 1
Then I could just iterate over the array of folder objects and identify the sizes.

This made part 2 trivial.

# Part 2
I simply subtracted the size of the '/' dir to figure out how much space needs to be freed, and then sorted the folder array by size and iterated over it until I found the first folder that was big enough.recursion
