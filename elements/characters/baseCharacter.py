import random, uuid


class _characterInitError(Exception):
    def __init__(self, message):
        super().__init__(message)


class _characterModifyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class baseCharacter:
    def __init__(
            self, 
            parent: str = None, name: str = None, race: str = None, alignment: str = None,
            attacks: dict = None,
            alive: bool = None, current_health: int = None, max_health: int = None,
            inventory: list = None, wealth: int = None,
            armor_class: int = None, level: int = None, start_ability_score_amount: int = None, speed: int = None,
            charisma: int = None, constitution: int = None, dexterity: int = None, intelligence: int = None, strength: int = None, wisdom: int = None,
        ):
        # general
        if not name:
            raise _characterInitError('Name must be specifed for the creation of a character')
        if not race:
            raise _characterInitError('Race must be specifed for the creation of a character')
    
        self.character_id: str = uuid.uuid4()
        self.parent: str = parent
        self.name: str = name
        self.race: str = race
        self.alignment: str = alignment

        # combat
        self.attacks: dict = attacks #{"melee":[], "range":[], "magic":[]}

        # health
        if not max_health:
            raise _characterInitError('Max health must be specifed for the creation of a character')
        if not current_health:
            current_health = max_health
        if not alive:
            alive = True
            
        self.alive: bool = alive
        self.current_health: int = current_health
        self.max_health: int = max_health

        # items
        if not inventory:
            raise _characterInitError('Inventory must be specified for the creation of a character')
        if not wealth:
            raise _characterInitError('Wealth must be specified for the creation of a character')

        self.inventory: list = inventory
        self.wealth: int = wealth

        # stat validation
        if not start_ability_score_amount:
            raise _characterInitError('Start ablility score amount must be specified for the creation of a character')
        if not armor_class:
            raise _characterInitError('Armor class must be specified for the creation of a character')
        if not level:
            raise _characterInitError('Level must be specified for the creation of a character')
        if not speed:
            raise _characterInitError('Speed must be specified for the creation of a character')

        # assign stats
        self.start_ability_score_amount = start_ability_score_amount
        self.armor_class: int = armor_class
        self.level: int = level
        self.speed: int = speed

        if any(v for v in [charisma, constitution, dexterity, intelligence, strength, wisdom]) and not all(v for v in [charisma, constitution, dexterity, intelligence, strength, wisdom]):
            raise _characterInitError(f'All or None of the ability scores must be set for the creation of a character')

        self.charisma: int  = charisma
        self.constitution: int  = constitution
        self.dexterity: int  = dexterity
        self.intelligence: int  = intelligence 
        self.strength: int  = strength
        self.wisdom: int  = wisdom

        if all(v for v in (charisma, constitution, dexterity, intelligence, strength, wisdom)):
            # all stats are None
            raise _characterInitError("All ability scores are missing")



    def _get_ability_scores(self):
        # set vars
        ability_points = self.start_ability_score_amount + self.level
        abilities = [self.charisma, self.constitution, self.dexterity, self.intelligence, self.strength, self.wisdom]
        
        # add points to abilities
        for point in range(len(ability_points)):
            ability_index = random.randint(0, len(abilities))
            abilities[ability_index] += 1



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

    
    def change_inventory(self, item: object, add: bool):
        if add:
            self.inventory.append(item)
        else:
            if item in self.inventory:
                self.inventory.remove(item)
            else:
                raise # CUSTOM NO ITEM ERROR

    
    def change_wealth(self, value: int):
        # change wealth
        self.wealth += value

        # DEBT system?


    def change_parent(self, new_parent: str):
        self.parent = new_parent


    def describe(self):
        return (f'None yet')