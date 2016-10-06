'''
@author: HYPJUDY
'''
import time
import random

FAILED = False

def getCollisionNum(board):
    num = 0
    for col in range(len(board)):
        for anotherCol in range(col+1, len(board)):
            if board[col] == board[anotherCol]:
                num += 1 # collied in the same row
            elif abs(board[col] - board[anotherCol]) == (anotherCol - col):
                num += 1 # collied diagonally
    return num


def step_RandomHillClimbing(board):
    while True:
        randomRow = random.randint(0,len(board)-1)
        randomCol = random.randint(0,len(board)-1)
        if board[randomCol] != randomRow:
            board[randomCol] = randomRow
            return board
    
    return board

def solution_RandomHillClimbing(board):
    maxRound = 500000
    count = 0
    while True:
        collisionNum = getCollisionNum(board)
        if collisionNum == 0:
            return board
        board = step_RandomHillClimbing(board)
        count += 1
        if(count >= maxRound):
            global FAILED
            FAILED = True
            return board
    
def main():
    title = "EightQueens_RandomHillClimbing"
    startTime = time.clock()
    successCase = 0
    totalCase = 0
    result = title + " result:\n\n"
    with open("eightQueensTest.txt", "r") as ins:
        for line in ins:
            print "case: ", totalCase
            global FAILED
            FAILED = False
            totalCase += 1
            board = []
            for col in line.split():
                board.append(int(col))
            board = solution_RandomHillClimbing(board)
            if FAILED:
                result += "Failed!"
            else:
                successCase += 1
                for col in range(len(board)):
                    result += str(board[col]) + " "
            result += "\n"
    
    endTime = time.clock()
    result += "\nTotal time: " + str(endTime - startTime) + '\n'
    result += "Total case number: " + str(totalCase) + ", Success case number: " + str(successCase) + '\n'
    result += "Success rate: " + str(successCase / float(totalCase)) + '\n'
    print result
    
    f = open(title + '.txt', 'w')
    f.write(result)
    f.close()
        
if __name__ == '__main__':
    main()