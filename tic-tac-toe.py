def clear():
    print("\n"*100)

def choice():
    global r
    import random
    r = random.randint(0,1)
    if r==0:
        print ("Player 1 is 'X' and Player 2 is 'O'")
    else:
        print("Player 1 is 'O' and Player 2 is 'X'")
    print("'X' starts first\n")

def ask():
    print("-------------------------------------------------------")
    c = int(input("1. New Game   2.Exit\n"))
    if c == 1:
        clear()
        start()
    else:
        print("Exiting.......")
        exit(0)


def winner(memory):
    global r


    if {1,2,3}.issubset(memory) or {4,5,6}.issubset(memory) or {7,8,9}.issubset(memory) or {1,5,9}.issubset(memory) or {3,5,7}.issubset(memory) or {1,4,7}.issubset(memory) or {2,5,8}.issubset(memory) or {3,6,9}.issubset(memory):
        if r==0:
            print("Player 1 wins!!")
        else:
            print("Player 2 wins!!")
        ask()

    if {-1, -2, -3}.issubset(memory) or {-4, -5, -6}.issubset(memory) or {-7,-8, -9}.issubset(memory) or {-1, -5, -9}.issubset(memory) or {-3, -5, -7}.issubset(memory) or {-1, -4, -7}.issubset(memory) or {-2, -5, -8}.issubset(memory) or {-3, -6,-9}.issubset(memory):
        if r==0:
            print("Player 2 wins!!")
        else:
            print("Player 1 wins!!")
        ask()

    if (len(memoryX)==10):
        print("Its a Draw!!")
        ask()
    player_input()


def game(num):
        global memoryX
        memoryX.add(num)


        if {1,2,3,-1,-2,-3}.intersection(memoryX):
                if 1 in memoryX:
                    print("  X  |",end="")
                elif -1 in memoryX:
                    print("  O  |",end="")
                else:
                    print("     |",end="")

                if 2 in memoryX:
                    print("  X  |", end="")
                elif -2 in memoryX:
                    print("  O  |", end="")
                else:
                    print("     |", end="")

                if 3 in memoryX:
                    print("  X  ")
                elif -3 in memoryX:
                    print("  O  ")
                else:
                    print("     ")
        else:
            print("     |     |")


        print("-----------------")

        if {4,5,6,-4,-5,-6}.intersection(memoryX):
                if 4 in memoryX:
                    print("  X  |", end="")
                elif -4 in memoryX:
                    print("  O  |", end="")
                else:
                    print("     |", end="")

                if 5 in memoryX:
                    print("  X  |",end="")
                elif -5 in memoryX:
                    print("  O  |",end="")
                else:
                    print("     |",end="")

                if 6 in memoryX:
                    print("  X  ")
                elif -6 in memoryX:
                    print("  O  ")
                else:
                    print("     ")

        else:
            print("     |     |")

        print("-----------------")

        if {7,8,9,-7,-8,-9}.intersection(memoryX):
            if 7 in memoryX:
                print("  X  |", end="")
            elif -7 in memoryX:
                print("  O  |", end="")
            else:
                print("     |", end="")

            if 8 in memoryX:
                print("  X  |", end="")
            elif -8 in memoryX:
                print("  O  |", end="")
            else:
                print("     |", end="")

            if 9 in memoryX:
                print("  X  ")
            elif -9 in memoryX:
                print("  O  ")
            else:
                print("     ")
        else:
            print("     |     |")

        winner(memoryX)


def display_board(num):
    global is_avail
    global count

    for i in is_avail:
        if num==0:
            break
        if i==num:
            print("Postion alreay taken, try again...")
            player_input()

    if num!=0:
        is_avail.append(num)

    count+=1

    if count%2==0:
        game(num)
    else:
        game(-num)


def player_input():
    global r
    if (count%2==0 and r==0) or (count%2!=0 and r==1):
        print("")
        print("---------------Player 2 move---------------")
    elif (count%2==0 and r==1) or (count%2!=0 and r==0):
        print("")
        print("---------------Player 1 move---------------")
    position = int(input("Position : "))
    if not(position in range(1,10)):
        print("Invalid Input, try again...")
        player_input()
    display_board(position)

def start():
    global count
    global is_avail
    global memoryX

    memoryX = set()
    count = -2
    is_avail = [686]
    choice()
    display_board(0)


start()







