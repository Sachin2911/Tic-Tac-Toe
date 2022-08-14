#imports
import time
import os
import random

#Creates game grid
def grid_Drawer(input):
    
    print("1  {} | {} | {}".format(input["A1"],input["B1"],input["C1"]))
    print("-------------")
    print("2  {} | {} | {}".format(input["A2"],input["B2"],input["C2"]))
    print("-------------")
    print("3  {} | {} | {}".format(input["A3"],input["B3"],input["C3"]))
    print("   A   B   C")

def start_prompt():
    print("Hi there I a Tic-Tac-Toe bot!!")
    if input("Do you want to play Yes/No \n") == "Yes":
        if random.randint(1,2) == 1:
            print("I will play first")
            ticker()
            return "Bot"
        if random.randint(1,2) == 2:
            print("You will play first")
            ticker()
            return "Player"
    else: exit()

def ticker():
    print("Tic...")
    time.sleep(1)
    print("Tac...")
    time.sleep(1)
    print("Toe...")
    
def botMove(values):
    print("I moved")
    
def playerMove(values):
    input("Enter move")
        
    