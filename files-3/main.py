'''
CP: https://courses.codepath.org/courses/tip101/unit/5#!session_one
Answers: https://github.com/codepath/compsci_guides/wiki/Unit-5-Session-1
'''

'''
Next problem: 8
'''

class Player():
    def __init__(self, character, kart):
        self.character = character 
        self.kart = kart
        self.items = []  
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