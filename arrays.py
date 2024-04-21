def check_if_array_is_sorted(arr_list):
    if arr_list == sorted(arr_list):
        print('The given array is sorted')
    else:   
        print('The given array is not sorted')  
        
check_if_array_is_sorted([1,2,3,4,5])
print('*****')
check_if_array_is_sorted([4,2,3,4,5])
