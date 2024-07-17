
from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        d={}
        result=[]
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key,value in d.items():
            if value>1:
                result.append(key)
        if result:
            return result
        return [-1]
#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.duplicates(n, arr)

        IntArray().Print(res)

# } Driver Code Ends