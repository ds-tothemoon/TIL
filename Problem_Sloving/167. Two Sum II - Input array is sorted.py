class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        tmp = numbers[left] + numbers[right]
        while left < right and tmp != target:
            tmp = numbers[left] + numbers[right]
            if tmp > target:
                right -= 1
            elif tmp < target:
                left += 1
        return [left + 1, right + 1]  