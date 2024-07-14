"""https://www.hackerrank.com/challenges/three-month-preparation-kit-divisible-sum-pairs/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one"""


def divisable_sum_pair(arr, k):
    result = []

    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i] + arr[j]) % k ==0:
                result.append((i,j))


    return result





a = [1, 3, 2, 6, 1, 2]
k = 3

print(divisable_sum_pair(a, k))
