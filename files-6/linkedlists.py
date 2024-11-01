'''----------------------------------------------------Session One----------------------------------------------------------'''
'''Problem 1: Merge Sorted Lists
Using the two pointer approach, write a function merge_sorted_lists() that takes in two sorted lists lst1 and lst2 as parameters and merges them into a single sorted list. The function returns the new list.'''

def merge_sorted_lists(lst1, lst2):
  first, second = 0, 0
  lst = []
  while first < len(lst1) and second < len(lst2):
    if lst1[first] < lst2[second]:
      lst.append(lst1[first])
      first += 1
    else:
      lst.append(lst2[second])
      second += 1
  while first < len(lst1):
    lst.append(lst1[first])
    first += 1
  while second < len(lst2):
    lst.append(lst2[second])
    second += 1
  return lst

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged_lst = merge_sorted_lists(lst1, lst2)
print(merged_lst)

'''Problem 2: Checking Subsequence
Write a function is_subsequence that takes in two strings s and t as parameters and returns True if s is a subsequence of t and False otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some or none of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).'''

def is_subsequence(s, t):
  first, second = 0, 0
  while first < len(s) and second < len(t):
    if s[first] == t[second]:
      first += 1
    second += 1
  return len(s) == first

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))
a = "cba"
b = "ahbgdc"
print(is_subsequence(a, b))

'''Problem 3: Sort List by Parity
Write a function sort_array_by_parity() that takes in a list of integers nums where half of the integers are odd, and the other half are even. The function sorts the list so that whenever nums[i] is odd, i is odd and whenever nums[i] is even, i is even. The function returns the list in any order that satisfies the condition.'''

def sort_array_by_parity(nums):
  first, second = 0, len(nums) - 1
  while first < second:
    if nums[first] % 2 != 0 and first % 2 == 0:
      if nums[second] % 2 == 0 and second % 2 != 0:
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp
    elif nums[first] % 2 == 0 and first % 2 != 0 and nums[second] % 2 != 0 and second % 2 == 0:
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp
    first += 1
    second -= 1
  return nums

nums = [4,2,5,7]
nums2 = [2,3]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

'''Problem 4: Merge to Palindrome
Write a function min_merge_operations() that takes in a list of non-negative integers nums and returns the minimum number of merge operations to make it a palindrome. A merge operation is adding two of the integers.'''

def min_merge_operations(nums):
  first, second = 0, len(nums) - 1
  count = 0
  while first < second:
    if nums[first] == nums[second]:
      first += 1
      second -= 1
    elif nums[first] < nums[second]:
      nums[first + 1] += nums[first]
      count += 1
      first += 1
    else:
      nums[second + 1] += nums[second]
      count += 1
      second += 1
  return count 

nums = [6,1,3,7]
print(min_merge_operations(nums))
nums2 = [1,3,3,1]
print(min_merge_operations(nums2))
nums3 = [1,3,2,7]
print(min_merge_operations(nums3))

'''Problem 5: Averages of Subarray
Use the sliding window technique to solve the following problem:
Write a function find_averages_of_subarrays() that takes in a list of integers nums and an integer k as parameters. The function returns a list where each element in the average of each contiguous subarray of size k in nums where 1 ≤ k ≤ len(nums)'''

def find_averages_of_subarrays(k, nums):
  lst = []
  for x in range(len(nums) - k + 1):
    window = nums[x:x+5]
    count = 0
    for i in window:
      count += i
    lst.append(count / k)
  return lst

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avg_lst = find_averages_of_subarrays(5, nums)
print(avg_lst)

'''Problem 6: Greater Than Threshold
Write a function num_of_subarrays() that takes in a list of integers nums and two integers k and threshold as parameters. The function returns the number of subarrays of size k whose average is greater than or equal to threshold.'''

def num_of_subarrays(lst, k, threshold):
  ans = 0
  for x in range(len(lst) - k + 1):
    window = lst[x:x+k]
    count = 0
    for i in window:
      count += i
    if count / k >= threshold:
      ans += 1
  return ans

nums = [2,2,2,2,5,5,5,8]
count = num_of_subarrays(nums, 3, 4)
print(count)

'''Problem 2: Create Squirtle
Step 2: Instantiate an instance of the class Pokemon and store it in a variable named squirtle. The Pokemon instance created should have name "Squirtle" and its types should be ["Water"].
Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.'''

class Pokemon:
  def __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = False

  def print_pokemon(self):
    print({
      "name": self.name,   # Output: "name": "Squirtle",
      "types": self.types, # Output: "types": ["Water"],
      "is_caught": self.is_caught # Output: "is_caught": False
    })

squirtle = Pokemon('Squirtle', ['Water'])
squirtle.print_pokemon()

'''Problem 3: Is Caught
Using your code from Problem 2, update your squirtle Pokemon so that is_caught is updated to True. Use the print_pokemon() function to verify that squirtle's is_caught property was updated.
Expected Output:
{
  "name": "Squirtle",
  "types": ["Water"],
  "is_caught": True
}'''

squirtle = Pokemon('Squirtle', ['Water'])
squirtle.is_caught = True
squirtle.print_pokemon()

'''Problem 4: Catch Pokemon
Update the Pokemon class with a new method catch() that takes in no parameters except self.
The method should update the Pokemon's is_caught attribute to True and not return any value.'''

class Pokemon:
  def __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = False
  def print_pokemon(self):
    print({
      "name": self.name,   # Output: "name": "Squirtle",
      "types": self.types, # Output: "types": ["Water"],
      "is_caught": self.is_caught # Output: "is_caught": False
    })
  def catch(self):
    self.is_caught = True

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()
my_pokemon.catch()
my_pokemon.print_pokemon()

'''Problem 5: Choose Pokemon
Update the Pokemon class with a new method choose() that takes in no parameters except self.
If the Pokemon is caught, the method should print the string "<Pokemon name> I choose you!".
Otherwise, it should print "<Pokemon name> is wild! Catch them if you can!".'''

class Pokemon:
  def __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = False
  def print_pokemon(self):
    print({
      "name": self.name,   # Output: "name": "Squirtle",
      "types": self.types, # Output: "types": ["Water"],
      "is_caught": self.is_caught # Output: "is_caught": False
    })
  def catch(self):
    self.is_caught = True
  def choose(self):
    if self.is_caught:
      print(f'{self.name} I choose you.')
    print(f'{self.name} is wild! Catch them if you can!')

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()
my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()

'''Problem 6: Add Pokemon Type
Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.
It should add new_type to the Pokemon's list of types.'''

class Pokemon:
  def __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = False
  def print_pokemon(self):
    print({
      "name": self.name,   # Output: "name": "Squirtle",
      "types": self.types, # Output: "types": ["Water"],
      "is_caught": self.is_caught # Output: "is_caught": False
    })
  def catch(self):
    self.is_caught = True
  def choose(self):
    if self.is_caught:
      print(f'{self.name} I choose you.')
    print(f'{self.name} is wild! Catch them if you can!')
    
  def add_type(self, new_type):
    self.types.append(new_type)

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()
jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()

'''Problem 7: Get Pokemon
Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.
The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.
Hint: To test, loop over Pokemon in return list and print the Pokemon's name'''

class Pokemon:
  def __init__(self, name, types):
    self.name = name
    self.types = types
    self.is_caught = False

  def print_pokemon(self):
    print({
      "name": self.name,   # Output: "name": "Squirtle",
      "types": self.types, # Output: "types": ["Water"],
      "is_caught": self.is_caught # Output: "is_caught": False
    })

  def catch(self):
    self.is_caught = True

  def choose(self):
    if self.is_caught:
      print(f'{self.name} I choose you.')
    print(f'{self.name} is wild! Catch them if you can!')

  def add_type(self, new_type):
    self.types.append(new_type)

def get_by_type(my_pokemon, pokemon_type):
  have_type = []
  for pokemon in my_pokemon:
    if pokemon_type in pokemon.types:
      have_type.append(pokemon)
  return have_type

jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])
my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
have_type = get_by_type(my_pokemon, "Normal")
for pokemon in have_type:
  print(pokemon.name)

'''Problem 8: Pokemon Evolution
Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, each instance of Pokemon has an 
attribute evolution. The attribute will either be the default value of None or another Pokemon instance.
Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter.
The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.'''

class Pokemon():
  def  __init__(self, name, types, evolution = None):
    self.name = name
    self.types = types
    self.is_caught = False
    self.evolution = evolution

def get_evolutionary_line(starter_pokemon):
  evolution = [starter_pokemon]
  current_pokemon = starter_pokemon
  while current_pokemon.evolution is not None:
    evolution.append(current_pokemon.evolution)
    current_pokemon = current_pokemon.evolution
  return evolution

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)
evolution = get_evolutionary_line(charmander)
for pokemon in evolution:
  print(pokemon.name)

'''Problem 9: Node Class
Using the provided Node class below, create two nodes:
The first node should have value a and be stored in a variable node_one.
The second node should have value b and be stored in a variable node_two.
You do not need to connect the nodes together yet.'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
node_one = Node('a')
node_two = Node('b')
node_one.next = node_two
print(node_one.value) 
print(node_one.next) 
print(node_two.value)
print(node_two.next)

'''Problem 11: Mario Party
Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list given the Node class:'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
node_4 = Node('Toad')
node_3 = Node('Wario', node_4)
node_2 = Node('Luigi', node_3)
node_1 = Node('Mario', node_2)
#a lternative
head = Node('Mario')
second = Node('Luigi')
third = Node('Wario')
tail = Node('Toad')
head.next = second
second.next = third
third.next = tail

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

'''Problem 12: Printing Linked List
Write a function print_linked_list() that takes in a head node as a parameter and prints the linked list using the 
string " -> " to separate each node
Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.value)
        current = current.next
    print(" -> ".join(values))
a = Node('a', Node('b', Node('c', Node('d', Node('e')))))
print_linked_list(a)

# ----------------------------------------------------Session TWO----------------------------------------------------------

'''Problem 3: Verify Update
Step 1: Using the same Card class from Problem 2, update your code so that the suit of card 
is "Hearts" instead of "Clubs".

Step 2: Use the print_card() method to verify that card was updated'''

class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	def print_card(self):
		print(f"{self.rank} of {self.suit}")

card = Card('Clubs', 'Ace')
card.suit = 'Hearts'
card.print_card()



class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    def is_valid(self):
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        return self.suit in suits and self.rank in ranks

    def get_value(self):
        if not self.is_valid():
            return None
        
        if self.rank.isdigit():  # Convert rank to int if it's a digit (like '2' to '10')
            return int(self.rank)
        elif self.rank == 'Ace':
            return 1
        elif self.rank == 'Jack':
            return 11
        elif self.rank == 'Queen':
            return 12
        elif self.rank == 'King':
            return 13
        return None


class Hand:
    def __init__(self):
        self.cards = []

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def add_card(self, card):
        self.cards.append(card)


def sum_hand(hand):
    count = 0
    for card in hand.cards:  # Iterate over hand.cards
        if not card.is_valid():
            return None
        count += card.get_value()
    return count


# Example usage
card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

hand_sum = sum_hand(hand)
print(hand_sum)  # Output: 17

'''Problem 7: Sum of Cards
Write a function sum_hand() that takes in an instance of Hand as a parameter and 
returns the summed value of all cards in the hand.

Use the methods from Problems 5-7 to assist you.
If any card in the hand is invalid, return None.'''

class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	def print_card(self):
		print(f"{self.rank} of {self.suit}")
	def is_valid(self):
		first = ["Hearts", "Spades", "Clubs", "Diamonds"]
		second = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		return self.suit in first and self.rank in second
	def get_value(self):
		if not self.is_valid():
			return None
		if self.rank.isdigit():
			return int(self.rank)
		elif self.rank == 'Ace':
			return 1
		elif self.rank == 'Jack':
			return 11
		elif self.rank == 'Queen':
			return 12
		elif self.rank == 'King':
			return 13
		return self.rank

class Hand:
    def __init__(self):
        self.cards = []
    def remove_card(self, card):
        self.cards.remove(card)
    def add_card(self, card):
        self.cards.append(card)
	
def sum_hand(hand):
	count = 0
	for x in hand.cards:
		if not x.is_valid():
			return None
		count += x.get_value()
	return count

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum)

'''Problem 9: Head and Tail Nodes
A linked list is a new data type that, similar to a normal list or array, allows us to 
store pieces of data sequentially. The difference between a linked list and a normal list
lies in how each element is stored in a computer’s memory.
Using the provided Node class below, create two nodes.
The first node should have value 100 and be stored in a variable head.
The second node should have value 200 and be stored in a variable tail.
Set head to point to tail.'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
head = Node(100)
tail = Node(200)
head.next = tail
print(head.value) 
print(head.next) 
print(tail.value) 
print(tail.next)

'''Problem 12: Printing Linked List
Write a function print_linked_list() that takes in a head node as a parameter and prints the linkedlist using the string " -> " to separate each node.

Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next= next

def print_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.value)
        current = current.next
    print(" -> ".join(values))

# input linked list: a->b->c->d->e
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
print_linked_list(a)

'''Problem 8: Print Hand
The class Card has been updated below with a new attribute next to represent the card that comes
after it in a hand of cards.
Write a function print_hand() that accepts a Card object and returns a list of all cards in the hand
that come after it.'''
class Card():
    def  __init__(self, suit, rank, next = None):
        self.suit = suit
        self.rank = rank
        self.next = next
    def print_card(self):
        print(f"{self.rank} of {self.suit}")
    def is_valid(self):
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        if self.suit in suits and self.rank in ranks:
            return True
        return False
    def get_value(self):
        num_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        if not self.is_valid():
            return None
        elif self.rank == 'Ace':
            return 1
        elif self.rank == 'Jack':
            return 11
        elif self.rank == 'Queen':
            return 12
        elif self.rank == 'King':
            return 13
        return int(self.rank)
    
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def remove_card(self, card):
        self.cards.remove(card)

def sum_hand(hand):
    count = 0
    for card in hand.cards:
        if not card.is_valid():
            return None
        count += card.get_value()
    return count

def print_deck(starting_card):
    cards = []
    current = starting_card
    while current:
        cards.append(current)
        current = current.next
    return cards

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")
card_one.next = card_two
card_two.next = card_three
print(print_deck(card_one))


'''Problem 11: Zodiac Signs
Create the list ["aries", "taurus", "gemini", "cancer"] as a linked list using the Node class:
Example Usage (after completing the problem with variable names node_1, node_2, node_3, and node_4.):
'''

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
node_1 = Node('aries')
node_2 = Node('taurus')
node_3 = Node('gemini')
node_4 = Node('cancer')
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

'''Problem 12: Print Linked List
Write a function print_linked_list() that takes in a head of a linked list as a parameter.
The function prints and returns a list of all the values in the linked list in the order they appear in
the linked list.

Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a
normal list.
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		

def print_linked_list(head):
    lst = []
    current = head
    while current.next:
        lst.append(current.value)
        current = current.next
    print(lst)

# input linked list: a->b->c->d->e
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
print_linked_list(a)

class Player():
    def __init__(self, character, kart, opponent=None):
        self.character = character 
        self.kart = kart
        self.items = []
        self.ahead = opponent
    def get_player(self):
        return f"{self.character} driving the {self.kart}"  
    def set_player(self, name):
        valids = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
        if name in valids:
            self.character = name
            print('Character updated')
        else:
            print('Invalid character')
    def add_item(self, item_name):
        valids = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
        if item_name in valids:
            self.items.append(item_name)
    def print_inventory(self):
        if len(self.items) == 0:
            print('Inventory empty')
        count_dict = {}
        for item in self.items:
            if item not in count_dict:
                count_dict[item] = 1
            else:
                count_dict[item] += 1
        ans = ' '.join(f'{item}: {count}' for item, count in count_dict.items())
        print(ans)

def print_results(race_results):
    for index, name in enumerate(race_results, start = 1):
        print(f'{index}. {name.character}')

'''Problem 12: Chase String
Write a function chase_list() that takes in a head of a linked list and returns a string linking
together the values of the list with the separator "chases".

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a
normal list.'''

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def chase_list(self):
    lst = [self.value]
    current = self.next
    while current:
        lst.append(current.value)
        current = current.next
    return ' chases '.join(lst)

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")
dog.next = cat
cat.next = mouse
mouse.next = cheese
print(chase_list(dog))

'''--------------------------------Session TWO------------------------------------------'''
'''Problem 8: Linked Listify
Write a function list_to_linked_list() that takes in a list lst as a parameter and
converts it to a linked list. The function should return the head of the linked list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def list_to_linked_list(lst):
	pass
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self. next = next
    
def list_to_linked_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for x in lst[1:]:
        current.next = Node(x)
        current = current.next
    return head.value

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print(linked_list) # Only prints the head element!

'''Problem 9: Doubly Linked List
One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node
only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked
list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Given the Node class for a doubly linked list below, recreate the list ["Poliwag", "Poliwhirl",
"Poliwrath"] as a doubly linked list.

class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
Example Usage: (after completing the problem with variable names poliwag, poliwhirl, and poliwrath):
'''

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

poliwhirl = Node('Poliwhirl')
poliwrath = Node('Poliwrath')
poliwag = Node('Poliwag')
poliwhirl.next = poliwrath
poliwhirl.prev = poliwag
poliwag.next = poliwhirl
poliwrath.prev = poliwhirl
print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)

'''Problem 10: Print Backwards
Write a function print_reverse() that takes in the tail of a doubly linked list as a parameter.

It should print out the values of the linked list in reverse order, each separated by a space.

#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
'''

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    
def print_reverse(tail):
    if tail is None:
        return None
    lst = [tail.value]
    current = tail.prev
    while current:
        lst.append(current.value)
        current = current.prev
    return ' '.join(lst)

poliwhirl = Node('Poliwhirl')
poliwrath = Node('Poliwrath')
poliwag = Node('Poliwag')
poliwhirl.next = poliwrath
poliwhirl.prev = poliwag
poliwag.next = poliwhirl
poliwrath.prev = poliwhirl
print(print_reverse(poliwrath))

'''Problem 1: Poker Two-Pair Hand
In poker, players are given a hand of five cards. A player has a "two-pair" hand if they have two
cards of the same rank and another two cards of another rank. The fifth card isn’t used here.

Given the Card class below, write a function is_two_pair() that takes in a list player_hand that
contains 5 Card objects.

The function returns True if the player has a two pair hand and False otherwise.
Cards in the hand are guaranteed to be unique and are guaranteed to have on the following suits
and ranks:
'''

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

def is_two_pair(player_hand):
    rank_count = {}
    for card in player_hand:
        if card.rank in rank_count:
            rank_count[card.rank] += 1
        else:
            rank_count[card.rank] = 1
    count = 0
    for x in rank_count.values():
        if x == 2:
            count += 1  
    return count == 2

card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")
player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))
player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))

'''Problem 4: Linked List Length
Write a function ll_length() that takes in a head of a linked list as a parameter and returns
the length of the linked list.

# Linked List: num1 -> num2 -> num3
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def ll_length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

num1 = Node('1')
num2 = Node('2')
num3 = Node('3')
head = num1
num1.next = num2
num2.next = num3
print(ll_length(head))
# Empty Linked List
head = None
print(ll_length(head))

'''Problem 5: Delete Tail
Write a function delete_tail() that takes in a head of a linked list as a parameter and removes
the tail from the end of the list.

The function does not need to return any value, as it modifies the linked list in place.

Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal
list.'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def delete_tail(head):
    if head is None or head.next is None:
        return None
    
    previous = None
    current = head

    while current.next is not None:
        previous = current
        current = current.next
    previous.next = None
        
num1 = Node('1')
num2 = Node('2')
num3 = Node('3')
num1.next = num2
num2.next = num3
delete_tail(num1)
print(num1.next.value)

'''Problem 6: Greatest Node
Write a function find_max() that takes in a head of a linked list as a parameter where each node
is an integer value.

The function should return the maximum value in the linked list.

# linked list: num1 -> num2 -> num3 -> num4
max_val = find_max(num1)
print(max_val)'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_max(head):
    highest = 0
    current = head
    while current:
        if current.value > highest:
            highest = current.value
        current = current.next
    return highest

num4 = Node(10)
num3 = Node(30, num4)
num2 = Node(15, num3)
num1 = Node(20, num2)
max_val = find_max(num1)
print(max_val)

'''Problem 7: Pop Node
Write a function ll_pop() that takes in the head of a linked list and an index i as parameters.

The function should remove the node at index i of the linked list and return the head of the list.

If i is greater than the length of the list, do nothing.
Hint: Linked lists do not have built-in indices so you will need to track the indices yourself.

# linked list: num1 -> num2 -> num3
ll_pop(num1, 1)
# result: num1 -> num3'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_pop(head, i):
    if head is None or i < 0:
        return None

    if i == 0:
        return head.next

    previous = None
    current = head
    count = 0

    while current is not None and count < i:
        previous = current
        current = current.next
        count += 1
    if current is not None and previous.next is not None:
        previous.next = current.next
    
    return head

num4 = Node(10)
num3 = Node(30, num4)
num2 = Node(15, num3)
num1 = Node(20, num2)
ll_pop(num1, 1)

'''Problem 8: Find Middle Node
Write a function find_middle_node() that takes in the head of a linked list and returns the
"middle" node.

If the linked list has an even length and there are two "middle" nodes, return the first middle node.
(E.g., "1 -> 2 -> 3 -> 4" would return 2, not 3.)

# linked list: num1 -> num2 -> num3 -> num4
head = num1
mid = find_middle_node(head)
# mid == num2'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def ll_length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def find_middle_node(head):
    length = ll_length(head)
    middle_index = (length - 1)// 2
    
    current = head
    current_index = 0
    while current_index < middle_index:
        current = current.next
        current_index += 1
    
    return current.value

num4 = Node(4)
num3 = Node(3)
num2 = Node(2)
num1 = Node(1, num2)
head = num1
mid = find_middle_node(head)
print(mid)

'''Problem 9: Create Double Links
One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node
only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly
linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Update the Node constructor below so that the code creates a doubly linked list with head <-> tail.'''

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

head = Node("First")
tail = Node("Last")

head.next = tail
tail.prev = head

print(head.value, "<->", head.next.value)
print(tail.prev.value, "<->", tail.value)


'''Problem 10: Double to Single
Below are the node classes for a singly linked list and a doubly linked list.
Write a function dll_to_sll() that takes in the head of a doubly linked list as a parameter
and recreates it as a singly linked list.

The function returns the head of the new singly linked list.

# DLL: Ice <-> Water <-> Steam
dll_head = Ice
sll_head = dll_to_sll(dll_head)
#SLL: Ice -> Water -> Steam'''

class SLLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class DLLNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value 
        self.next = next
        self.prev = prev
    
def dll_to_sll(dll_head):
    mock_head = SLLNode(None)
    current_sll = mock_head
    current_dll = dll_head

    while current_dll:
        new_node = SLLNode(current_dll.value)
        current_sll.next = new_node
        current_sll = current_sll.next
        current_dll = current_dll.next

    return mock_head.next

steam = DLLNode('Steam')
water = DLLNode('Water', steam)
ice = DLLNode('Ice', water)
dll_head = ice
sll_head = dll_to_sll(dll_head)
print(sll_head.value)