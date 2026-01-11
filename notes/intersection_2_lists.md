Relies on clever pointer counting trick!

the number of steps to traverse two non-intersecting lists before reaching none is m + n.

Therefore, to hit none at the same time:
* a: traverse m -> swap to n -> traverse reach none.
* b: traverse n -> swap to m -> traverse reach none at same time.