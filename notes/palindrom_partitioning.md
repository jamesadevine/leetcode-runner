# palindrome partitioning

each character is a palindrome

need to learn a technique called backtracking.

Backtracking is a tree exploration pattern where you build up state going down and restore it coming back up.

For palindrome, we iterate over the string and for each palindrome explore the remaining string.

When the palindrome reaches the len of S this is the success criteria - add to results

if we bum out, we pop the partitions array.