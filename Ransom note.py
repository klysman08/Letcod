class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        a = ransomNote
        b = magazine
 
        for i in a:
            if i in b:
                b = b.replace(i,"",1)
            else:
                return False
                
        return True
            
                

teste = Solution()
teste.canConstruct("abaa", "abaa8a")

if teste == True:
    print('ok')
else:
    print('not')