# Tic-tac-toe game with Minimax AI
Tic-tac-toe game with an AI powered by the Minimax algorithm.

## Optimized with alpha-beta pruning. 
Although tic-tac-toe is a small game and does not require much computing power, the AI seemed to take a little while when making the first move. 
This is presumably due to the fact that the algorithm has to traverse every single child node until the leaves, which can add up quickly.
Without alpha-beta pruning, it took the AI around 4.50 seconds each time when making the first move. 
After implementing alpha-beta pruning, this time was decreased considerably, as it now only takes around 0.15 seconds.
All the subsequent moves also saw a decrease in time (e.g. second move average ~0.7 sec reduced to ~0.08 sec).

