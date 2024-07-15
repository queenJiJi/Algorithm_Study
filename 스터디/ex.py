arr1 = [(4, 0.5), (3, 0.5), (2, 0.42857142857142855), (1, 0.125), (5, 0.0)]
arr2 = [(4, 1.0), (3, 0.0), (2, 0.0), (1, 0.0)]

# Custom sort function
def custom_sort(arr):
    # Sort by x2 in descending order and then by x1 in ascending order
    return sorted(arr, key=lambda x: (-x[1], x[0]))

sorted_arr1 = custom_sort(arr1)
sorted_arr2 = custom_sort(arr2)

# Extract only the x1 values
result_arr1 = [x[0] for x in sorted_arr1]
result_arr2 = [x[0] for x in sorted_arr2]

print("Sorted arr1:", result_arr1)
print("Sorted arr2:", result_arr2)