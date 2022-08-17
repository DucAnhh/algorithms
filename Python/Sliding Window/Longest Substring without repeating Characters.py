class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        substring = [] # the temporary substring
        for i in range(len(s)):
            if s[i] not in substring:
                substring.append(s[i])
            else:
                answer = max(len(substring), answer)
                # remove until the present duplicate element in substring
                while s[i] in substring:
                    substring.remove(substring[0])
                # add the new element again
                substring.append(s[i])
        return max(len(substring), answer)

s = "abac"
a = Solution()
print(a.lengthOfLongestSubstring(s))