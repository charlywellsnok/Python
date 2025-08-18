Step 4: Make User Input a Valid String
Project Changes
Changed the get_user_pick() method to take valid input
import random

class Game:
    def __init__(self):
        # get the computer's pick 
        self.computer_pick = self.get_computer_pick()
        
        # get the user's pick
        self.user_pick = self.get_user_pick()

     
    
    def get_computer_pick(self):
        # get random number among 1, 2 and 3
        random_number = random.randint(1, 3)
        
        # possible options 
        options = {1: 'rock', 2: 'paper', 3: 'scissors'}
        
        # return the value present at random_number
        return options[random_number]

    def get_user_pick(self):
        
        # infinite while loop 
        while True:
            user_pick = input('Enter rock/paper/scissors: ')

            # convert to lowercase
            user_pick = user_pick.lower()

            # if user_pick is either rock or paper or scissors,
            # terminate the loop
            if user_pick in ('rock', 'paper', 'scissors'):
                  break
            else:
                print('Wrong input!') 

        return user_pick
Inside the get_user_pick() method

We have created an infinite while loop inside this method. Inside the loop, we have asked for user input and converted it to lowercase.

If this value is either 'rock' or 'paper' or 'scissors', the break statement terminates the loop. However, if the user input is invalid, the loop is again iterated and the user is again asked to enter the input.

Confused about something? Ask a question!
