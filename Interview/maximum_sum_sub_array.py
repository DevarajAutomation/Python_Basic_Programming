def maximum_sum_sub_array(arr):
    current_max=0
    overall_max=0

    for num in arr:
        current_max=max(current_max+num,num)
        overall_max=max(overall_max,current_max)

    return overall_max

print(maximum_sum_sub_array([7,2,-9,3]))