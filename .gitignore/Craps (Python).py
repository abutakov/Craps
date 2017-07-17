'''
       TODO:
             1. Finish Save Option
                a) searching the file for existing names
                b) save name and balance if found
                
             2. Reset Winnings mode
             
             3. Finish up "playGame()" method
                a) do the proper loop
                b) do the "getch()" implementation for "r"

Project Name: Craps Game
      Course: CIT-287-S1 "OOPL for Java Programmers"
  Instructor: Arland J. Richmond
        Date: April 15, 2017
        
'''


import sys
import random
import msvcrt
import os.path
import time

balance = 1000
winnings = 0
username = 'test'
fname = 'data.txt'

def playGame():
    print('Playing the game...Press "R" to play')

    global balance
    global winnings
    
    gameWinnings = 0

    sum = rollDice()
    
    if sum == 2 or sum == 3 or sum == 12:
       
        winnings = winnings - 100
        print('\nYou lost!')
        print('\nYour new balance: ', '$', balance + winnings)
            
    elif sum == 7 or sum == 11:
        winnings = winnings + 100
        print('\nYou won!',)
        print('\nYour new balance: ', '$',  balance + winnings, '$')       
    else:
        print('Roll ', sum, ' to win!')
        sum2 = rollDice()
        while(sum2 != sum and sum2 != 7): 
            sum2 = rollDice()

        if sum2 == sum:
            winnings = winnings + 100
            print('You win!')
            print('\nYour new balance: ', '$', balance + winnings)
        else:
            winnings = winnings - 100
            print('You lose!')
            print('\nYour new balance: ', '$',  balance + winnings, '$') 
            
        if (balance + winnings) <= 0:
            print("You are out of funds. Bye!")
     
        
def rollDice():
    char = kbfunc()
    while char.decode() != 'r':
        print(char)
        char = kbfunc()
        
     # Rolling the Dice 
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)

    sum = num1 + num2
    print("Your 1st dice value - ", num1, ", ", "the 2nd dice value - ", num2, "\n")
    print("Your sum is: ", sum, " - Draw" if (sum != 2 and sum !=3 and sum != 12 and sum != 7 and sum != 11) else "")

    return sum 

def printMenu():
    print('\n     *     *     *')
    print()
    print('1.  Play the Game\n')
    print('2.  Display Available Funds\n')
    print('3.  Reset Winnings to Zero\n')
    print('4.  Save Name and Score\n')
    print('5.  Quit\n')

# C++ style getch() method, that refuses to work 
def kbfunc():
    #if the keyboard has been hit
    if not msvcrt.kbhit():
        #getch acquires the character encoded in binary ASCII
        ret = msvcrt.getch()
    else:
        ret = 'x'
    return ret

def isExistingUser(s):
    
    global balance
    isExist = False
    
    try:
        with open(fname) as file:
           for line in file:
                if s == line.rstrip('\n'):
                    balance = int(next(file))
                    isExist = True
                    
        if isExist:
            print("\nWelcome back, ", s, "!")
            print("Here is your last score: " , "$", balance)
        else:
            print("\nWelcome to Craps,", s, '!')
            print("Your starting balance is ", "$", balance)
           
    except IOError as e:
        print ("Unable to open file")
        
def saveUser():
    
    global balance

    isExist = False

    
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            for line in f:
                if username == line.strip():
                    isExist = True
                    

    except IOError as e:
        print("Unable to open file")


    try:
        file = open(fname, 'a')
        
        file.write(username)
        file.write('\n')
        file.write(str(balance + winnings))
        file.write('\n')
    finally:
        file.close()

    print("Saved!")


   
def main():
    global username
    global winnings

    counter = 0
    
    username = str(input("\nEnter your Name: "))

    isExistingUser(username)
    
    while True:

        printMenu()
        userchoice = -1
        userChoice = int(input("Choose your option: "))
        while userChoice < 1 and userChoice > 5:
                userChoice = int(input('Wrong option. Please, use numbers in the range [1-5]: '))
          
        print()

        #  Playing the Game Option
        if userChoice == 1:
          
            #char = input("Press 'r' to play...")
        
            #while char.lower() != 'r':
                #char = input("Press 'r' to play...")
                
            playGame()

        #2 Displaying Available Funds 
        elif userChoice == 2:
            print('\nAvailable Funds: ', balance + winnings, '$\n')
            
        #3 Reseting the Winnings 
        elif userChoice == 3:
            winnings = 0

        #4 Saving the Data 
        elif userChoice == 4:
            saveUser()
          
        #5 Quiting the Game 
        elif userChoice == 5:
            print('Quiting...')
            sys.exit(0)
        else:
            print ('Wrong option. Please user numbers in the range [1-5]: ')
            userChoice = int(input())
                     
        print('==============================================')
        
main()

    
    
