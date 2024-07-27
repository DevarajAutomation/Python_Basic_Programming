def maximum_product_sub_array(arr):
    minimum=arr[0]
    maximum=arr[0]
    overall_max=arr[0]

    for i in range(1,len(arr)):
        temp=max(max(arr[i],arr[i]*maximum), arr[i]*minimum)
        minimum=min(min(arr[i],arr[i]*maximum),arr[i]*minimum)
        maximum=temp

        overall_max=max(overall_max,maximum)

    return overall_max

ar=[-1, -3, -10, 0,90,2]
print(maximum_product_sub_array(ar))