import numpy, sys, random

def quit():
    print("Ok, bye bye")
    sys.exit(0)


def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


def rand():
    flip = ["Heads", "Tails"]
    print("Players, choose Heads or Tails.")
    cont = input("Press enter to continue")
    return "The one who chose {} will go first".format(random.choice(flip))


def win(end_state, pi, pj):
    listi = list()
    listj = list()
    for i in range(len(end_state)):
        sumj = 0
        for j in range(len(end_state[i])):
            sumj += end_state[i][j]
        listj.append(sumj)
    for j in range(len(end_state)):
        sumi = 0
        for i in range(len(end_state[j])):
            sumi += end_state[i][j]
        listi.append(sumi)
    print("The sums of the vertical lines are {} while the sums of the horizontal lines are {}\n".format(listi, listj))
    
    bubbleSort(listi)
    bubbleSort(listj)
    
    #maximum = 0
    maxpos = ''
    for i in range(3):
        if listi[i] > listj[i]:
            #maximum = listi[i]
            maxpos = 'i'
            
        elif listi[i] < listj[i]:
            #maximum = listj[i]
            maxpos = 'j'
    if maxpos == 'i':
        print("The player with vertical lines won\n")
        pi += 1
    else:
        print("The player with horizontal lines won\n")
        pj += 1
    main(pi, pj)


def printArray(args):
    print(" ".join(args))


def calc(numbers, board):
    print(("Choose a number from these {}").format(numbers))
    ans = int(input("> "))
    if ans not in numbers:
        print("You have already used this number")
        for row in board:
            printArray([str(x) for x in row])
        calc(numbers, board)
    print("Choose the x coordinate from 1 to 3")
    x = int(input("> "))
    print("And the y coordinate from 1 to 3")
    y = int(input("> "))
    numbers.remove(ans)
    if board[x - 1][y - 1] == 0:
        board[x - 1][y - 1] = ans
    else:
        print("You have already used this position")
        numbers.insert(ans - 1, ans)
        for row in board:
            printArray([str(x) for x in row])
        calc(numbers, board)
    for row in board:
        printArray([str(x) for x in row])
    if not numbers:
        return 0
              

def main(pi, pj):
    
    if pi != 0 or pj != 0:
        print("The score is {}-{}".format(pi, pj))
        print("Would you like to play again?")
        ans = input("[y/n]: ")
    else:    
        print("Hello there. Do you wish to play?")
        ans = input("[y/n]: ")
    
    #print("The score is {}-{}".format(pi, pj)) 
    
    if ans == 'n':
        quit()
    #This is where the introduction will be
    
    og = [
        [0, 0, 0], 
        [0, 0, 0], 
        [0, 0, 0]
    ]
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    print("Do you want to choose or assign array at random?")
    ch = input("[c/r]: ")

    if ch == "r":
        print(rand())
    
    while True:
        i = calc(options, og)
        if i == 0:
            win(og, pi, pj)

pi = 0
pj = 0
main(pi, pj)
