### Problem:
>  The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
> And then read line by line: "PAHNAPLSIIGYIR"
>
> Write the code that will take a string and make this conversion given a number of rows:
`string convert(string text, int nRows);`
>
> convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 

### Hints:
* create a list of row strings
* set index and step
* walking through string by index and step: move to first row, set step to 1, move to last row set step to -1(backward)
* join strings of each rows

#### References:

#### Tags:
String
