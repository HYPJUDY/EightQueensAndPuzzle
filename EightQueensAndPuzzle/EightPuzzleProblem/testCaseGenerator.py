import random

def step_RandomHillClimbing(board):
    for i in range(len(board)):
        if board[i] == 0:
            break
    while True:
        randCase = random.randint(0,4)
        if randCase == 0:
            if i >= 3:
                upBoard = list(board)
                upBoard[i] = board[i-3]
                upBoard[i-3] = 0
                return upBoard
        elif randCase == 1:
            if i < 6:
                downBoard = list(board)
                downBoard[i] = board[i+3]
                downBoard[i+3] = 0
                return downBoard
        elif randCase == 2:
            if i%3 != 0:
                leftBoard = list(board)
                leftBoard[i] = board[i-1]
                leftBoard[i-1] = 0
                return leftBoard
        else:    
            if (i+1)%3 != 0:
                rightBoard = list(board)
                rightBoard[i] = board[i+1]
                rightBoard[i+1] = 0
                return rightBoard
        
    return board

def solution_RandomHillClimbing(board):
    maxStep = 5000
    count = 0
    while True:
        board = step_RandomHillClimbing(board)
        count += 1
        if(count >= maxStep):
            return board
    

def main():
    f = open("eightPuzzleTest.txt", "wb")
    testCaseCount = 10000
    result = ""
    while testCaseCount > 0:
        board = [0,1,2,3,4,5,6,7,8]
        testCaseCount -= 1
        
        board = solution_RandomHillClimbing(board)
        
        for i in range(0,8): # i = 0 1 2 3 4 5 6 7
            result += str(board[i]) + ' '
        result += str(board[i+1]) + '\n' #! i+1=8
    print result
    f.write(result)
    f.close()
    
if __name__ == '__main__':
    main()