Opening a File
We use the built-in open() function to open files.

Suppose we have a file named message.txt with the following content.

A file on the computer.
Figure: A Computer File
Now let's open this file using the open() function.

f = open('message.txt')
If we run this code, a file object is created, which is assigned to the f variable. This file object is used to perform file operations such as reading content from the file and writing content to the file.

When we open a file like this, the file is opened in the read mode. Meaning, we can read contents from the file, however, we can't modify it.

We can also explicitly specify the mode by passing the second argument.

f = open('message.txt', 'r')
Here, 'r' means the file is opened for reading.

Confused about something? Ask a question!
