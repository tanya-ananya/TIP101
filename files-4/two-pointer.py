'''
Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
'''
def is_prime(n):
  if n <= 1:
      return False
  i = 2
  while i * i <= n:
      if n % i == 0:
          return False
      i += 1
  return True

print(is_prime(5))
print(is_prime(12))

'''
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).
'''
def reverse_list(lst):
  first, second = 0, len(lst) - 1
  while first < second:
    lst[first], lst[second] = lst[second], lst[first]
    first += 1
    second -= 1
  return lst

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))

'''
Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.
'''
def sort_array_by_parity(nums):
  left, right = 0, len(nums) - 1
  while left < right:
    if nums[left] % 2 == 0:
      left += 1
    elif nums[right] % 2 == 1:
      right -= 1
    elif nums[left] % 2 == 1 and nums[right] % 2 == 0:
      nums[left], nums[right] = nums[right], nums[left]
  return nums

nums = [3,1,2,4]
print(sort_array_by_parity(nums))

'''
Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the first palindromic string in the list. A string is palindromic if it reads the same forward and backward. If there is no such string, return an empty string ""
'''
def helper_function(s):
  first, second = 0, len(s) - 1
  while first < second:
    if s[first] != s[second]:
      return False
    first += 1
    second -= 1
  return True

def first_palindrome(words):
  for word in words:
    if helper_function(word):
      return word
  return ' '

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

'''
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes the duplicates in-place such that each element appears only once. Do not allocate extra space for another array; you must do this by modifying the input list with O(1) extra memory. The function returns the new length of the list.
'''
def remove_duplicates(nums):
  if not nums:
    return 0
  # Pointer j for the position of the next unique element
  j = 1
  # Iterate through the array with i
  for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
      nums[j] = nums[i]
      j += 1
  nums[:] = nums[:j]
  return j  # The new length after removing duplicates

nums = [1,1,2,3,4,4,4,6]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list

'''
------------------Section Two
'''

'''
Write a function is_perfect_number() that takes in a positive integer n and returns True if it is a perfect number and False otherwise. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

For example, 6 is a perfect number because its divisors or 1, 2, and 3 and 1 + 2 + 3 = 6.
'''

def is_perfect_number(n):
  count = 0
  for x in range(1, n):
    if n % x == 0:
      count += x
  return count == n

print(is_perfect_number(6))

'''
Write a function reverse_vowel() that takes in a string s as a parameter and returns a string with all the vowels in the string reversed. The consonants should remain in the same position. For this question, we consider a, e, i, o, and u as vowels but not y. The vowels can appear in both lower and upper cases, more than once.
'''
def reverse_vowels(s):
  first, second = 0, len(s) - 1
  vowel = ['a', 'e', 'i', 'o', 'u']
  s_list = list(s)
  while first < second:
    if s_list[first] in vowel and s_list[second] in vowel:
      s_list[first], s_list[second] = s_list[second], s_list[first]
      first += 1
      second -= 1
    elif s_list[first] in vowel:
      second -= 1
    elif s_list[second] in vowel:
      first += 1
    else:
      first += 1
      second -= 1
  return ''.join(s_list)

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

'''
The two-pointer approach can also be used with two pointers that iterate forward through a list or string at different rates. Use two pointers to solve the following problem:

Write a function removeElement() that takes in a list nums and a value val as parameters and removes all instances of that value in-place. The function returns the new length of nums.
'''
def removeElement(nums, val):
  i = 0
  for j in range(len(nums)):
    if nums[j] != val:
      nums[i] = nums[j]
      i += 1
  return i

nums = [5, 4, 4, 3, 4, 1]
nums_len = removeElement(nums, 4)
print(nums) # same list
print(nums_len)

'''
Problem 1: Highest Exponent
Write a function find_highest_exponent() that takes in an integer base and an integer limit as parameters. The function returns the highest exponent for which a given base raised to that exponent is less than or equal to limit.
'''

def find_highest_exponent(base, limit):
  current = 0
  for x in range(1, 100):
    if 2 ** x <= limit:
      current = x
  return current

exp = find_highest_exponent(2, 100)
print(exp)

'''
Write a function two_sum() that takes in a sorted list of integers nums and an integer target as parameters and returns the indices of the two numbers that add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the indices in any order.
'''

def two_sum(nums, target):
  first, second = 0, 1
  while first < second:
    current = nums[first] + nums[second]
    if current == target:
      return [first, second]
    else:
      first += 1
      second += 1

nums = [2,7,11,15,7]
sol1 = two_sum(nums, 9)
print(sol1)
sol2 = two_sum(nums, 18)
print(sol2)

'''
Write a function reverse_prefix() that takes in a 0-indexed string word and a character ch as parameters. The function reverses the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive) and keeps the rest of the string the same. If ch does not exist in word, do nothing. Return the resulting string.
'''

def reverse_prefix(word, ch):
  first, second = 0, 0
  new_word = list(word)
  for x, y in enumerate(word):
    if y == ch:
      second = x
    else:
      second = -1

  if second == -1:
    return word 

  while first < second:
    new_word[first], new_word[second] = new_word[second], new_word[first]
    first += 1
    second -= 1
  return ''.join(new_word)

word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

'''
--------------------------SESSION TWO---------------------------
'''

'''
Write a function is_long_pressed() that takes in a string name and a string typed as parameters. Imagine your friend is typing their name into a keyboard and when typing a character, the key might get long pressed and the character will be typed 1 or more times.

The function should examine the typed characters and return True if it is possible that it was your friends name with some characters being long pressed and False otherwise.
'''
def is_long_pressed(name, typed):
  first, second = 0, 0
  while first < len(name) and second < len(typed):
    if name[first] == typed[second]:
      first += 1
      second += 1
    elif name[first] != typed[second]:
      return True
  return False


name = "alex"
typed = "alex"
print(is_long_pressed(name, typed))

'''
Imagine you're an awesome babysitter and want to give the kids you're looking after some cookies as a snack.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with.
Each cookie j has a cookie size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child will be content.
If s[j] < g[i], the child will not be content.

Write a function find_content_children() that takes in the greed list g and the cookie size list s as parameters and maximizes the number of content children you are babysitting! The function returns

Example 1:

g = [1,2,3]
s = [1,1,3]
# There are 3 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 1 --> content child

# child `1` has a greed factor of 2
# cookie `1` has a size of 1, this child will not be content

# child `2` has a greed factor of 3
# cookie `2` has a size of 3 --> content child

find_content_children(s, g) 
# Output: 2 
'''
def find_content_children(g, s):
  first, second = 0, 0
  ans = 0
  while first < len(g) and second < len(s):
    if g[first] <= s[second]:
      ans += 1
    first += 1
    second += 1
  return ans

g = [1,2,3]
s = [1,1,3]
print(find_content_children(g, s))

'''
Write a function valid_palindrome() that takes in a string s as a parameter and returns True if s can be a palindrome after deleting at most one character from it and False otherwise.
'''
def valid_palindrome(s):
  first, second = 0, len(s) - 1
  new_s = list(s)
  count = 0
  while first < second:
    if new_s[first] == new_s[second]:
      first += 1
      second -= 1
    elif new_s[first + 1] == new_s[second] and count < 2:
      first += 2
      second -= 1
      count += 1
    elif new_s[first] == new_s[second - 1] and count < 2:
      first += 1
      second -= 2
      count += 1
    else:
      return False
  return True

s = "aba"
s2 = "abca"
s3 = "abda"

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))

'''
Write a function find_largest_k() that takes in a list of integers nums that does not contain any zeroes as a parameter. The function finds the largest positive integer k such that -k also exists in the array and returns k. If there is no such integer, return -1.
'''
def find_largest_k(nums):
  highest = 0
  for x in nums:
    if x > highest:
      highest = x
  if highest * -1 in nums:
    return True
  else:
    return -1

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

'''Problem 3: Valid Palindrome
Write a function valid_palindrome() that takes in a string s as a parameter and returns True if s can be a palindrome after deleting at most one character from it and False otherwise.'''
def valid_palindrome(s):
  del_count = 0
  lst = list(s)
  first, second = 0, len(lst) - 1
  while first < second:
    if lst[first] == lst[second]:
      first += 1
      second -= 1
    elif lst[first] != lst[second] and del_count < 1:
      lst.pop(second)
      second -= 1
      del_count += 1
    else:
      return False
  return True

s = "aba"
s2 = "abca"
s3 = "abc"
print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))

'''Problem 4: Positive Negative Pairs
Write a function find_largest_k() that takes in a list of integers nums that does not contain any zeroes as a parameter. The function finds the largest positive integer k such that -k also exists in the array and returns k. If there is no such integer, return -1.'''

def find_largest_k(nums):
  nums.sort()
  first, second = 0, len(nums) - 1
  largest = -1

  while first < second:
    sum = nums[first] + nums[second]
    if sum < 0:
      first += 1
    elif sum > 0:
      second -= 1
    else:
      largest = nums[second]
      first += 1
      second -= 1
  return largest

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))
nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))

'''Problem 5: Good Substring
Use the sliding window technique to solve the following problem:
Write a function count_good_substrings() that takes in a string s as a parameter and returns the number of good substrings of length three. A string is good if there are no repeated characters. A substring is a continuous sequence of characters in a string.
If there are multiple occurrences of the same substring, every occurrence should be counted.'''

def count_good_substrings(s):
  count = 0
  for x in range(len(s) - 2):
    window = s[x:x+3]
    if len(window) == len(set(window)):
      count += 1
  return count 

s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))

'''Problem 6: Duplicates Within Range
Write a function contains_nearby_duplicate() that takes in a list lst and a positive number k as parameters. The function returns True if the list contains any duplicate elements within the range k and False otherwise. If k is more than the list's size, the solution should check for duplicates in the complete list'''

def contains_nearby_duplicate(lst, k):
  seen = {}
  for index, num in enumerate(lst):
    if num in seen and index - seen[num] <= k:
      return True
    seen[num] = index
  return False

lst = [1, 2, 3, 1, 2, 3]
lst2 = [1, 0, 1, 1]
print(contains_nearby_duplicate(lst, 2))
print(contains_nearby_duplicate(lst2, 1))