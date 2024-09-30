'''
Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values.

keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.
'''

def create_dictionary(keys, values):
  ans = {}

  for x in ksys:
    for y in values:
      ans[x] = y

  return ans

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]

'''
# Session One, Question 1
def is_subsequence(lst, sequence):
  ans = []
  for x in lst:
    for y in sequence:
      if x == y:
        ans.append(x)
  if ans == sequence:
    return True
  return False

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
'''