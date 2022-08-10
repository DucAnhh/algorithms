class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = [] # list of word_dict
        output = [] # list of strings
        for s in strs:
            word_dict = self.count(s)
            if word_dict not in hash_map: # if s is in new group
                hash_map.append(word_dict)
                output.append([s])
            else:
                for i in range(len(hash_map)):
                    if hash_map[i] == word_dict:
                        output[i].append(s)
        return output
            
    def count(self, strs:str): # example: bat -> {a:1, b:1, c:1} (word_dict)
        ans = {}
        for i in range(len(strs)): 
            if strs[i] not in ans: # check the i'th word
                num = 1 # number of the i'th word
                for j in range(i+1, len(strs)):
                    if strs[j] == strs[i]:
                        num = num + 1
                ans[strs[i]] = num
        return ans