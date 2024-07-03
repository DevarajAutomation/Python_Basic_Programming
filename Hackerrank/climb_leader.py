"""https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem"""

def climb_leader(ranked,player):

    ranked=sorted(set(ranked), reverse=True)

    n=len(ranked)
    result=[]
    for score in player:
        low,high = 0,n-1

        while low <=high:

            mid=(low+high)//2

            if ranked[mid]==score:
                low=mid
                break
            elif ranked[mid] < score:
                high=mid-1
            else: 
                low=mid+1

        result.append(low+1)

    return result

r=[100,100,50,40,40,20,10]
p=[5,25,50,120]

print(climb_leader(r,p))








