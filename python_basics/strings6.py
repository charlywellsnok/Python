String Methods
Python offers many useful methods that make it really easy to work with strings. Let's try a few of them.

The replace() method
The replace() method replaces a specified substring with another specified substring.

text = "bat ball"

# replace "ba" with "ca"
replaced_text = text.replace("ba", "ca")

print(replaced_text)    # cat call
The find() method
The find() method returns the index of the first occurrence of the substring. For example,

message = "Avengers"

# get the index of "nge"
print(message.find("nge"))   # 3
The upper() and lower() methods
The upper() method converts all the alphabets to uppercase. Similarly, the lower() method converts all the alphabets to lowercase.

message = "Python Is Fun"

result = message.lower()
print(result)   # python is fun

result = message.upper()
print(result)   # PYTHON IS FUN
