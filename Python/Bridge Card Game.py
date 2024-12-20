# -*- coding: utf-8 -*-
"""
Randomly generates a hand of a bridge game and the points acumulated
by each player. It shows the cards in organized matter which suit each 
card is from.

CSC130 PROGRAMMING ASSIGNMENT # 5 Fall 2023

By Ginnie 

"""

import random  

def ITOTAL(hand,length):
    point=0
    for i in range (length):             
        if hand[i] % 13 == 0:
            point = point + 4
        elif ((hand[i]+1) % 13) == 0: 
            point = point + 3 
        elif ((hand[i]+2) % 13) == 0:
            point = point + 2
        elif ((hand[i]+3) % 13) == 0:
            point = point + 1
    return point

            
def SHOW(hand, points):
    print("    SPADES")
    for i in hand: 
        if i >= 1 and i <= 13:
            if i == 13:
                print("    A")
            elif i == 12:
                print("    K")
            elif i == 11: 
                print("    Q")
            elif i == 10:
                print("    J")
            else:
                print("    " + str(i+1))
    print("    HEARTS") 
    for i in hand: 
        if i >= 14 and i <= 26: 
            if i == 26:  
                print("    A")
            elif i == 25:
                print("    K")
            elif i == 24: 
                print("    Q")
            elif i == 23:
                print("    J")
            else:
                print("    "+str((i-13)+1))
    print("    DIAMONDS")
    for i in hand: 
        if i >= 27 and i <= 39:
            if i == 39:
                print("    A")
            elif i == 38:
                print("    K")
            elif i == 37: 
                print("    Q")
            elif i == 36:
                print("    J")
            else:
                print("    "+str((i-26)+1))  
    print("    CLUBS")
    for i in hand: 
        if i >= 40 and i <= 52:
            if i == 52:
                print("    A")
            elif i == 51:
                print("    K")
            elif i == 50: 
                print("    Q")
            elif i == 49:
                print("    J")
            else:
                print("    "+str((i-39)+1)) 
    print("NUMBER OF POINTS: ", points)
    return ""
                    

#creates deck
deck = [i for i in range(1,53)]

#shuffles deck

for i in range(0,3):
    random.shuffle(deck)

#creates players list

North = []
East = []
South = []
West = []

#Deals the deck

for i in deck:
    if (deck.index(i)+4)%4 == 0:
        North.append(i) 
    elif(deck.index(i)+3)%4 == 0:
        East.append(i)
    elif (deck.index(i)+2)%4 == 0:
        South.append(i)
    elif (deck.index(i)+1)%4 == 0:
        West.append(i)

#sorts each hand

North.sort() 
East.sort()
South.sort()
West.sort()

#displays earch hand    

print("WEST")
SHOW(West,ITOTAL(West,len(West)))
print(" ")
print("NORTH")
SHOW(North,ITOTAL(North,len(North)))
print(" ")
print("EAST")
SHOW(East,ITOTAL(East,len(East)))
print(" ")
print("SOUTH")
SHOW(South,ITOTAL(South,len(South)))