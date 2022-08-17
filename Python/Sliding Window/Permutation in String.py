class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # I tried to write an algorithm with O(n) time-complexity
        if len(s1) > len(s2):
            return False
        
        count_s1 = {} # the character counter, it is fix
        # count in s1
        for i in s1:
            count_s1[i] = 1 + count_s1.get(i, 0)
        
        count_sub = {} # the counter of substring, substring is a sliding window
        
        # initialize count_sub that is the first len(s1) elements of s2
        for i in range(0, len(s1)):
            count_sub[s2[i]] = 1 + count_sub.get(s2[i], 0)
        if count_sub == count_s1:
                return True
        
        # slide
        for i in range(len(s1), len(s2)):
            # add s2[i] to sliding window
            count_sub[s2[i]] = count_sub.get(s2[i], 0) + 1
            # remove the front element (it is s2[i - len(s1)]) from sliding window
            count_sub[s2[i - len(s1)]] = count_sub.get(s2[i-len(s1)], 0)  - 1
            # if any element have value == 0 will be removed
            if count_sub.get(s2[i-len(s1)], 0) == 0 :
                count_sub.pop(s2[i-len(s1)])
            # compare
            if count_sub == count_s1:
                return True
        return False

s1 = "adc"
s2 = "dcda"
a = Solution()
print(a.checkInclusion(s1, s2))