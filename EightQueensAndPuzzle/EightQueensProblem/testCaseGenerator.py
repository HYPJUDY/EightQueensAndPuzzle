import random

def main():
    f = open("eightQueensTest.txt", "wb")
    testCaseCount = 1000
    board = ""
    while testCaseCount > 0:
        testCaseCount -= 1
        for col in range(0,7):
            board += str(random.randint(0,7)) + ' '
        board += str(random.randint(0,7)) + '\n'
    f.write(board)
    f.close()
    
if __name__ == '__main__':
    main()