### Problem:

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

### Hints:
My approach:   
store 10-letter-string to dict, and then check strings.  

1. check duplicated string in result.

Time cost O(N), Memory too much

#### References:
78 136 137 187 169  

#### Tags:
Dictionary, bit manuplate