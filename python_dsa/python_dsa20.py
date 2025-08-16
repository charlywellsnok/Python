Introduction
Sorting is the process of arranging elements in a particular order, most commonly either in ascending or descending order.

Sorting is one of the most frequently carried out tasks in computer programming.

Sorting is used in:

Data Analysis: To organize and analyze large datasets.
User Interfaces: To display items in systematic order, such as sorting files by name, date, or size.
Database Systems: To order records and perform faster search operations.
Algorithms Design: Some algorithms rely on input data being sorted.


How to Sort Data?
Suppose you have a list of numbers, as shown below:

numbers = [12, -4, 56, 67, 10]
You can quickly sort those elements using the list's sort() method.

numbers = [12, -4, 56, 67, 10]
numbers.sort()

print(numbers)
Output

[-4, 10, 12, 56, 67]




Different Sorting Algorithms
We will not use the sort() method to sort elements in this chapter. Instead, we will learn about the internal workings of different sorting algorithms.

Each algorithm offers different levels of efficiency, depending on the dataset and its use case.

We will cover the following sorting algorithms in this chapter:

Bubble Sort
Selection Sort
Insertion Sort
Merge Sort
Quick Sort
Counting Sort
The first three sorts in the above list are comparison-based sorting algorithms that work by comparing two elements and swapping them if necessary.

Next, we will learn about bubble sort.
