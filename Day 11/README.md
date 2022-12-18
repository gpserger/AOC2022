# Day 11 Reflections

Okay right off the bad we have to parse some text.
For the operation we can probably use python's eval function, which would be pretty cool.

The way the boredom mechanic (dividing worry level by 3) works is not that clear.
It seems that every time they inspect an item, their operation occurs, and then the division.

# Part 1
Using eval with local variables was a bit trickier than expect, but I got it to work.

Easy enough
# Part 2
Okay so the problem here is working with big numbers which takes a long time.
It's been a while since I did this type of number theory.
Some googling points me to the chinese remainder theorem to keep the worry levels manageable.
This took me a while to relearn.

It's not the fastest but it solves it in under 10 seconds.