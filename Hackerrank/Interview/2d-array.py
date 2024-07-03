"""https://www.hackerrank.com/challenges/2d-array/problem"""

def hourGlass(arr):

    max_sum=-63

    for i in range(4):
        for j in range(4):
            top= arr[i][j] + arr[i] [j+1] + arr[i][j+2]
            mid= arr[i+1][j+1]
            bottom= arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+1]

            hour_glass= top+mid+bottom

            if hour_glass > max_sum:
                max_sum=hour_glass

    return max_sum