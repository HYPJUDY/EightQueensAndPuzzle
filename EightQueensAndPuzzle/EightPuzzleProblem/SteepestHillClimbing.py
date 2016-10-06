'''
@author: HYPJUDY
'''
import random
import time

FAILED = False

# manhattan_distance
def getManhattanDistance(board):
    distance = 0
    for i in range(len(board)):
        distance += abs(i/3 - board[i]/3) + abs(i%3 - board[i]%3)
    return distance

# for each column, calculate the collision number
# if the queen is moved to the other rows
# find the smallest one and move to it.
def step_steepestHillClimbing(board):
    for i in range(len(board)):
        if board[i] == 0:
            break
    distanceBoard = {}
    if i >= 3:
        upBoard = list(board)
        upBoard[i] = board[i-3]
        upBoard[i-3] = 0
        distanceBoard[i-3] = getManhattanDistance(upBoard)
    if i < 6:
        downBoard = list(board)
        downBoard[i] = board[i+3]
        downBoard[i+3] = 0
        distanceBoard[i+3] = getManhattanDistance(downBoard)
    if i%3 != 0:
        leftBoard = list(board)
        leftBoard[i] = board[i-1]
        leftBoard[i-1] = 0
        distanceBoard[i-1] = getManhattanDistance(leftBoard)
    if (i+1)%3 != 0:
        rightBoard = list(board)
        rightBoard[i] = board[i+1]
        rightBoard[i+1] = 0
        distanceBoard[i+1] = getManhattanDistance(rightBoard)
    
    shortestDistance = getManhattanDistance(board)
    for point,value in distanceBoard.iteritems():
        # "<=" means "not worse than" situation
        # plain
        if value <= shortestDistance:
            shortestDistance = value
    
    shortestDistancePoints = []
    for point,value in distanceBoard.iteritems():
        if value == shortestDistance:
            shortestDistancePoints.append(point)
    
    # can not find a steeper move
    # we have come to the peek(local optimization)
    if len(shortestDistancePoints) == 0:
        # print "local optimization"
        global FAILED
        FAILED = True
        return board
    
    random.shuffle(shortestDistancePoints)
    board[i] = board[shortestDistancePoints[0]]
    board[shortestDistancePoints[0]]= 0
    return board

def solution_steepestHillClimbing(board):
    # For each case, there are only several situations using this solution.
    # In average, we will reach a local optimization within 100 steps
    # or fall into a infinite loop (a plain) within 100 steps.
    maxRound = 100
    count = 0
    while True:
        count += 1
        collisionNum = getManhattanDistance(board)
        # print count, collisionNum
        if collisionNum == 0:
            return board
        board = step_steepestHillClimbing(board)
        global FAILED
        if FAILED:
            return board
        if(count >= maxRound):
            # for i in range(0,len(board)):
            #     print board[i]
            FAILED = True
            return board
    
def main():
    title = "EightPuzzle_steepestHillClimbing"
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
            board = solution_steepestHillClimbing(board)
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
    # print result
    
    f = open(title + '.txt', 'w')
    f.write(result)
    f.close()
        
if __name__ == '__main__':
    main()