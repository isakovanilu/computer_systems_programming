def check_if_array_is_sorted(arr_list):
    if arr_list == sorted(arr_list):
        print('The given array is sorted')
        return 1
    else:   
        print('The given array is not sorted')
        return 0
        
print(check_if_array_is_sorted([1,2,3,4,5]))
print('*****')
print(check_if_array_is_sorted([4,2,3,4,5]))

def max_value_in_array(arr_list):
    max_value = arr_list[0]

    for elem in range(1, len(arr_list)):
        if arr_list[elem] > max_value:
            max_value = arr_list[elem]
    return max_value

print(max_value_in_array([3,5,6,777]))