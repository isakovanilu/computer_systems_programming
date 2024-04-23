def check_if_array_is_sorted(arr_list):
    if arr_list == sorted(arr_list):
        print('The given array is sorted')
        return 1
    return 0
        
print(check_if_array_is_sorted([1,2,3,4,5]))
print('*****')
print(check_if_array_is_sorted([4,2,3,4,5]))

def max_value_in_array(arr_list):
    max_value = arr_list[0]
    for elem in range(1, len(arr_list)):
        if arr_list[elem] > max_value:
            max_value = arr_list[elem]
    print(f'The max value is {max_value}')
    return max_value

print(max_value_in_array([3,5,6,777]))

def linear_search_in_array(arr_list, n):
    for index, elem in enumerate(arr_list):
        if n == elem:
            return index
    return -1
print(linear_search_in_array([9,1,2,3,4,7,3], 3))

def sum_array(arr_lis):
    sum = 0
    for _, elem in enumerate(arr_lis):
        sum += elem
    return sum

print(sum_array([1,2,3,4,5]))