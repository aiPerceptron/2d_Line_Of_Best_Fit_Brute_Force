# 2d Line Of Best Fit but using Brute Force
This is the 2D line of best fit, but instead of using gradient descent I'm checking for every possible number.

You can find the lowest point within a certain range of numbers and step (step means how much are you incrementing per number, a step of 1 would be 1, 2, 3, 4 and so on.) 

However, This method really isn't as good as it seemes because checking every single number makes the performance of this method terrible. I ended up writing so much more code, because you have to check for every single number, and modify the step and range for M and B.

It adds complexity to the code too. Using gradient descent you can find the refined form of M in just one line. With Brute force on the other hand, you have to loop through lists and try every single number, adding so much more lines to the code.
