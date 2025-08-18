Access Files Inside Different Folder
In our programs, we have directly used the file name inside the open() function. These programs work only if our Python file and the file we are trying to access are in the same folder (directory).

If we have to access an external file that exists in a different folder, we have to provide the directory name as well. Let's see an example.

Suppose we have a folder structure like this:

main.py
external
  - messages.txt
Here, the main.py file and the external folder are in the same folder, and the message.txt file is inside the external folder.

Now, if we have to access messages.txt file from main.py, we have to specify the path like this:

with open('external/messages.txt', 'r'):
    f.read()
Notice that we have used the folder name, external, followed by / before the file name to access the messages.txt file inside the external folder.

We will learn about this topic (directories) in detail in the next lesson.

Confused about something? Ask a question!
