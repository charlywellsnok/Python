Extending the Project
Running the game n times
Suppose we want to run our game 5 times. Here's how we can do that:

# putting object creation inside the loop
for i in range(5):
   game = Game()
   game.print_result()
Asking the user to play game again
Suppose we want to ask the user if they want to play the game again after a game is completed. Here's how we can do it.

# putting object creation inside the loop
while True:
   game = Game()
   game.print_result()

   play_again = input('Do you want to play again? (y/n): ')

   # if user enter any other character other than y, the game ends
   if play_again != 'y':
      break
Now, each time a game is completed, the user is asked whether they want to play the game again or not. If the user enters any other input other than y, the game is run again because of the infinite loop.

Confused about something? Ask a question!
