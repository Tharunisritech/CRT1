
# def numberOfSubarrays(nums: List[int], k: int) -> int:
#     def sub_arr(k):
#         if k < 0:
#             return 0
#         left,count,odd = 0, 0, 0
#         for right in range(len(nums)):
#             if nums[right] % 2 == 1:
#                 odd += 1
#             while odd > k:
#                 if nums[left] % 2 == 1:
#                     odd -= 1
#                 left += 1
#             count += (right - left + 1)
#         return count
#     return sub_arr(k) - sub_arr(k - 1)
# nums = [1, 1, 2, 1, 1]
# k =  3
# print(numberOfSubarrays(nums, k))


# # leetcode 1763

# def longestNiceSubstring( s: str) -> str:
#         if len(s) < 2:
#             return ""
        
#         char_s = set(s)
#         for i, c in enumerate(s):
#             if c.lower() in char_s and c.upper() in char_s:
#                 continue
#             left = self.longestNiceSubstring(s[:i])
#             right = self.longestNiceSubstring(s[i+1:])
#             return left if len(left) >= len(right) else (right)
#         return s 
# s = "YazaAay"
# print(longestNiceSubstring(s))