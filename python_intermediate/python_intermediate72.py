Example: Write to Files
Suppose a file named python.txt doesn't exist. Let's see what will happen if we write contents to a python.txt file.

with open('python.txt', 'w') as f:

    # write contents to the python.txt file
    f.write('Python is awesome')
    f.write('I love Python')
Since python.txt didn't previously exist, this code creates the python.txt file. And, it's content will be the contents we specified inside the write() method.

If we run the above code, this file is created.

Writing to Files in Python
Figure: Writing to Files in Python
By the way, we can easily add contents in new lines by using the new line character, \n.

with open('python.txt', 'w') as f:
    f.write("I like Python.\n")
    f.write("Files is easy.")
Now let's see what will happen if we run this code.

Writing to Files in Python
Figure: Writing to a File
Since the python.txt file previously existed, this code erases all the contents of the file and new content was written to the python.txt file.

Idea Emoji
Important: We need to be careful when working with files in writing mode because we may accidentally erase old data without realizing.
Confused about something? Ask a question!
