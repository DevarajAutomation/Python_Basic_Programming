def product_except_self(nums):

    length=len(nums)
    product=[1] * length

    for i in range(1,length):
        product[i]=product[i-1] * nums[i-1]

    right=nums[-1]

    for i in range(length-2,-1,-1):
        product[i] *=right
        right *=nums[i]

    return product

a=[2,3,4,5]
print(product_except_self(a))