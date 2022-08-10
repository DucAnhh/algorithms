class Solution:
    # require an algorithm that runs in O(n) time and without using the division operation.
    def productExceptSelf(self, nums):
        prefix = [1] # the first element of prefix is 1
        postfix = [1] # the last element of postfix is 1
        answer = []
        for i in range(len(nums)):
            prefix.append(prefix[-1]*nums[i])
        #print(prefix)
        for i in range(len(nums)):
            postfix.insert(0, postfix[0]*nums[len(nums)-i-1])
        #print(postfix)
        for i in range(len(nums)):
            answer.append(prefix[i]*postfix[i+1])
        return answer
nums = [1, 2, 3, 4]
a = Solution()
print(a.productExceptSelf(nums))

# example nums = [1, 2, 3, 4] 
# so prefix (the array of product of all element which after nums[i]) 
# and postfix (the array of product of all element which before nums[i]) 
# prefix = 1 + [1, 2, 6, 24] with the first element is always 1 because no element is before nums[0]
# postfix = [24, 24, 12, 4] + 1 with the last element is always 1 becuase no element is after nums[-1]