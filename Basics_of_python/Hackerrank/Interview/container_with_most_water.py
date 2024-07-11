def container_most_water(heights):

    max_area=0
    l=0
    r=len(heights)-1

    while l < r:
        area=(r-l) * min(heights[r],heights[l])

        max_area=max(max_area,area)

        if heights[l] < heights[r]:
            l +=1

        else:
            r-=1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(container_most_water(height))