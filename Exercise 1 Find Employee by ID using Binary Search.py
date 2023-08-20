#Exercise 1: Find Employee by ID using Binary Search
"""
Create a list of Employee Objects each has a name, a
unique ID and salary (use an excel file to store and read
Employee info)

Sort the list in ascending order based on Employee IDs

Implement a binary search algorithm to find an Employee
object in the list based on its ID.

Hint: write and use the binary_search_employees
function that takes a sorted list of Employee objects and a
target employee ID as input and returns the Employee
object if found or None if not found.
"""

# Step 1: Create an Excel file (employee_info.xlsx) with columns: Name, ID, Salary
import pandas as pd
# Step 2: Read the Excel file and create Employee objects
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

def read_employee_info(file_path):
    employee_data = pd.read_excel(file_path)
    employee_list = []
    
    for index, row in employee_data.iterrows():
        employee = Employee(row['Name'], row['ID'], row['Salary'])
        employee_list.append(employee)
    
    return employee_list

# Step 3: Sort the list of Employee objects based on IDs
def sort_employee_list(employee_list):
    employee_list.sort(key=lambda emp: emp.emp_id)

# Step 4: Implement binary search to find an Employee by ID
def binary_search_employees(employee_list, target_id):
    left, right = 0, len(employee_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_id = employee_list[mid].emp_id
        
        if mid_id == target_id:
            return employee_list[mid]
        elif mid_id < target_id:
            left = mid + 1
        else:
            right = mid - 1
            
    return None

# Main program
if __name__ == "__main__":
    file_path = "employee_info.xlsx"
    employees = read_employee_info(file_path)
    sort_employee_list(employees)

    target_id = 101  # Change this to the desired employee ID to search for
    found_employee = binary_search_employees(employees, target_id)

    if found_employee:
        print(f"Employee found - Name: {found_employee.name}, ID: {found_employee.emp_id}, Salary: {found_employee.salary}")
    else:
        print("Employee not found.")