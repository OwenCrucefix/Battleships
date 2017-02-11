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
    spdtyping("  |A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|x\n",0.000001)
    x = 0
    for i in alphabet:
        x = x + 1
        y = x
        if x < 10:
            x = str(x) + " "
            spdtyping(str(x),0.000001)
        else:
            x = str(x)
            spdtyping(str(x),0.000001)
        for j in numbers:
            if i[str(j)] == "0":
                spdtyping("|*",0.000001)
            elif i[j] == "1":
                spdtyping("|x",0.000001)
            else:
                spdtyping("|0",0.000001)
        spdtyping("|\n",0.000001)
        x = y
    spdtyping("y\n",0.000001)


#Starts here
typing("Welcome to Battleships\n\n")
new_game()
board()

