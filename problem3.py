


class Solution:
    def reverse_array(self, arr, start, end):
        
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            
    
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        #reverse the whole array
        self.reverse_array(nums, 0, n-1)
        
        #reverse the first k elements
        self.reverse_array(nums, 0, k-1)
    
        #revers the rest of the elements
        self.reverse_array(nums, k, n-1)
    
    """
    Time Complexity: O(N)
    Space Complexity O(N)
    """
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
        
#         k = k % n
        
#         stack_k = []
        
#         for i in range(k):
#             stack_k.append( nums.pop() )
            
#         stack_all = []
        
#         while len(nums) != 0:
#             stack_all.append( nums.pop() )
            
            
#         while len(stack_k) != 0:
#             nums.append( stack_k.pop() )
            
#         while len(stack_all) != 0:
#             nums.append( stack_all.pop() )
            
        