Reading Content from a File
After we open a file, we can read its content using the read() method of the file object. Let's see an example.

# open a file
f = open('message.txt', 'r')


# read the file
content = f.read()
print(content)
After we have opened the file, we have used the file object, f, to call the read() method. Now, the contents of the file will be in the content variable.

Closing the file
After we perform a file operation, we should always close the file; it's a good programming practice.

To close the file, we use the close() method of the file object.

# open a file
f = open('message.txt', 'r')

# read the file
content = f.read()
print(content)


# close the file
f.close()
Now, if we run the code, we will get this output.

I love programming.
I love Programiz.
Reading contents from a file in Python
Figure: Reading File Content
Confused about something? Ask a question!
