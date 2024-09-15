# random function

import random


random_number = random.randrange(1,11)

a = 1 

print("\n YOU CAN ONLY GUESS 5 TIMES \n")
while a<=5:
    
   
    guess_number = int(input("Guess the number from 1 to 10: "))
    
    if guess_number == random_number:
        print(f"Congratulations !!! your guess is correct '{random_number}'")
        print(f"you have tried {a} times.")
        
        if(a==1):
            print("Score : 100")
        
        if(a==2):
            print("Score : 80")
            
        if(a==3):
            print("Score : 60")
        
        if(a==4):
            print("Score : 40")
            
        if(a==5):
            print("Score : 20")
        
      
    
    elif(guess_number<random_number):
        
        if(a == 5):
              print("You lose !!! You didn't guess the correct number")
        
        print(f"Your guess number is lesser than the correct number.")
        
        
    elif(guess_number > random_number and guess_number <=10):
        
        if(a == 5):
              print("You lose !!! You didn't guess the correct number")
              
        print(f"Your guess number is greater than the correct number ")
        
    else: print("Your number is invaild !!! please guess the number between 1 to 5") 
    a+=1
    
    
    
# Rock, paper, scissor

'''
while True:
   
    user_input = (input("Choose: rock, paper, scissor : " )).lower()
    
    while user_input not in ['rock', 'paper', 'scissor']: 
        print("Please choose correct given option!!!!! \n ")
        user_input = (input("Choose: rock, paper, scissor : " )).lower()
        
    computer_input = random.choice(['rock', 'paper', 'scissor'])
         
         
    if(user_input == computer_input):
        
        print(f"It's a tie, you both choose '{computer_input}'")
    
    elif(user_input == 'rock' and computer_input == 'scissor' ) or (user_input == 'paper' and computer_input == 'rock') or \
         (user_input == 'scissor' and computer_input == 'paper'):
             
             print(f"!! CONGRATULATIONS !! You win !!, your choice was: '{user_input}' and computer choice was: '{computer_input}'")
    
    else: print(f"YOU LOSE !!!!!!, computer choice was : '{computer_input}' and you choice was : '{user_input}'  ")


    
'''
