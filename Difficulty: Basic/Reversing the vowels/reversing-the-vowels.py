#User function Template for python3

class Solution:
    def modify(self, s):
        s=list(s)
        vowel={"a","e","i","o","u"}
        l=0
        r=len(s)-1
        while l<r:
            if s[l] not in vowel:
                l=l+1
            elif s[r] not in vowel:
                r=r-1
            elif s[r] in vowel and s[l] in vowel:
                s[l],s[r]=s[r],s[l]
                l=l+1
                r=r-1
        return "".join(s)   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends