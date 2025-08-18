Lesson
Ask Programiz
Make a New Directory
We can create a new directory using the mkdir() method of the os module.

import os
os.mkdir('test')
This code creates a new directory named test in the current directory.

Creating a New Directory in a Specified Path
import os

# change current working directory
os.chdir('D:/Projects')

os.mkdir('test')
Here, we have changed the current working directory to D:/Projects before creating the folder. Hence, this code creates a directory named test inside the Projects directory (which is located

inside the D drive).

By the way, mkdir means make directory.

Confused about something? Ask a question!
