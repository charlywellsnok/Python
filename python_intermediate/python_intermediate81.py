Lesson
Ask Programiz
Deleting a Directory or a File
We can use the remove() method of the os module to remove a file.

import os

os.remove('hello.txt')
This code deletes the hello.txt file.

Similarly, we use the rmdir() method of the os module to remove a directory.

import os

os.rmdir('new')
This code removes the new directory we previously created. One thing we need to remember when removing a directory is that the directory must be empty. Otherwise, an exception will be raised.

By the way, rmdir means remove directory.

Confused about something? Ask a question!


main.py

Run



1
Output
Code Explanation


