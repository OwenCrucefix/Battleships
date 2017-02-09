import time
import random
import sys

def typing(string): 
    for c in string: 
        sys.stdout.write(c) 
        sys.stdout.flush() 
        time.sleep(0.05) 
    print
    
def spdtyping(string,speed):
    for c in string: 
        sys.stdout.write(c) 
        sys.stdout.flush() 
        time.sleep(speed) 
    print

def board():
    spdtyping("  |A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|x",0.000001)
    x = 0
    while x !=26:
        x = x + 1
        y = x
        if x < 10:
            x = str(x) + " "
        spdtyping(str(x)+ "|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|",0.000001)
        x = y
    spdtyping("y",0.000001)

dicletter = 0
while dicletter != 26:
    dicletter = dicletter + 1
typing("Welcom to Battleships\n\n")

board()
    
