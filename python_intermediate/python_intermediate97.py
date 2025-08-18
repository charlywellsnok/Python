Step 3: Get user's Pick
Project Changes
Added the user_pick attribute inside the __init__() class
Added the get_user_pick method
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
        user_pick = input('Enter rock/paper/scissors: ')

        # converting the user's pick to lowercase and returned it
        return user_pick.lower()
Inside the __init__() method

We have called the get_user_pick() to get input from the user which is assigned to the user_pick attribute.

Inside the get_user_pick() method

The user is asked to enter a string. This string is converted to lowercase using the lower() method and we have returned the string.

Idea Emoji
Note: We have converted the string to lowercase so that we can compare it with the computer_pick which contains either 'rock', 'paper' or 'scissors' (in the lowercase).
If the user enters any other string other than 'rock', 'paper' or 'scissors', we cannot compare it properly with the computer's pick.

To solve this issue, let's modify the get_user_pick() method so that the user is asked to enter input again and again until the user enters a valid string.

Confused about something? Ask a question!
