
## Problem1 Trap Rain Water 

# (https://leetcode.com/problems/trapping-rain-water/)


"""
Time Complexity: O(N)
Space Complexity: O(2*N)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left = []
        current = 0
        
        for h in height:
            current = max(current, h)
            left.append(current)
        
        right = []
        current = 0
        
        for h in height[::-1]:
            current = max(current, h)
            right.append(current)
            
        right = right[::-1]
        
        water = 0
        for i, h in enumerate(height):
            if i == 0 or i == n - 1:
                continue
                
            water_content = max(0, min(left[i-1], right[i+1]) - h )
            #print(i, left[i-1], right[i+1], water_content)
            water += water_content
            
        return water


"""
Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        right = []
        current = 0
        
        for h in height[::-1]:
            current = max(current, h)
            right.append(current)
            
        right = right[::-1]
        
        left = 0
        water = 0
        for i, h in enumerate(height):
            if i == 0 or i == n - 1:
                left = max(left, h)
                continue
                
            water_content = max(0, min(left, right[i+1]) - h )
            #print(i, left[i-1], right[i+1], water_content)
            left = max(left, h)
            
            water += water_content
            
        return water