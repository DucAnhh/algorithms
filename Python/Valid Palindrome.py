class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = self.convert(s)
      
      for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-1-i]:
          return False
      return True

    def convert(self, s: str):
      for i in s:
        if (ord("A") <= ord(i) <= ord("Z") or ord("a") <= ord(i) <= ord("z") or ord("0") <= ord(i) <= ord("9")) == True:
          continue
        else:
          s = s.replace(i, "") #remove
      return s.lower() # uppercase into lowercase

a = Solution()
print(a.isPalindrome(s = "A man, a plan, a canal: Panama"))