1. Given an N x M binary image f, initialize an associated
N x M region label array: r (n) = 0 for all n. Also initialize
a region number counter: k = 1.

Then, scanning the image from left to right and top to
bottom, for every n do the following:

2. If f(n) = 0 then do nothing.

3. If f(n) = 1 and also f(n - (1,O)) = f(n - (0, 1)) = 0,
as depicted in Fig. 8(a), then set r(n) = 0 and k = k + 1.
In this case the left and upper neighbors of f(n) do not
belong to objects.