# Tic-tac-toe game with Minimax AI
Tic-tac-toe game with an AI powered by the Minimax algorithm.

## The Minimax Algorithm
Minimax is an algorithm used in games with two players (e.g. tic-tac-toe, chess, checkers), where one player is the *maximizer* and the other is the *minimizer*. In this case,
the 'X' is the maximizer and the 'O' is the minimizer.
While the maximizer aims to get the highest possible score, the minimizer aims for the opposite. The algorithm recursively goes through every possible move until it
reaches an end state (however, this is limited to a certain depth in bigger games like chess). Then, every end state is evaluated: if it is a win for X, or the maximizer, it gets
a score of 1. On the other hand, if it is a win for O, it gets a score of -1, while a tie gets a score of 0 (it favours none of the players).

## Optimized with alpha-beta pruning. 
Although tic-tac-toe is a small game and does not require much computing power, the AI seemed to take a little while when making the first move. 
This is presumably due to the fact that the algorithm has to traverse every single child node until the leaves, which can add up quickly.
Without alpha-beta pruning, it took the AI around 4.50 seconds each time when making the first move. 
After implementing alpha-beta pruning, this time was decreased considerably, as it now only takes around 0.15 seconds.
All the subsequent moves also saw a decrease in time (e.g. second move average ~0.7 sec reduced to ~0.08 sec).

