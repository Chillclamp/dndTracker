import random, uuid

class baseCharacter:
    def __init__(
            self, 
            parent: str = None, name: str = None, race: str = None, alignment: str = None,
            attacks: dict = None,
            alive: bool = True, current_health: int = None, max_health: int = None,
            inventory: list = None, wealth: int = None,
            level: int = None, ability_scores: dict = None, armor_class: int = None, speed: int = None
        ):
        # general
        self.character_id: str = uuid.uuid4()
        self.parent: str = parent
        self.name: str = name
        self.race: str = race
        self.alignment: str = alignment

        # combat
        self.attacks: dict = attacks #{"melee":[], "range":[], "magic":[]}

        # health
        self.alive: bool = alive
        self.current_health: int = current_health
        self.max_health: int = max_health

        # items
        self.inventory: list = inventory
        self.wealth: int = wealth

        # stats
        self.level: int = level
        self.ability_scores: dict = ability_scores #{"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10}
        self.armor_class: int = armor_class
        self.speed: int = speed


    def _get_name(self):
        self.name = 'Not set'

    
    def _get_race(self):
        self.race = 'Not set'


    ###########################
    #    MODIFY ATTRIBUTES    #
    ###########################

    def change_alignment(self, new_alignment: str):
        self.alignment = new_alignment


    def change_attack(self, attack_type: str, attack: object, add: bool = True):
        if type not in ['melee', 'range', 'magic']:
            raise # CUSTOM NOT VALID ATTACK TYPE ERROR

        if add:
            self.attacks[attack_type].append(attack)
        else:
            if attack in self.attacks[attack_type]:
                self.attacks[attack_type].remove(attack)
            else:
                raise # CUSTOM NO ATTACK ERROR


    def change_health(self, value: int):
        # change health
        self.current_health += value

        # is over max health
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        # if under 0 (is dead)
        elif self.current_health < 0:
            self.current_health = 0
            self.alive = False
            raise # CUSTOM ERROR

    
    def change_item(self, item: object, add: bool):
        if add:
            self.inventory.append(item)
        else:
            if item in self.inventory:
                self.inventory.remove(item)
            else:
                raise # CUSTOM NO ITEM ERROR



    def change_parent(self, new_parent: str):
        self.parent = new_parent


    def describe(self):
        return (f'None yet')


# | Sub-class | Chance | Race class |
# |-|-|-|
# | Elven | 25% | wood elf, high elf  |
# | Dwarf | 30% | mountain dwarf, hill dwarf  |
# | Human | 45% | - |

