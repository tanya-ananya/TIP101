'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''
def firstUniqChar(s):
  dict = {}
  for index, char in enumerate(s):
      if char not in dict:
          dict[char] = [1, index]
      else:
          dict[char][0] += 1
  print(dict)
  for key, value in dict.items():
    if value == 1:
      return s.index(key)
  return -1

s = 'leetcode'
print(firstUniqChar(s))

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''
def isAnagram(s, t):
    s_word = ''.join(sorted(s))
    t_word = ''.join(sorted(t))
    if s_word == t_word:
        return True
    return False

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

def isValid(s):
  stack = [] # only use append and pop
  pairs = {
      '(': ')',
      '{': '}',
      '[': ']'
  }
  for bracket in s:
      if bracket in pairs:
          stack.append(bracket)
      elif len(stack) == 0 or bracket != pairs[stack.pop()]:
          return False

  return len(stack) == 0

#   parenthesis_dict = {
#     '(': ')',
#     '{': '}',
#     '[': ']'
#   }

#   for index, char in enumerate(s):
#       if char in parenthesis_dict and parenthesis_dict[char] in s[index:]:

s = '[}]'
print(isValid(s))

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

def isPalindrome(s):
  new_s = s.lower()
  if new_s.isalpha() is False:
    return False

  s_backwards = s[::-1]
  if new_s == s_backwards:
    print(f'{s} is a palindrome. The same backward as forward')

isPalindrome('hannah')

def isPalindrome(s):
  lower_s = s.lower()
  strip_s = re.sub(r'[^a-z0-9]', '', lower_s)
  print(strip_s)

  s_backwards = strip_s[::-1]
  if strip_s == s_backwards:
    return True
  return False
  