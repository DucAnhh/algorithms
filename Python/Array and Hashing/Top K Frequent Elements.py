class Solution:
    def topKFrequent(self, nums, k: int):
        hashlist = {} # create hashmap using dict
        for i in nums:
            if i not in hashlist: 
                hashlist[i] = 1 # add i to hashmap
            else:
                hashlist[i] = hashlist[i] + 1
        # sort dict by value
        hashlist = dict(sorted(hashlist.items(), key=lambda item: item[1], reverse=True))
        
        # return a list of the first k key()
        return list(hashlist.keys())[0:k]