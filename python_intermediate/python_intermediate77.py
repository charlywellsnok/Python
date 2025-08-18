Changing Directory
As we know, Python thinks the current directory is the directory containing our Python file.

If we need to change the current working directory, we can use the chdir() method of the os module.

import os

# print current working directory
print('Before CWD =',os.getcwd())

# change current working directory
os.chdir('D:/Projects')

# print current working directory
print('After CWD =', os.getcwd())
Sample Output

Before CWD = c:\Users\lenovo\Desktop\Files
After CWD = D:\Projects
Before the current working directory was c:\Users\lenovo\Desktop\Files.

Then, we changed the current working directory to D:/Projects using this code:

os.chdir('D:/Projects')
Now, if we again print the current working directory, we get this new path.

Idea Emoji
Note: If we try to access a file after changing the directory, Python looks for the file in this new directory location.
By the way, chdir means change directory.

Confused about something? Ask a question!
