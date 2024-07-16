class Solution:
    def missingNumber(self, n, arr):
        num_set = set(arr)
        for num in range(1, n+1):
            if num not in num_set:
                return num
        return n

        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends