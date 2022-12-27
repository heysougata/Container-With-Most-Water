#User function Template for python3



def maxArea(A,le):
    #code here
    l,r,area=0,le-1,0
    while l<r:
        area = max(area,min(A[l],A[r])*(r-l))
        if A[l]<A[r]:
            l+=1
        else:
            r-=1
    return area
    
