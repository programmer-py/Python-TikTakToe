import random
import time


reset = False
beginner = 0
field = list()
A1 = " "
A2 = " "
A3 = " "
B1 = " "
B2 = " "
B3 = " "
C1 = " "
C2 = " "
C3 = " "
availablefield = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
usedfield = list()
usedfieldplayer = list()

beginner = random.randint(1, 2)
print ("Instructions: Assign the fields to the program as follows: e.g. A1 or B2 or C2.")
print ("")
print ("Here is the example field:")

print (" " + " A " + "  B " + "  C ")
print ("1 " + A1 + " | " + B1 + " | " + C1 )
print ("2 " + A2 + " | " + B2 + " | " + C2 )
print ("3 " + A3 + " | " + B3 + " | " + C3 )

while reset == False:
    if beginner == 1:
        beginner = 2
    else:
        beginner = 1

    if beginner == 1:
        choice = input("Whitch field do you want to take? ")
        availablefield.remove(choice)
        usedfieldplayer.append(choice)
        if choice == "A1":
            A1 = "X"
        if choice == "A2":
            A2 = "X"
        if choice == "A3":
            A3 = "X"
        if choice == "B1":
            B1 = "X"
        if choice == "B2":
            B2 = "X"
        if choice == "B3":
            B3 = "X"   
        if choice == "C1":
            C1 = "X"
        if choice == "C2":
            C2 = "X"
        if choice == "C3":
            C3 = "X"
    elif beginner == 2:
        print ("The computer chooses...")
        time.sleep(random.randint(1, 2))
        computer_pick = random.choice(availablefield)
        availablefield.remove(computer_pick)
        usedfield.append(computer_pick)
        if computer_pick == "A1":
            A1 = "O"
        if computer_pick == "A2":
            A2 = "O"
        if computer_pick == "A3":
            A3 = "O"
        if computer_pick == "B1":
            B1 = "O"
        if computer_pick == "B2":
            B2 = "O"
        if computer_pick == "B3":
            B3 = "O"   
        if computer_pick == "C1":
            C1 = "O"
        if computer_pick == "C2":
            C2 = "O"
        if computer_pick == "C3":
            C3 = "O"
    
    print (" " + " A " + "  B " + "  C ")
    print ("1 " + A1 + " | " + B1 + " | " + C1 )
    print ("2 " + A2 + " | " + B2 + " | " + C2 )
    print ("3 " + A3 + " | " + B3 + " | " + C3 )


    #player check


    if "A1" in usedfieldplayer and "A2" in usedfieldplayer and "A3" in usedfieldplayer:
        print ()
        print ("You won the game. \nYou are a very very good player. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if "A1" in usedfieldplayer and "B1" in usedfieldplayer and "C1" in usedfieldplayer:
        print ()
        print ("You won the game. \nYou are a very very good player. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)
    
    if "A1" in usedfieldplayer and "B2" in usedfieldplayer and "C3" in usedfieldplayer:
        print ()
        print ("You won the game. \nYou are a very very good player. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if "B1" in usedfieldplayer and "B2" in usedfieldplayer and "B3" in usedfieldplayer:
        print ()
        print ("You won the game. \nYou are a very very good player. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if "C1" in usedfieldplayer and "C2" in usedfieldplayer and "C3" in usedfieldplayer:
        print ()
        print ("You won the game. \nYou are a very very good player. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if "A3" in usedfieldplayer and "B3" in usedfieldplayer and "C3" in usedfieldplayer:
        print ()
        print ("You won the game. \nYou are a very very good player. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if "C1" in usedfieldplayer and "B2" in usedfieldplayer and "A3" in usedfieldplayer:
        print ()
        print ("You won the game. \nYou are a very very good player. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)





#computer check




    if "A1" in usedfield and "A2" in usedfield and "A3" in usedfield:
        print ()
        print ("The computer won the game. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if "A1" in usedfield and "B1" in usedfield and "C1" in usedfield:
        print ()
        print ("The computer won the game. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)
    
    if "A1" in usedfield and "B2" in usedfield and "C3" in usedfield:
        print ()
        print ("The computer won the game. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if "B1" in usedfield and "B2" in usedfield and "B3" in usedfield:
        print ()
        print ("The computer won the game. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if "C1" in usedfield and "C2" in usedfield and "C3" in usedfield:
        print ()
        print ("The computer won the game. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if "A3" in usedfield and "B3" in usedfield and "C3" in usedfield:
        print ()
        print ("The computer won the game. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if "C1" in usedfield and "B2" in usedfield and "A3" in usedfield:
        print ()
        print ("The computer won the game. \nTo restart the game quit it and start it again.")
        reset = True
        time.sleep(3)

    if len(availablefield) == 0 and reset == False:
        print ("Its draw! Nobody won.")
