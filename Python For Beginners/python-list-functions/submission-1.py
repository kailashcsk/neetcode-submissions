from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    s = 0
    for n in nums:
        s += n
    return s

def get_min(nums: List[int]) -> int:
    mi = float('inf')
    for n in nums:
        if n < mi:
            mi = n
    return mi

def get_max(nums: List[int]) -> int:
    ma = float('-inf')
    for n in nums:
        if n > ma:
            ma = n
    return ma

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
