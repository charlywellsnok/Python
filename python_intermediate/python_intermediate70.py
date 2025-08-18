try...finally in Files
We should always remember to close the file after we use it. So, it's considered a good practice to use the try...finally statement when working with files.

In the finally block, we will put the code to close the file. It's because the finally block is always executed, and the file is closed even if an exception occurs.

try:
    f = open('message.txt', 'r')
    content = f.read()
    print(content)

finally:
    # close the file
    f.close()
There is a better way to write the above code using the with...open syntax. Here's how:

with open('message.txt', 'r') as f:
    content = f.read()
    print(content)
The file is automatically closed if we use this syntax to work with files.

Idea Emoji
Remember: Make a habit of using with..open syntax when working with files so that you don't have to worry about closing the file.
Confused about something? Ask a question!
