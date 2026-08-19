# # leetcode 1480
# def runningSum( nums: List[int]) -> List[int]:
#     nums = [1, 2, 3, 4]
#     for i in range(1, len(nums)):
#         nums[i] += nums[i-1]
#     print(nums)
        
# leetcode 1732
# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         curr_alt = 0
#         max_alt = 0

#         for i in gain:
#             curr_alt += i
#             if curr_alt > max_alt:
#                 max_alt = curr_alt 
#         return max_alt

# def largestAltitude(self, gain: List[int]) -> int:
#         n = len(gain)
#         alt = [0] *(n+1)
#         for i in range(1, n+1):
#             alt[i] = alt[i-1] + gain[i-1]
#         return max(alt)

# leetcode 1991
# from typing import List


# class Solution:

#   def findMiddleIndex(self, nums: List[int]) -> int:
#     total_sum = sum(nums)
#     left_sum = 0

#     for i in range(len(nums)):
#       right_sum = total_sum - left_sum - nums[i]
#       if left_sum == right_sum:
#         return i
#       left_sum += nums[i]

#     return -1



# if __name__ == "__main__":
#   sol = Solution()

#   # Test cases from LeetCode
#   nums1 = [2, 3, -1, 8, 4]
#   nums2 = [1, -1, 4]
#   nums3 = [2, 5]

#   print("Result 1:", sol.findMiddleIndex(nums1))  # Expected: 3
#   print("Result 2:", sol.findMiddleIndex(nums2))  # Expected: 2
#   print("Result 3:", sol.findMiddleIndex(nums3))  # Expected: -1

# leetcode 724
# def pivotIndex(self, nums: List[int]) -> int:
#         total_sum , left_sum = sum(nums), 0
#         for i in range(len(nums)):
#             right_sum = total_sum - nums[i] - left_sum 
#             if left_sum == right_sum:
#                 return i
#             left_sum += nums[i]
#         return -1
# leetcode 523
