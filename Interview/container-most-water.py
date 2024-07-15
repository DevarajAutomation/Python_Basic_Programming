def container_most_water(heights):

    l=0
    r=len(heights)-1
    maxarea=0

    while l < r:
        area = (r-l) * min(heights[l],heights[r])

        maxarea = max(maxarea,area)

        if heights[l] < heights[r]:
            l +=1
        else:
            r-=1
    return maxarea


height = [1,8,6,2,5,4,8,3,7]

print(container_most_water(height))