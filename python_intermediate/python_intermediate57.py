Example: Add Two Distances (feet-inch System)
In this example, we will add two distances (in feet-inch) using object-oriented programming.

If you don't know,

1 feet = 12 inches
Source Code
class Distance:
    # initialize feet and inches attributes
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    def add_distances(self, distance):
        result_inches = self.inches + distance.inches
        result_feet = self.feet + distance.feet
        
        # while inch is 12 or greater,
        # increase feet by 1 and decrease inches by 12
        while (result_inches >= 12):
            result_feet = result_feet + 1
            result_inches = result_inches - 12 
            
        # create an object of Distance
        result_distance = Distance(result_feet, result_inches)
        return result_distance
        
# create distance1 object
distance1 = Distance(12, 8)

# create distance2 object
distance2 = Distance(10, 6)

# call add_distances using distance1 object
# distance2 is used as argument
result = distance1.add_distances(distance2)
print(f'Result distance: {result.feet} ft {result.inches} inches')
Output

Result distance: 23 ft 2 inches
When the distance1 object is created, its feet attribute will be 12 and the inches attribute will be 8.

Similarly, the feet attribute of distance2 is 10 and its inches attribute is 6.

Then, we have called the add_distances() method using distance1 object with distance2 as argument.

result = distance1.add_distances(distance2)
Inside the add_distances() method definition, self will be distance1 and distance will be distance2. Then, we have added feet and inches of these two distances separately. And, if inches is 12 or greater, we have converted it to feet.

# Inside add_distances()
result_inches = self.inches + distance.inches
result_feet = self.feet + distance.feet

while (result_inches >= 12):
    result_feet = result_feet + 1
    result_inches = result_inches - 12
Then, we have created a new Distance object with feet attribute equal to result_feet and inches attribute equal to result_inches, and returned it.

# Inside add_distances()
result_distance = Distance(result_feet, result_inches)
return result_distance
This object is assigned to the result variable outside of the class.

Idea Emoji
Reminder: Great job on completing this section! Now, practice what you've learned with the problems in Practice: Python Intermediate.
Confused about something? Ask a question!
