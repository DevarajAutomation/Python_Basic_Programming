"""https://www.hackerrank.com/challenges/picking-numbers/problem"""

def pick_number(a):

    freq=[0]*100

    for ar in a:
        freq[ar]+=1

    maximum_sub_array=0

    for i in (1, 100):
        maximum_sub_array= max(maximum_sub_array, freq[i] + freq[i-1])

    return maximum_sub_array

a=[1,1,2,2,4,4,5,5,5]

print(pick_number(a))