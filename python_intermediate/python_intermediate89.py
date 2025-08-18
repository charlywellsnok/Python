Adding Python Code
Now, let's add code inside our Python files.

Inside player.py:

def get_player_info():
    print('I am the main player.')
Inside boss.py:

def get_boss_info():
    print('I am the enemy player.')
We have added simple functions to illustrate Python packages. However, while developing large programs, these modules might contain classes and multiple functions.

Importing Modules Inside a Package
Now, let's access the modules inside the game package from the main.py file (this file exists outside of the game directory). Let's access the player module first.

# importing the player module
import game.characters.player as p1

# call get_player_info()
p1.get_player_info()
Output

I am the main player.
Here is how this code works:

1. import game.characters.player as p1

This code imports the player module and renamed it to p1. Since this module lies inside packages, we also have to specify the path to the module.

2. p1.get_player_info()

Then, we have called the get_player_info() function of the player module using this code.

We can import the boss module in a similar way.

Confused about something? Ask a question!
