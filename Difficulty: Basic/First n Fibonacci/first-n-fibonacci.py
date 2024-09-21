#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        res=[1,1]
        if n==1:
            return [1]
        elif n==2:
            return res
        elif n>2:
            num=2
            while num<n:
                s=res[num-1]+res[num-2]
                res.append(s)
                num+=1
            return res    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends