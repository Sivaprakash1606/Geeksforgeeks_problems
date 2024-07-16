class Solution:
    def ExtractNumber(self, sentence):
        num = set("1234567890")
        num_arr = []
        w = ""

        for i in sentence:
            if i not in num:
                if len(w) > 0 and "9" not in w:
                    num_arr.append(int(w))
                w = ""
            else:
                w += i
        if len(w) > 0 and "9" not in w:
            num_arr.append(int(w))

        if num_arr:
            return max(num_arr)
        return -1


                


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends