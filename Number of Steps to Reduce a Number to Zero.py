class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:    
            if num % 2 == 0:
                count += 1
                num = num / 2
            else:
                num = num - 1
                count += 1 
        return count

#test for num = 14
num = 14
steps = Solution()
print(steps.numberOfSteps(num))