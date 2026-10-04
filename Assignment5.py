#Import random package
import random

#Start with the function
#Take prompt the user to play, validate their answer, and return it
def user_validation(): 
    #Use .lower() otherwise if user inserts a valid answer that is not lowercase they will be taken into the loop even though they are choosing a valid option
    #I have inserted \n because I want a separation between each new guess and previous information to make it more visual appealing
    user_choice = str(input('\nEnter your choice: rock, paper, scissors: ')).lower()
    #I used AI to learn how to compare if an element is contained in a list
    #From that I learn that I can used in/ not in
    while user_choice not in valid_choices :
        user_choice = input('Sorry, ' + '"' + user_choice + '" is not a valid choice. Please try again: ').lower()
    #Returns a valid input 
    return user_choice

#Determine the winner
def determine_winner(user_choice, computer_choice) :
    #There are many combinations so to make it easier just check for tie and win the rest means the user losses 
    if user_choice == computer_choice :
        return 'tie'
    elif (user_choice == 'paper') and (computer_choice == 'rock') :
        return 'win'
    elif (user_choice == 'rock') and (computer_choice == 'scissors') :
        return 'win'
    elif (user_choice == 'scissors') and (computer_choice == 'paper') :
        return 'win'
    else :
        return 'lose'
    
#--------------------------------------------------------------------------------------------------------------------
#END OF FUNCTIONS 
#--------------------------------------------------------------------------------------------------------------------

#Create a list of valid choices outside of the loop to make it a global variable instead of a local variable
valid_choices = ['rock', 'paper', 'scissors']

#Start the game and ask the user how many rounds they want to play
print('Welcome to the Rock Paper Scissors game!')
number_rounds = int(input('How many rounds would you like to play?: '))

#Take the user into a loop if they enter an even number of rounds
while number_rounds % 2 == 0 :
    number_rounds = int(input('Sorry the number must be an odd number. Please try again: '))

#Start game
#Create variable that keep track of tie, win, and lose
completed_rounds = 0
wins = 0
losses = 0
#Create a while loop accounting that tie rounds do not count towards the total number of rounds
#If it is tie than completed_rounds will not increase
while completed_rounds < number_rounds :
    #Call our function for user to insert their choice
    user_choice = user_validation() 
    #Create a random choice from rock, paper, scissors. I used AI to learn about the random.choice() function
    computer_choice = random.choice(valid_choices)
    #Call our function to determine who wins/loses
    result = determine_winner(user_choice, computer_choice)
    #Create a loop to increase the completed rounds if != tie and keep track of wins/loses
    if result == 'tie' :
        completed_rounds += 0
    elif result == 'win' :
        wins += 1
        completed_rounds += 1
    else :
      losses += 1  
      completed_rounds += 1
    #Print results. Add \n to keep gaps between printed results in the console
    print('\n'+ result)
    print('You chose: ' + user_choice)
    print('Computer chose: ' + computer_choice)

#Summary game
print('\nFINAL SCORES \n')
print(f'You scored {wins} and the computer scored {losses}')
#Wins and losses correspond to user only so if wins > losses that means user wins
if wins > losses :
    print('You win!!')
else :
    print('You lost :(\n')