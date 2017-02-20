import time
import random
import sys

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
    global A
    global B
    global C    #Is there any more efficient way of doing this, as everything I've tried doesn't work
    global D
    global E
    global F
    global G
    global H
    global I
    global J
    global K
    global L
    global M
    global N
    global O
    global P
    global Q
    global R
    global S
    global T
    global U
    global V
    global W
    global X
    global Y
    global Z
    A = {}
    B = {}
    C = {}
    D = {}
    E = {}
    F = {}
    G = {}
    H = {}
    I = {}
    J = {}
    K = {}
    L = {}
    M = {}
    N = {}
    O = {}
    P = {}
    Q = {}
    R = {}
    S = {}
    T = {}
    U = {}
    V = {}
    W = {}
    X = {}
    Y = {}
    Z = {}
    global alphabet
    global numbers
    alphabet = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
    numbers = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
    for i in alphabet:
        num = 0
        while num != 26:
            num = num +1
            i[str(num)] = "0"
    

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
            if j[str(i)] == "0":
                spdtyping("|*",0.00000001)
            elif j[i] == "1":
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
        if len(set_new) < 2 or len(set_new) > 3:
            spdtyping("You have not input a square (format xy)\n",0.001)
            attack = True
        else:
            if set_new[0] == "A":
                set_new1 = A
            elif set_new[0] == "B":
                set_new1 = B
            elif set_new[0] == "C":
                set_new1 = C
            elif set_new[0] == "D":
                set_new1 = D
            elif set_new[0] == "E":
                set_new1 = E
            elif set_new[0] == "F":
                set_new1 = F
            elif set_new[0] == "G":
                set_new1 = G
            elif set_new[0] == "H":
                set_new1 = H
            elif set_new[0] == "I":
                set_new1 = I
            elif set_new[0] == "J":
                set_new1 = J
            elif set_new[0] == "K":
                set_new1 = K
            elif set_new[0] == "L":
                set_new1 = L
            elif set_new[0] == "M":
                set_new1 = M
            elif set_new[0] == "N":
                set_new1 = N
            elif set_new[0] == "O":
                set_new1 = O
            elif set_new[0] == "P":
                set_new1 = P
            elif set_new[0] == "Q":
                set_new1 = Q
            elif set_new[0] == "R":
                set_new1 = R
            elif set_new[0] == "S":
                set_new1 = S
            elif set_new[0] == "T":
                set_new1 = T
            elif set_new[0] == "U":
                set_new1 = U
            elif set_new[0] == "V":
                set_new1 = V
            elif set_new[0] == "W":
                set_new1 = W
            elif set_new[0] == "X":
                set_new1 = X
            elif set_new[0] == "Y":
                set_new1 = Y
            elif set_new[0] == "Z":
                set_new1 = Z
            else:
                spdtyping("You have not input a square (format xy)\n",0.001)
                attack = True

        set_new2 = set_new[1:3]
        if set_new2 not in numbers:
            spdtyping("You have not input a square (format xy)\n",0.001)
            attack = True
    
    set_new1[set_new2] = "1"
    board()
    
#Starts here
typing("Welcome to Battleships\n\n")
new_game()
board()
attack()

