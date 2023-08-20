#Exercise: Sort List of Students by GPA using Insertion Sort
"""
You are given a list of students, each represented as a
dictionary with the following attributes: name, age, and gpa.
Your task is to sort the list of students based on their GPA
in descending order using the Insertion Sort algorithm.

Example of a student dictionary:

students = [

{"name": "Alice", "age": 20, "gpa": 3.9},

{"name": "Bob", "age": 22, "gpa": 3.7},

{"name": "Charlie", "age": 21, "gpa": 4.0},

{"name": "David", "age": 19, "gpa": 3.5},

]
"""




def insertion_sort_dictionry(arr,stype):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
    while j >= 0 and key[stype] > arr[j][stype]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key


# Test case

def main():
    
    students = [
        {"name": "Alice", "age": 20, "gpa": 3.9},
        {"name": "Bob", "age": 22, "gpa": 3.7},
        {"name": "Charlie", "age": 21, "gpa": 4.0},
        {"name": "David", "age": 19, "gpa": 3.5},
        ]
    
    print("Original students:")
    for student in students:
        print(student)
        
        
    print('-------------------')
    
    
    insertion_sort_dictionry(students, "name")
    print("Sorted dictionary:", students)

main()





