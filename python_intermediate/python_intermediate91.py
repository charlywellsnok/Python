Use of __init__.py file
Now let's use the __init__.py file we previously created.

This is a special file that runs automatically when we import a package. Let's add a simple print statement inside the __init__.py file of the game directory.

print('Initializing game features')
Now, if we run the main.py file with this code:

# importing the player module
import game.characters.player as player

# call get_player_info()
player.get_player_info()
The __init__.py file is automatically executed. Then, the main.py file is executed.

Output

Initializing game features
I am the main player.
Confused about something? Ask a question!
