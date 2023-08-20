class Employee:
    def __init__(self, emp_id, name, age, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department

def binary_search_employees(employees, target_id):
    left, right = 0, len(employees) - 1

    while left <= right:
        mid = (left + right) // 2

        if employees[mid].emp_id == target_id:
            return employees[mid]
        elif employees[mid].emp_id < target_id:
            left = mid + 1
        else:
            right = mid - 1

    return None

# Test case
if __name__ == "__main__":
    employees = [
        Employee(101, "Alice", 30, "HR"),
        Employee(203, "Bob", 28, "IT"),
        Employee(305, "Charlie", 35, "Marketing"),
        Employee(408, "David", 25, "Finance"),
    ]

    target_id = 305
    result_employee = binary_search_employees(employees, target_id)

    if result_employee:
        print(f"Employee with ID {target_id} found:")
        print(f"Name: {result_employee.name}, Age: {result_employee.age}, Department: {result_employee.department}")
    else:
        print(f"Employee with ID {target_id} not found in the list.")
