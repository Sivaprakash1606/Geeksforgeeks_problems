from typing import List

class Solution:
    def duplicates(self, n: int, arr: List[int]) -> List[int]:
        count = {}
        
        # Count occurrences of each element
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        # Filter elements that occur more than once
        result = [key for key, value in count.items() if value > 1]
        
        # Sort the result in ascending order
        result.sort()
        
        # Return the sorted list of duplicates or [-1] if no duplicates are found
        return result if result else [-1]




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