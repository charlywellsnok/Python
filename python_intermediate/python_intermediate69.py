Reading Specific Number of Characters
We can pass an optional argument to the read() method specifying the number of characters we want to read.

Let's read the first 5 characters from the message.txt file.

f = open('message.txt', 'r')


# read the first 5 characters
content = f.read(5)

print(content)

f.close()
Output

I lov
Now, if we read the file again using the same file object, it starts reading the file from the 6th character.

f = open('message.txt', 'r')


# read the first 5 characters
content = f.read(5)

print(f'result1: {content}')


# read the next 13 characters
content = f.read(13)

print(f'result2: {content}')

f.close()
Output

result1: I lov
result2: e programming
Confused about something? Ask a question!
