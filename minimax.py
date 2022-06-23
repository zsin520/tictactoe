import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    
    count=0
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                count+=1

    if (count%2) == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    
    possibleActions=set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possibleActions.add(tuple((row,col)))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if len(action) != 2:
        raise Exception ('Invalid action: ',action)

    if action[0]<0 or action[0]>2 or action[1]<0 or action[1]>2:
        raise Exception ('Invalid action: ',action)
    
    row=action[0]
    col=action[1]
    
    if board[row][col] != EMPTY:
        raise Exception ('Move has already been made: ',action)
    else:
        import copy
        newBoard=copy.deepcopy(board)
        newBoard[row][col] = player(board)
        return newBoard 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check vertical 
    for v in range(3):
        if (board[0][v] == board[1][v] == board[2][v]) and board[0][v] != EMPTY:
            return board[0][v]

    #check horizontal
    for h in range(3):
        if (board[h][0] == board[h][1] == board[h][2]) and board[h][0] != EMPTY:
            return board[h][0]

    #check diagonals
    if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]) and board[1][1] != EMPTY:
        return board[1][1]

    #otherwise there is no winner
    return None 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board)==X or winner(board)==O):
        return True
    elif (EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]):
        return True
    else:
        return False 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    alpha=-(math.inf)
    beta=math.inf
    
    if terminal(board):
        return None
    
    if player(board) == O:

        value= math.inf
        move= None
    
        for action in actions(board):
            max_value=maxValueMove(result(board,action),alpha,beta)
  
            if max_value<value:
                value=max_value
                move=action
        return move 

    elif player(board) ==X:

        value= -(math.inf)
        move= None
    
        for action in actions(board):
            min_value=minValueMove(result(board,action),alpha,beta)

            if min_value>value:
                value=min_value
                move=action
        return move 

def maxValueMove(board,alpha,beta):
    if terminal(board):
        return utility(board)

    min_value=-(math.inf)

    for action in actions(board):
        min_value=max(min_value,minValueMove(result(board,action),alpha,beta))

        alpha=max(alpha,min_value)
        if beta <= alpha:
            break

    return min_value

def minValueMove(board,alpha,beta):
    if terminal(board):
        return utility(board)

    max_value=math.inf
    
    for action in actions(board):
        max_value=min(max_value,maxValueMove(result(board,action),alpha,beta))

        beta=min(beta,max_value)
        if beta <=alpha:
            break
        
    return max_value 
