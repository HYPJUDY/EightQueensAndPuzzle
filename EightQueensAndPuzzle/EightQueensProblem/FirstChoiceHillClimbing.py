'''
@author: HYPJUDY
'''
import time
import random

FAILED = False

# heuristic cost
def getCollisionNum(board):
    num = 0
    for col in range(len(board)):
        for anotherCol in range(col+1, len(board)):
            if board[col] == board[anotherCol]:
                num += 1 # collied in the same row
            elif abs(board[col] - board[anotherCol]) == (anotherCol - col):
                num += 1 # collied diagonally
    return num

# randomly select a point until it is 
# better than the original one
# change "better than" to "not worse than"
# can significantly increase the success rate
def step_FirstChoiceHillClimbing(board):
    collisionNum = getCollisionNum(board)
    maxRound = 1000 # the expected number to find a better choice
    count = 0
    while True:
        count += 1
        if(count >= maxRound):
            global FAILED
            FAILED = True
            return board
        randomRow = random.randint(0,len(board)-1)
        randomCol = random.randint(0,len(board)-1)
        if board[randomCol] == randomRow:
            continue
        originRow = board[randomCol]
        board[randomCol] = randomRow
        if getCollisionNum(board) <= collisionNum: # not worse than
            return board
        board[randomCol] = originRow
        

def solution_FirstChoiceHillClimbing(board):
    maxRound = 200 # the expected number to find a solution
    count = 0
    while True:
        collisionNum = getCollisionNum(board)
        if collisionNum == 0:
            return board
        board = step_FirstChoiceHillClimbing(board)
        global FAILED
        if FAILED:
            return board
        count += 1
        if(count >= maxRound):
            FAILED = True
            return board
    
def main():
    title = "EightQueens_FirstChoiceHillClimbing"
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
            board = solution_FirstChoiceHillClimbing(board)
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