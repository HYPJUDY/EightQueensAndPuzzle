'''
@author: HYPJUDY
'''
import time
import random
import math

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

# accept the random choice with certain probability
def step_SimulatedAnnealing(board):
    temperature = len(board)**2
    annealingRate = 0.95
    while True:
        randomRow = random.randint(0,len(board)-1)
        randomCol = random.randint(0,len(board)-1)
        originCollisionNum = getCollisionNum(board)
        originRow = board[randomCol]
        board[randomCol] = randomRow
        newCollisionNum = getCollisionNum(board)
        temperature = max(temperature * annealingRate, 0.02)
        if newCollisionNum < originCollisionNum:
            return board
        else:
            deltaE = newCollisionNum - originCollisionNum
            acceptProbability = min(math.exp(deltaE / temperature), 1)
            if random.random() <= acceptProbability:
                return board
            else:
                board[randomCol] = originRow
    
    return board

def solution_SimulatedAnnealing(board):
    # the success rate will increase by increasing the maxRound
    maxRound = 500000
    count = 0
    while True:
        collisionNum = getCollisionNum(board)
        if collisionNum == 0:
            return board
        board = step_SimulatedAnnealing(board)
        count += 1
        if(count >= maxRound):
            global FAILED
            FAILED = True
            return board
    
def main():
    title = "EightQueens_SimulatedAnnealing"
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
            board = solution_SimulatedAnnealing(board)
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