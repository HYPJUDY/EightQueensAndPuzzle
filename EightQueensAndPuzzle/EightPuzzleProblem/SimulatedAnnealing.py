'''
@author: HYPJUDY
'''
import time
import random
import math

FAILED = False

# manhattan_distance
def getManhattanDistance(board):
    distance = 0
    for i in range(len(board)):
        distance += abs(i/3 - board[i]/3) + abs(i%3 - board[i]%3)
    return distance

# accept the random choice with certain probability
def step_SimulatedAnnealing(board):
    temperature = len(board)
    annealingRate = 0.95
    
    for i in range(len(board)):
        if board[i] == 0:
            break
    distance = getManhattanDistance(board)
    temperature = max(temperature * annealingRate, 0.02)
    while True:
        randCase = random.randint(0,4)
        if randCase == 0:
            if i >= 3:
                upBoard = list(board)
                upBoard[i] = board[i-3]
                upBoard[i-3] = 0
                if getManhattanDistance(upBoard) < distance:
                    return upBoard
                else:
                    deltaE = getManhattanDistance(upBoard) - distance
                    acceptProbability = min(math.exp(deltaE / temperature), 1)
                    if random.random() <= acceptProbability:
                        return upBoard
        elif randCase == 1:
            if i < 6:
                downBoard = list(board)
                downBoard[i] = board[i+3]
                downBoard[i+3] = 0
                if getManhattanDistance(downBoard) < distance:
                    return downBoard
                else:
                    deltaE = getManhattanDistance(downBoard) - distance
                    acceptProbability = min(math.exp(deltaE / temperature), 1)
                    if random.random() <= acceptProbability:
                        return downBoard
        elif randCase == 2:
            if i%3 != 0:
                leftBoard = list(board)
                leftBoard[i] = board[i-1]
                leftBoard[i-1] = 0
                if getManhattanDistance(leftBoard) < distance:
                    return leftBoard
                else:
                    deltaE = getManhattanDistance(leftBoard) - distance
                    acceptProbability = min(math.exp(deltaE / temperature), 1)
                    if random.random() <= acceptProbability:
                        return leftBoard
        else:    
            if (i+1)%3 != 0:
                rightBoard = list(board)
                rightBoard[i] = board[i+1]
                rightBoard[i+1] = 0
                if getManhattanDistance(rightBoard) < distance:
                    return rightBoard
                else:
                    deltaE = getManhattanDistance(rightBoard) - distance
                    acceptProbability = min(math.exp(deltaE / temperature), 1)
                    if random.random() <= acceptProbability:
                        return rightBoard
                    
    return board

def solution_SimulatedAnnealing(board):
    # the success rate will increase by increasing the maxRound
    maxRound = 500000
    count = 0
    while True:
        collisionNum = getManhattanDistance(board)
        if collisionNum == 0:
            print count
            return board
        board = step_SimulatedAnnealing(board)
        count += 1
        if(count >= maxRound):
            global FAILED
            FAILED = True
            return board
    
def main():
    title = "EightPuzzle_SimulatedAnnealing"
    startTime = time.clock()
    successCase = 0
    totalCase = 0
    result = title + " result:\n\n"
    with open("eightPuzzleTest.txt", "r") as ins:
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