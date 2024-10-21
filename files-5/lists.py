
------------------------------UNIT ONE--------------------------------
# Question 3
def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu('🍕')

# Question 4
def sum(a, b):
  return a + b

print(sum(20, 6))

# Question 5
def product(a, b):
  print(a * b)

product(3, 3)

# Question 6
def classify_age(age):
  if age < 18:
    print('child')
  else:
    print('adult')

classify_age(23)

# Question 7
def what_time_is_it(hour):
  if hour == 2:
    print('Taco time')
  elif hour == 12:
    print('Peanut butter tume')
  else:
    print('nap time')

what_time_is_it(6)

# Question 8
def blackjack(score):
  if score == 21:
    print('Blackjack!')
  elif score > 21:
    print('Bust!')
  elif (score >= 17) and (score < 21):
    print('Nice hand!')
  elif score < 17:
    print('Hit me!')

blackjack(19)

# Question 9
def counter(stop):
  for x in range(stop):
    print(x + 1)

counter(7)

#  Question 12
def sum_ten():
  count = 0
  for x in range(1, 11):
    count += x
  return count

print(sum_ten())

#  Question 14
def sum(x, y):
  count = 0
  for i in range(x, y+1):
    count += i
  return count

print(sum(3, 9))

#  Question 15
def print_negatives(containter):
  lst = []
  for x in containter:
    if x < 0:
      lst.append(x)
  return lst

example = [1, -2, -4, 7, 8 -9, -10]
print(print_negatives(example))

# Section 2, Question 3
def concatenate_list(example):
  return example * 2

lst = [1,2,3,4]
print(concatenate_list(lst))

# Question 5
def calculate_tip(bill, service_quality):
  if service_quality == 'poor':
    tip = bill * 0.10
  elif service_quality == 'average':
    tip = bill * 0.15
  elif service_quality == 'excellent':
    tip = bill * 0.20
  else:
    return None
  return tip

print(calculate_tip(44.53, 'average'))

# Question 11
def list_length(lst):
  leng = 0
  for x in lst:
    leng += 1
  return leng

lst = [2,4,6,8,10]
length = list_length(lst)
print(length)

# Question 12
def factorial(num):
  ans = 1
  for x in range(1, num+1):
    ans = ans * x
  return ans

print(factorial(5))

------------------------- Session 2 -----------------------------------

# Problem set 1. Question 1
def print_list(lst):
  for x in lst:
    print(x)

lsts = ['apple', 'banana', 'carrot']
print_list(lsts)

# Question 5
def max_difference(lst):
    max_val = lst[0]
    min_val = lst[0]

    for num in lst:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

    return max_val - min_val

# Question 9
def find_divisors(n):
  divisors = []
  for i in range(1, n + 1):
      if n % i == 0:
          divisors.append(i)
  return divisors

# Question 10
def fizzBuzz(n):
  for x in range(1, n+1):
    if (x % 3 != 0) and (x % 5 != 0):
      print(x)
    elif (x % 3 == 0) and (x % 5 == 0):
      print('fizzBuzz')
    elif x % 3 == 0:
      print('fizz')
    elif x % 5 == 0:
      print('Buzz')

fizzBuzz(27)

# Question 11
def print_indices(lst):
  for x in range(len(lst)):
    print(x)

lst = [5,1,3,8,2]
print_indices(lst)

# Question 12
def linear_search(lst, target):
  for x in range(len(lst)):
    if lst[x] == target:
      return x
  return -1

print(linear_search([1, 4, 5, 2, 8], 5))

# Section 2, Question 1
def convertTemp(celsius):
  ans = []
  kelvin = celsius + 273.15
  fahrenheit = celsius * 1.80 + 32.00

  ans.append(kelvin)
  ans.append(fahrenheit)
  return ans

temperatures = convertTemp(23.00)
print(temperatures)

# Question 2
def average(scores):
  sum = 0
  for x in scores:
    sum += x
  return sum/len(scores)

lst = [1, 2, 3, 4, 5, 5, 6, 7]
print(average(lst))

# Question 3
def increment_values(lst):
  new_lst = []
  for x in lst:
    new_lst.append(x+1)
  return new_lst

lst = [3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)

# Question 4
def check_num(lst, num):
  for x in lst:
    if x == num:
      return True
  return False

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(flag1)
print(flag2)

# Question 5
def find_missing(nums):
  nums.sort()
  count = 0
  for x in nums:
    if x == count:
      count += 1
  return count

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)

# Question 6
def reverse_list(lst):
  new_lst = []
  for x in lst:
    new_lst.insert(0, x)
  return new_lst

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)

# Question 7
def get_odds(nums):
  lst = []
  for x in nums:
    if x % 2 == 1:
      lst.append(x)
  return lst

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)

# Question 8
def multiplication_table(num):
  for x in range(1, 11):
    print(num * x)

multiplication_table(7)

# Question 9
def list_to_number(digits):
  number = 0
  for digit in digits:
      number = number * 10 + digit
  return number

digits = [1,0,3]
number = list_to_number(digits)
print(number)

# Question 10
def move_zeroes(nums):
  lst = []
  counter = 0
  for x in nums:
    if x != 0:
      lst.append(x)
    else:
      counter += 1
  for _ in range(counter):
    lst.append(0)
  return lst

nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)

# Question 11
def print_odd_indices(nums):
  rang = len(nums)
  for x in range(rang):
    if x % 2 == 0:
      print(nums[x])

nums = [3,4,8,1,5,2]
print_odd_indices(nums)

# Question 12
def find_all_occurrences(lst, target):
  ans = []
  for x in lst:
    if x == target:
      ans.append(x)
  return ans

lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list)
