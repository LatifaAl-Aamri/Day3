def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test case
def main():
    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    target_element = 50
    result_index = binary_search(ordered_list, target_element)

    if result_index != -1:
        print(f"Element {target_element} found at index {result_index}.")
    else:
        print(f"Element {target_element} not found in the list.")
main()