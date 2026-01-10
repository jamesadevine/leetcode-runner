# bitwise and

This is one where you just have to know the trick...

Any inclusive range AND will result in the common prefix of the two values being shared. This is because when you AND two numbers only the common set bits remain.

5 = 101
6 = 110
7 = 111
    ---
    100 = 4  ← only the leftmost bit (the common prefix) survives

So, to get to the answer, you simply shift until both values are equal, keeping track of the number of shifts. Then shift the value by the number of shifts performed.


This is the naiive answer:
```
value = left
    for i in range(left + 1, right):
        value &= i
    print(value)
    return value
```