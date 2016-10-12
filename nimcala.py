import time


DEFAULT = "333333"

def validateUserBoard(inputBoard):
    if len(inputBoard)==6:
        if inputBoard.isdigit():
            return True
    else:
        return False

def createBoard(inputBoard):
    board = (tuple(int(pit) for pit in inputBoard))
    return board

def factorMove(moves):
    if moves%2 == 1:
        turn = False
        multiplier = 1
    else:
        turn = True
        multiplier = -1
    return multiplier, turn

def winOrLose(score):
    if score > 0:
        return "Hey bud, looks like you're gonna win!!"
    else:
        return "Sorry bud, looks like you're gonna lose!!"

def gameOver(inputBoard):
    for value in inputBoard:
        if value > 0:
            return False
    return True

def nextBoard(inputBoard, pit):
    if inputBoard[pit] == 0:
        return None
    value = inputBoard[pit]
    newNimBoard = []
    for step in range(len(inputBoard)):
        newNimBoard.append(inputBoard[step])
    newNimBoard[pit] = 0
    newPit = pit + 1
    while (value > 0) and (newPit < len(inputBoard)):
        newNimBoard[newPit] += 1
        newPit = newPit + 1
        value = value - 1
    return newNimBoard

def bestMove(nimBoard, moves):
    multiplier,turn = factorMove(moves)
    if gameOver(nimBoard):
        return (-1,(100-moves)*multiplier)
    if turn:
        pit = -123
        score = -1234
        for step in range(len(nimBoard)):
            if nimBoard[step] > 0:
                newBoard = nextBoard(nimBoard, step)
                pos,solution = bestMove(newBoard,moves+1)
                if solution > score:
                    score = solution
                    pit = step
    else:
        pit = -123
        score = 1234
        for step in  range(len(nimBoard)):
            if nimBoard[step] > 0:
                newBoard = nextBoard(nimBoard, step)
                pos,solution = bestMove(newBoard, moves+1)
                if score > solution:
                    score = solution
                    pit = step
    return pit+1,score
        
def main():
    userChoice = "Y"
    while (userChoice != "n" and userChoice !="N"):
        
        userBoard = DEFAULT
        userBoard = input("Enter the state of current board ")
        if not validateUserBoard(userBoard):
            print("Wrong board state entered!!")
        else:        
            nimBoard = createBoard(userBoard)         
            startTime = time.time()
            pit,score = bestMove(nimBoard, 0)
            endTime = time.time()
            outcome = winOrLose(score)
            print("Pick the stones in pit "+str(pit))
            print(outcome)
            print("Best next move found in "+str(endTime - startTime)+" seconds")
            print(" ")
        userChoice = input("Try again? (Y)es/(N)o: ")
    


main()
