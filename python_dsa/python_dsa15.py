List pop()
The pop() method removes the item at the specified index. The method also returns the removed item.

prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print(f"Updated List: {prime_numbers}")
print(f"Removed Element: {removed_element}")
Output

Updated List: [2, 3, 7]
Removed Element: 5
If we do not pass any arguments to the pop() method, it removes the last element.

prime_numbers = [2, 3, 5, 7]

# remove the last item
prime_numbers.pop()

print(f"Updated List: {prime_numbers}")
Output

Updated List: [2, 3, 5]
