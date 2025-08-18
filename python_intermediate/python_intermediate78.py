List All Directories and Files
We can list all files and subdirectories inside a directory by using the listdir() method of the os module. For example,

import os
print(os.listdir())
This code returns a list of all the files and subdirectories in the current working directory.

Sample Output

['external', 'main.py']
Get Files and Directories of a Specific Path
We can get files and directories of a specific location by passing the path argument inside the listdir() method. For example,

import os
print(os.listdir('D:/Projects'))
Sample Output

[Scraper, test.js, GoogleDocsAPI]
The above code lists all the files and directories located inside D:/Projects.

By the way, listdir means list directories.

Confused about something? Ask a question!
