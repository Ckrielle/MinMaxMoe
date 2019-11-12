import sys, random, json

def quit():
    print("Ok, bye bye")
    sys.exit(0)


"""def bubbleSort(arr):
   
    for i in range(len(arr)):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
"""

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
    
    listi.sort()
    listj.sort()
    
    maxpos = ''
    for i in range(3):
        if listi[i] > listj[i]:
            maxpos = 'i'
            
        elif listi[i] < listj[i]:
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
    
    coordinates = {
        "1": [1, 1],
        "2": [1, 2],
        "3": [1, 3],
        "4": [2, 1],
        "5": [2, 2],
        "6": [2, 3],
        "7": [3, 1],
        "8": [3, 2],
        "9": [3, 3],
    }
    
    print(("Choose a number from these {}").format(numbers))
    ans = int(input("> "))
    
    if ans not in numbers:
        print("You have already used this number")
        for row in board:
            printArray([str(x) for x in row])
        calc(numbers, board)
    
    #print(json.dumps(coordinates.keys()))
    print("Choose one of these positions: " + ','.join([k for k in coordinates.keys()]))
    point = input("> ")
    """print("Choose the x coordinate from 1 to 3")
    x = int(input("> "))
    
    print("And the y coordinate from 1 to 3")
    y = int(input("> "))"""
    print(coordinates[point]) 
    numbers.remove(ans)
    
    x, y = coordinates[point]
    
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

"""def generator(n, m):
    
    og = list()
    for i in range(n):
        for j in range(m):
            og.append(0)
    
    return og"""


def main(pi, pj):
    
    if pi != 0 or pj != 0:
        print("The score is {}-{}".format(pi, pj))
        print("Would you like to play again?")
        ans = input("[y/n]: ")
    else:    
        print("Hello there. Do you wish to play?")
        ans = input("[y/n]: ")
    
    if ans == 'n':
        quit()
        
    print("""The rules are simple. Two players are assigned either the vertical or 
        the horizontal arrays of a 3x3 grid and choose a number from 1-9 to place
        in the grid. Once all numbers have been placed, the sum of all horizontal and 
        vertical arrays is counted, and the player with the highest sum wins.\n""")
        
    n, m = map(int, input("Enter the grids dimensions: ").split(" "))
    og = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0],
     ]#generator(n, m)
    options = [int(x) for x in range(1, (n * m) + 1)]
    
    print("Should the players choose the order and arrays or should the programm assign them at random?")
    ch = input("[c/r]: ")

    if ch == "r":
        print(rand())
    
    input("Press any key to continue")

    while True:
        i = calc(options, og)
        if i == 0:
            win(og, pi, pj)

main(0, 0)
