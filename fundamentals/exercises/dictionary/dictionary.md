# Build queries for a language dictionary

## Problem Statement

Use the fundamental tools of Python to implement queries for a dictionary of words and their meanings in any language

### Part 0

We will use the *Gutenberg* dictionary of English words for this exercise. You can find it here: **https://www.gutenberg.org/cache/epub/29765/pg29765.txt**
Download it and store it as **gutenberg_dictionary.txt**.
You also have a **dictonary.py** which contains some intial code. Basically, it has set up a few *command-line arguments* and in this exercise each of these arguments will be implemented one by one.

### Part 1

`--is_word word`

Whether or not `word` exists

`--word word`

If `word` exists in the dictionary, print the word and its meaning(s).
Otherwise, print "The word `word` does not exist" to console

Tip: Reuse functionality of code using *function(s)* and avoid copy+paste

### Part 2

`--words word1,word2,...`

For each word in the above list, print its meaning if it exists, else an appropriate message

### Part 3

`--after N`

Print `N` words after `word` in dictionary order

`--before N`

Print `N` words before `word` in dictionary order

Make sure these options work only if `--word` or `--words` is given

### Part 4

For all the words that are successfully searched, store them separately *somewhere* and call it as `cache`. Next time a word is queried, look for that word in this `cache`. If found, return the result right away. Otherwise, search the dictionary as usual.

This technique is called *caching*. It greatly improves the *performance* of queries of *repeated* words. The reason for increase in performance should be apparent.

Limit the number of words that are stored in cache to 100.

Tip: Think where all can you store this cache that can be used each time this program is run. We have seen such a place in one of the sessions.

### Part 5

`--cache-size N`

Set the number of words stored in cache to `N`
