class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)== sorted(t):
          return True
        else:
          return False

a = Solution1()
print(a.isAnagram("nguyenducanh", "anhnguyenduc"))

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        countS, countT = {}, {} #two dict
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c):
                return False
        
        return True

b = Solution2()
print(b.isAnagram("cat", "rat"))