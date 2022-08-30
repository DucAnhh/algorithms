from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # sort information of car descending order to postion 
        car = [(p, s) for p, s in zip(position, speed)]
        car.sort(reverse = True)
        # stack contains the time for the fleet to finish the race
        stack = []
        # Descending order of position because the nearest (destination) car is always in the fleet which goes to the destination firstly. 
        # And the behind car cannot finish before the front one i.e. the time to finish of the behind car is only less than or equal the front car's one
        # because if the behind car catches up the front one, it means that the speed of the behind one is greater than the front's and 
        # the behind must run with the front car's speed after merging.
        for p, s in car:
            time = (target-p)/s
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
   
        return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

a = Solution()
print(a.carFleet(target, position, speed))