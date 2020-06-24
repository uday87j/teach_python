# Explore socialization aspects

## Problem statement

Use basics of Python to extract interesting inferences from a social network

### Part 0

A file called `network` contains the names of people in our social network.
The names are listed in alphabetical order.
It also contains a bitmap of *1s and 0s* to indicate whether or not a person is connected with another person indicated by the bit position in the bitmap.
The bitmap starts from position 0 at the left most bit and increases as we scan towards the right.
For example,
**SOMEONE 10001000**
`# Indicates that SOMEONE is connected to 0th person and 4th person.`

### Part 1

Create a Python program and add a command-line argument called `--most-connected` that outputs the person with maximum number of connections to ther people.

Similarly, add `--least-connected`

Tip: Think of different ways in which this network can be represented in Python

### Part 2

`--least-connected-in-largest-network`

The person, belonging to largest network, and has minimum connections

`--most-connected-in-smallest-network`

Similar to above

### Part 3

`--starts-with-person  person`

Given `person`, output all the people that have the same first letter in their name

`--starts-with-person-in-network`

Given `person`, output all the people in their network that have the same first letter in their name

### Part 4

`--total-networks`

Number of total connected components

`--avg-network-size`

Average size of connected networks

`--largest-network-size`

`--smallest-network-size`

### Part 5

`--person-network-size  person`

Network size containing `person`

`--most-connected-person-in-network-containing  person`

Who is the most connected person in the network containing `person`

`--least-connected-person-in-network-containing  person`

Who is the least connected person in the network containing `person`

`--network-index-of  person`

Of all the network sizes, in descending order, the positional index of the network containing `person`
