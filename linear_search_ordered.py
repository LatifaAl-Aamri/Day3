def linear_search_ordered(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        elif arr[i] > target:
            break
    return -1
def linear_search_unordered(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test case
def main():
    ordered_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    target_element = 50
    result_index = linear_search_ordered(ordered_list, target_element)

    if result_index != -1:
        print(f"Element {target_element} found at index {result_index}.")
    else:
        print(f"Element {target_element} not found in the list.")
main()