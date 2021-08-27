'''
    CS5001
    Fall 2019
    Homework 7 / Final Project
    ALIGN Quest
    Old-School Adventure game to gain more experience with Classes,
    Objects, Files, Lists, Program Decomposition, and almost
    everything else we touched on in the course

    This file contains the starter code for the game's Rooms, Puzzles and
    Monsters. Left to:do for the student: Build out the Item class.
    The rest of the framework can be extended, but works as-is
'''

'''
    class: Room
    Description:
    This class encapsulates all of the behavior for the "areas" in our
    virtual world. A room is a general idea; rooms might be anywhere
    the player can explore by stepping into them (e.g. closets, boxes)
    Each room has a description and can contain items. Some rooms
    may have a puzzle to solve or a "monster" (our monsters are cute,
    furry animals or toys) that protect the room. If a monster or puzzle
    is present, the user must "deactivate" said puzzle/monster before
    the full room description is presented to them
'''
    
class Room:
    def __init__(self, number = 0, name = 'n/a',
                 description = 'trapped!', adjacent = [], picture = ''):
        self.name = name
        self.number = number
        self.description = description
        self.adjacent_rooms = adjacent
        self.picture = picture
        self.items = []
        self.puzzles = []
        self.monsters = []
    def add_item(self, item): # add an item to the room
        self.items.append(item)
    def add_puzzle(self, puzzle): # add a puzzle to the room
        self.puzzles.append(puzzle)
    def add_monster(self, monster): # add a monster to the room
        self.monsters.append(monster)
    def has_items(self):            # answer if the room has items or not
        return not (len(self.items) == 0)
    def has_puzzle(self):           # does the room have puzzles?
        return not (len(self.puzzles) == 0)
    def has_monsters(self):         # answer if monster is in the room
        return not (len(self.monsters) == 0)
    def reverse_effects(self):      # reverse effects of puzzle/monster
        for i in range(len(self.adjacent_rooms)):
            if self.adjacent_rooms[i] < 0: # blocked by a puzzle or monster
                self.adjacent_rooms[i] = 0 - self.adjacent_rooms[i] # make it open
    def contextual_description(self):
        if self.has_puzzle(): # puzzle blocks regular description. 
            for each in self.puzzles:
                if (each.target == self and
                    each.active and
                    each.affects_target):
                    return each.do_effect()
        # if no puzzles/monsters are active, return regular description
        return self.description 
    def __str__(self):
        return (str(self.number) + ':' + self.name + ':' + self.description)

'''
    class: Item
    Description:
    This class encapsulates all of the behavior for the "things" in our
    rooms. Items can be collected by the player by Taking them during
    their quest. Items also have a description that players can see when
    they Look at the item. Players can also Drop or Use items
    For this prototype, puzzles and monsters CAN be attached to items
    (just like rooms) but the framework doesn't fully support the
    resolution of solutions for those puzzles on objects yet.
    reverse_effects() is future work, so you can leave it as a "pass"
    in your code
'''
class Item:
    def __init__(self, number = 0, name = 'n/a',
                 description = '', weight = 0, value = 0, use = 0):
        self.name = name
        self.number = number
        self.description = description
        self.weight = weight
        self.value = value
        self.use_remaining = use
        self.puzzle = ''
        self.description = description
        
    # does the item have any use left, or is it used up?
    def has_use_remaining(self):
        if self.use_remaining > 0:
            return True
        return False
    
    def reverse_effects(self):
        pass # to:do for version 2

    # answer if the Item has a puzzle or not
    def has_puzzle(self):
        if self.puzzle == '':
            return False
        return True
    
    # try to use the item (on a puzzle or monster)
    def use(self):
        # if the item has some uses remaining (e.g. use_remaining > 0)
        # then decrement use_remaining by 1 AND
        # return a 2-tuple with the item name and True
        # otherwise, return a 2-tuple with item name and False
        #pass
        if has_use_remaining(self) == True:
            self.use_remaining -= 1
            return self.name, True
        return self.name, False

'''
    class: Puzzle
    Description:
    This class encapsulates all of the behavior for the challenges in our
    rooms. Puzzle is a general term...right now it's not some hard problem
    to solve, but currently the use of some ITEM to "neutralize" the problem
    or monster the player encounters. E.g. a glass of water might neutralize
    a FIRE puzzle
    If puzzles are active, they occlude the regular description of a room
    Items neutralize puzzles and deactivate them
'''
class Puzzle:
    def __init__(self, name = 'n/a',description = '', target = '',
                 active = True, affects_target = False,
                 solution = '', effect = ''):
        self.name = name
        self.description = description
        self.active = active
        self.affects_target = affects_target
        self.solution = solution
        self.target = target
        self.effect = effect
    def activate(self):
        self.active = True
    def deactivate(self):
        self.active = False
    def is_active(self):
        return self.active
    def do_effect(self):
        return self.effect
    def try_to_solve(self, solution):
        if solution.upper() == self.solution.upper():
            self.deactivate()
            return True
        return False

'''
    class: Monster
    Description:
    This class is a subtype of Puzzle that can "attack" the user.
    All of our monsters are soft and furry creatures so they can't
    really hurt the user (no need for inducing PTSD in a computer game)
    Like their superclass, they occlude the regular room description
    until they are neutralized
'''
class Monster(Puzzle):
    def __init__(self, name = 'n/a',description = '', target = '',
                 active = True, affects_target = False,
                 solution = '', effect = '',
                 can_attack = True, attack = 'Cotton Balls'):
        super().__init__(name, description, target,
                         active, affects_target, solution, effect)
        self.can_attack = can_attack
        self.attack = attack
    def do_effect(self):
        return self.effect + '\n' + self.do_attack()
    def do_attack(self):
        return self.name + ' ' + self.attack
    def defeated(self):
        return 'The ' + self.name + ' has been defeated. It is not moving.'

'''
    class: Game
    Description:
    This class encapsulates all of the behavior for the challenges in the game.
    I believe that these classes could have been called in the main/or functions
    in the align_quest file. I did not get the opportunity to finish this class,
    however it gave me a slightly better understanding to classes and objects.
'''   

class Game:
    def __init__(self, item_dict, room_dict, puzz_n_mon_dict, target = '' ):
        self.puzzle_n_monsters = []
        self.rooms = []
        self.item_dict = item_dict
        self.room_dict = room_dict
        self.puzz_n_mon_dict = puzz_n_mon_dict
        self.target = target
            
    def add_rooms(self, room_dict):
        for key, value in room_dict:
            self.rooms.append(value)
    
    def add_puz_mon(self, puzz_mon_dict):
        for key, value in puzz_mon_dict:
            self.puzzle_n_monsters.append(value)
            
    def link(self):
        for puz_mon in self.puzzles_n_monsters:
            if 'Room' in puzz_mon.target:
                room_str = puzz_mon.target.split(puzz_mon)
                puzz_mon.target = self.rooms[int(room_str[1])]
                self.rooms[int(room_str[1]) - 1].add_puzzle(puz_mon)
