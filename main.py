from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    left = 0
    right = 1

    while left < len(nums) - 1:
        if nums[left] + nums[right] == target:
            return [left, right]
        
        right += 1
        if right >= len(nums):
            left += 1
            right = left + 1