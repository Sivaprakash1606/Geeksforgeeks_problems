class Solution:
    def isValid(self, str):
        count = 0
        num = ""
        
        for i in range(len(str)):
            if str[i] != ".":
                num = num + str[i]
            else:
                # Check if the segment is empty or out of range or has leading zeros
                if num == "" or int(num) > 255 or (len(num) > 1 and num[0] == '0'):
                    return False
                num = ""
                count = count + 1
        
        # After the loop, we need to validate the last segment
        if num == "" or int(num) > 255 or (len(num) > 1 and num[0] == '0'):
            return False
        
        # Ensure that we have exactly 4 segments
        count = count + 1
        if count == 4:
            return True
        
        return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends