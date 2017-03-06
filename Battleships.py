import time
import random
import sys
run_program = True

#Typing functions, thanks to Finlay Haggar for those
def typing(string): 
    for c in string: 
        sys.stdout.write(c) 
        sys.stdout.flush() 
        time.sleep(0.03) 

    
def spdtyping(string,speed):
    for c in string: 
        sys.stdout.write(c) 
        sys.stdout.flush() 
        time.sleep(speed)

#Assigns each space with it's value
def new_game():
    global spaces
    spaces = {"A":{},"B":{},"C":{},"D":{},"E":{},"F":{},"G":{},"H":{},"I":{},"J":{},"K":{},"L":{},"M":{},"N":{},"O":{},"P":{},"Q":{},"R":{},"S":{},"T":{},"U":{},"V":{},"W":{},"X":{},"Y":{},"Z":{}}
 #   global A
  #  global B
   # global C    #Is there any more efficient way of doing this, as everything I've tried doesn't work
    #global D
    #global E
    #global F
    #global G
   # global H
   # global I
  #  global J
 #   global K
#    global L
#    global M
 #   global N
  #  global O
   # global P
    #global Q
    #global R
   # global S
  #  global T
  #  global U
   # global V
  #  global W
 #   global X
#    global Y
#    global Z
#    A = {}
 #   B = {}
  #  C = {}
  #  D = {}
 #   E = {}
#    F = {}
 #   G = {}
  #  H = {}
   # I = {}
   # J = {}
  #  K = {}
 #   L = {}
#    M = {}
#    N = {}
 #   O = {}
  #  P = {}
   # Q = {}
  #  R = {}
  #  S = {}
   # T = {}
    #U = {}
    #V = {}
   # W = {}
  #  X = {}
 #   Y = {}
#    Z = {}
    global alphabet
    global numbers
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
    for i in alphabet:
        num = 0
        while num != 26:
            num = num +1
            spaces[i][str(num)] = "0"
    
   #The user selects their gamemode
    global gamemode
    global name1
    global name2
    spdtyping("What gamemode would you like to play?\nType 1 for 1 Player versus AI or type 2 for 2 player versus.\n",0.01)
    gamemode = raw_input("")
    if gamemode == "1":
        spdtyping("What is your name?/n",0.01)
        name1 = raw_input("")
    elif gamemode == "2":
        spdtyping("What is Player 1's name?",0.01)
        name1 = raw_input("")
        spdtyping("What is Player 2's name?",0.01)
        name2 = raw_input("")
    

#Generates the board based on the values of each space           
def board():
    spdtyping("  |A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|x\n",0.00000001)
    x = 0
    for i in numbers :
        x = x + 1
        y = x
        if x < 10:
            x = str(x) + " "
            spdtyping(str(x),0.00000001)
        else:
            x = str(x)
            spdtyping(str(x),0.00000001)
        for j in alphabet:
            if spaces[j][str(i)] == "0":
                spdtyping("|*",0.00000001)
            elif spaces[j][i] == "1":
                spdtyping("|x",0.00000001)
            else:
                spdtyping("|0",0.00000001)
        spdtyping("|\n",0.00000001)
        x = y
    spdtyping("y\n",0.00000001)
#A single attack
def attack():
    attack = True
    while attack == True:
        set_new = raw_input("What space do you want to attack? ").upper()
        attack = False
        set_new2 = set_new[1:3]
        if len(set_new) < 2 or len(set_new) > 3:
            spdtyping("You have not input a square (format xy)\n",0.001)
            attack = True
        else:
            
            if set_new[0] not in alphabet:
                spdtyping("You have not input a square (format xy)\n",0.001)
                attack = True

            
            elif set_new2 not in numbers:
                spdtyping("You have not input a square (format xy)\n",0.001)
                attack = True
            elif spaces[set_new[0]][set_new2] != "0":
                spdtyping("You have already attacked this space\n",0.001)
                attack = True
    
    spaces[set_new[0]][set_new2] = "1"
    board()

#Starts here
while run_program == True:
    typing("Welcome to Battleships\n")
    new_game()
    board()
    attack()

    again_try = True
    while again_try == True:
        spdtyping("Would you like to play again? (y/n) ",0.01)
        again = raw_input("").lower()
        if again == "y":
            again_try = False
        elif again == "n":
            again_try = False
            run_program = False
        else:
            spdtyping("You have input an invalid value. (y or n only)\n",0.001)

