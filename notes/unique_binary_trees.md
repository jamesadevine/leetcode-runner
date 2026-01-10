# unique binary trees

The problem asks to compute the number of unique binary trees. Once you know what they are asking for it is ok.

For each root node, you must count the number of nodes to the left and right. If either way has a value of zero, it still counts as one as it is valid.

the number of left nodes is the current node number - 1, and the number of right nodes is the total number of nodes - the current node number