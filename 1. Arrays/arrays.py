# ==========================================
# DSA WITH PYTHON
# ARRAYS
# ==========================================


# ==================================================
# 1. FIND THE LARGEST ELEMENT
# ==================================================
#
# Given an array, find the largest number.
#
# Example:
# [3, 7, 2, 9, 4]
#
# Answer:
# 9
#
# Pattern:
# Keep track of the largest number seen so far.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


numbers = [3, 7, 2, 9, 4]


def find_largest(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest


print(find_largest(numbers))


# ==================================================
# 2. FIND THE SMALLEST ELEMENT
# ==================================================
#
# Given an array, find the smallest number.
#
# Example:
# [3, 7, 2, 9, 3]
#
# Answer:
# 2
#
# Pattern:
# Keep track of the smallest number seen so far.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def smallest_number(nums):
    smallest = nums[0]

    for num in nums:
        if num < smallest:
            smallest = num

    return smallest


print(smallest_number([3, 7, 2, 9, 3]))


# ==================================================
# 3. DETECT DUPLICATES
# ==================================================
#
# Check whether an array contains duplicate values.
#
# Example:
# [3, 7, 2, 9, 3]
#
# Answer:
# True
#
# We first solved this using nested loops.
# Then we learned the set approach.
#
# A set removes duplicate values.
#
# If:
#
# len(nums) != len(set(nums))
#
# then a duplicate exists.


def find_double(nums):
    nums_set = set(nums)

    if len(nums) != len(nums_set):
        return True

    return False


print(find_double([3, 7, 2, 9, 3]))


# ==================================================
# 4. FIND SECOND-LARGEST DISTINCT NUMBER
# ==================================================
#
# Find the largest and second-largest DISTINCT numbers.
#
# Example:
# [3, 7, 2, 9, 3, 8]
#
# Answer:
# Biggest = 9
# Second biggest = 8
#
# Duplicate largest values don't count as the
# second-largest DISTINCT number.
#
# Example:
# [9, 9, 8, 7]
#
# Biggest = 9
# Second biggest = 8
#
# If there is no second distinct number:
#
# [5, 5, 5, 5]
#
# Biggest = 5
# Second biggest = None
#
# Pattern:
# Scan the array while maintaining:
#
# biggest
# second_biggest
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def largest_and_2nd_largest(nums):
    biggest = None
    second_biggest = None

    for num in nums:

        if num == biggest:
            continue

        if biggest is None or num > biggest:
            second_biggest = biggest
            biggest = num

        elif second_biggest is None or num > second_biggest:
            second_biggest = num

    return biggest, second_biggest


print(largest_and_2nd_largest([3, 7, 2, 9, 3, 8]))


# ==================================================
# 5. COUNT OCCURRENCES
# ==================================================
#
# Count how many times a target number appears.
#
# Example:
# [3, 7, 3, 2, 7, 3, 9, 3]
#
# Target = 3
#
# Answer:
# 4
#
# Pattern:
# Use a counter.
#
# count = 0
#
# Every time the condition is true:
#
# count += 1
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def count_number(nums, target):
    count = 0

    for num in nums:
        if target == num:
            count += 1

    return count


print(count_number([3, 7, 3, 2, 7, 3, 9, 3], 3))


# ==================================================
# 6. COUNT NUMBERS GREATER THAN A TARGET
# ==================================================
#
# Count how many numbers are greater than a target.
#
# Example:
# [3, 7, 3, 2, 7, 3, 9, 3]
#
# Target = 5
#
# Numbers greater than 5:
# 7, 7, 9
#
# Answer:
# 3
#
# Pattern:
# Counter + condition.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def count_greater(nums, target):
    count = 0

    for num in nums:
        if target < num:
            count += 1

    return count


print(count_greater([3, 7, 3, 2, 7, 3, 9, 3], 5))


# ==================================================
# 7. REVERSE AN ARRAY
# ==================================================
#
# Given:
# [1, 2, 3, 4, 5]
#
# Expected:
# [5, 4, 3, 2, 1]
#

numbers = [1, 2, 3, 4, 5, 6, 7]

def reverse_array(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
    return nums


print(reverse_array(numbers))

# ==================================================
# 8. CHECK IF ARRAY IS PALINDROME
# ==================================================

# Check if an array reads the same from both sides.

# Example:
# [1, 2, 3, 2, 1] → True
# [1, 2, 3, 4, 5] → False

# Pattern:
# Two Pointers.

# Time Complexity: O(n)
# Space Complexity: O(1)

numbers = [1, 2, 4, 3, 4, 1, 1]

def is_palindrome(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome(numbers))

# ==================================================
# 9. REMOVE DUPLICATES FROM SORTED ARRAY
# ==================================================

# Remove duplicates from a sorted array using two pointers.
# Keep only unique elements in the beginning of the array.

# Example:
# [1, 1, 2, 2, 3, 3, 4] → [1, 2, 3, 4]

# Pattern:
# Two Pointers.

# Time Complexity: O(n)
# Space Complexity: O(1)

numbers = [1, 1, 2, 2, 3, 3, 4]

def remove_duplicates(nums):
    unique = 0

    for scan in range(1,len(numbers)):
        if nums[unique] != nums[scan]:
            nums[unique] = nums[scan]
            unique += 1

    return nums[:unique+1]

print(remove_duplicates(numbers))