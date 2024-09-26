'''
The sliding window technique is an algorithmic technique often used to find a subarray or substring that meets certain criteria. It works by initializing two pointers to point at the start and end of a ‘window’ or subsection of the string/array at a time. The pointers are then incremented to slide the window and examine a different subarray or substring.

Use the sliding window technique to solve the following problem:

Write a function count_good_substrings() that takes in a string s as a parameter and returns the number of good substrings of length three. A string is good if there are no repeated characters. A substring is a continuous sequence of characters in a string.
If there are multiple occurrences of the same substring, every occurrence should be counted.
'''

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


'''
--------------------------------SESSION ONE------------------------------
'''

'''
Question 1
Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
'''

def is_prime(n):
  if n <= 1:
    return False
  for x in range(2, n):
    if n % x == 0:
      return False
  return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

'''
Question 2
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).
'''

def reverse_list(lst):
  first, second = 0, len(lst) - 1
  while first < second:
    lst[first], lst[second] = lst[second], lst[first]
    first += 1
    second -= 1
  return lst

print(reverse_list([1, 2, 3, 4, 5]))

'''
Question 3
Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.
'''

def sort_array_by_parity(nums):
  first, second = 0, len(nums) - 1
  while first < second:
    if nums[first] % 2 == 0:
      first += 1
    elif nums[second] % 2 != 0:
      second -= 1
    else:
      nums[first], nums[second] = nums[second], nums[first]
      first += 1
      second -= 1
  return nums

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

'''
Question 5
Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the first palindromic string in the list. A string is palindromic if it reads the same forward and backward. If there is no such string, return an empty string ""
'''

def is_palindrome(s):
  first, second = 0, len(s) - 1
  while first < second:
    if s[first] != s[second]:
      return False
    first += 1
    second -= 1
  return True

def first_palindrome(words):
  for word in words:
    if is_palindrome(word):
      return word
  return ''


words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

'''
Problem 6: Remove Duplicates with O(1)
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes the duplicates in-place such that each element appears only once. Do not allocate extra space for another array; you must do this by modifying the input list with O(1) extra memory. The function returns the new length of the list.
'''

def remove_duplicates(nums):
  if nums is None:
    return 0
  j = 1
  for x in range(1, len(nums)):
    if nums[x] != nums[x - 1]:
      nums[j] = nums[x]
      j += 1
  nums[:] = nums[:j]
  return len(nums)

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list

'''
Problem 1: Perfect Number
Write a function is_perfect_number() that takes in a positive integer n and returns True if it is a perfect number and False otherwise. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

For example, 6 is a perfect number because its divisors or 1, 2, and 3 and 1 + 2 + 3 = 6.
'''

def is_perfect_number(n):
  if n <= 1:
    return False
  counter = 0
  for x in range(1, n):
    if n % x == 0:
      counter += x
  return counter == n

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))

'''
Problem 2: 2-Pointer Palindrome
Write a function is_palindrome() that takes in a string s as a parameter and returns True if the string is a palindrome and False otherwise. You may assume the string contains only lowercase alphabetic characters.
'''
def is_palindromes(s):
  first, second = 0, len(s) - 1
  while first < second:
    if s[first] != s[second]:
      return False
    first += 1
    second -= 1
  return True

s = "amanaplanacanalpanama"
s2 = "helloworld"
print(is_palindromes(s))
print(is_palindromes(s2))

'''
Problem 4: Make Palindromes
You are given a string s consisting of lowercase English letters, and are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter.

Write a function make_palindrome() that takes in a string s and turns it into a palindrome with the minimum number of operations as possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

The function returns the resulting palindrome string.
'''

def make_palindrome(s):
  if not s:
    return False

  lst = list(s)
  first, second = 0, len(s) - 1
  while first < second:
    if s[first] < s[second]:
      lst[first] = lst[second]
    else:
      lst[second] = lst[first]
    first += 1
    second -= 1
  return ''.join(lst)

s = "egcfe"
s_pal = make_palindrome(s)
print(s_pal)

s = "abcd"
s_pal = make_palindrome(s)
print(s_pal)

s = "seven"
s_pal = make_palindrome(s)
print(s_pal)

'''
Problem 5: Reverse Vowels
Write a function reverse_vowel() that takes in a string s as a parameter and returns a string with all the vowels in the string reversed. The consonants should remain in the same position. For this question, we consider a, e, i, o, and u as vowels but not y. The vowels can appear in both lower and upper cases, more than once.
'''
def helper(letter):
  return letter in 'aeiouAEIOU'
def reverse_vowels(s):
  first, second = 0, len(s) - 1
  lst = list(s)
  while first < second:
    while first < second and not helper(lst[first]):
      first += 1
    while first < second and not helper(lst[second]):
      second -= 1
    temp = lst[first]
    lst[first] = lst[second]
    lst[second] = temp
    first += 1
    second -= 1
  return ''.join(lst)

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)
s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)

'''
Problem 6: Two-Pointer Remove Element
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
print(nums)
print(nums_len)

'''
Problem 6: Squash Spaces
The two-pointer approach can also be used with two pointers that iterate forward through a list or string at different rates. Use two pointers to solve the following problem:

Write a function squash_spaces() that takes in a string s as a parameter and returns a new string with each substring with consecutive spaces reduced to a single space. Assume s can contain leading or trailing spaces, but in the result should be trimmed.
Do not use any of the built-in trim methods.
'''

def squash_spaces(s):
  ptr = 0
  output = []
  while ptr < len(s) and s[ptr] == ' ':
    ptr += 1
  while ptr < len(s):
    if s[ptr] != ' ':
      output.append(s[ptr])
    else:
      if len(output) > 0 and output[-1] != ' ' and ptr + 1 < len(s) and s[ptr + 1] != ' ':
        output.append(s[ptr])
    ptr += 1
  return ''.join(output)

print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))

'''
-----------------------------SESSION TWO--------------------------------
'''
'''
Problem 1: Long Pressed
Write a function is_long_pressed() that takes in a string name and a string typed as parameters. 
Imagine your friend is typing their name into a keyboard and when typing a character, the key might 
get long pressed and the character will be typed 1 or more times.

The function should examine the typed characters and return True if it is possible that it was your
friends name with some characters being long pressed and False otherwise.
'''
def is_long_pressed(name, typed):
   first, second = 0, 0
   while first < len(name) and second < len(typed):
      if name[first] == typed[second]:
         first += 1
         second += 1
      elif typed[second] == typed[second - 1]:
         second += 1
      else:
         return False
   if first < len(name):
      return False 
   while second < len(typed):
      if typed[second] == name[-1]:
         return False
      second += 1
   return True

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))
name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))
name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))