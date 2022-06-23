# tictactoe
This project is an adversarial search problem, tictactoe, where there is an opponent that is trying to achieve the opposite goal. The agent is given an initial state, a game board represented as a 2D list, a list of three lists, filled with three different variables, X, O, and EMPTY, and the purpose is to reach a goal state, win the game or draw.

Minimax algorithm is used. There are two hypothetical players, a minimum and maximum player. The goal of the maximum player is to get the highest score and vice versa. The algorithm represents scores as -1, 1 for each player respectively and 0 for a draw. The algorithm recursively searches all possible game states from the initial game state to the terminal state. The actions of the players will be dictated by the minimum or maxmimum value given different terminal states. The maximizing player will choose an action that produces the highest terminal value based on actions that assume the minimum player plays optimally. 

An introduction to AI with python project by Harvard University Online
