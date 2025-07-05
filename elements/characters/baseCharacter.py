import random

class baseCharacter:
    def __init__(self, name: str, alignment: str, location: dict):
        self.name = name 
        self.alignment = alignment
        self.location = location
        
        race_gen = random.randint(1,100)
        sub_race_gen = random.randint(1,100)
        
        # Is this how its gonna work?
        
        if race_gen <= 25:
            if sub_race_gen <= 30:
                high_elf()
            elif sub_race_gen <=100:
                wood_elf()
        
        elif race_gen <= 55:
            if sub_race_gen <= 20:
                mountain_dwarf()
            elif sub_race_gen <= 100:
                hill_dwarf()
        
        else:
            
            # STILL NEED TO ADD SUB RACES IE WHITE, BLACK, ASIAN ETC.
            
            human()

    def describe(self):
        return (f"{self.name} located at {self.location}, race: {self.race}, sub_race: {self.sub_race}, alignment: {self.alignment}.")
    
    



class elf():
    def __init__(self, sub_race: str):
        self.subrace = sub_race
        
        pass

class wood_elf(elf):
    def __init__(self, sub_race):
        super().__init__(sub_race)

class high_elf(elf):
    def __init__(self, sub_race):
        super().__init__(sub_race)

class dwarf:
    def __init__(self, sub_race: str):
        self.subrace = sub_race
        pass

class mountain_dwarf(dwarf):
    def __init__(self, sub_race):
        super().__init__(sub_race)

class hill_dwarf(dwarf):
    def __init__(self, sub_race):
        super().__init__(sub_race)

class human():
    def __init__(self, sub_race: str):
        self.subrace = sub_race
        
        pass
        


# | Sub-class | Chance | Race class |
# |-|-|-|
# | Elven | 25% | wood elf, high elf  |
# | Dwarf | 30% | mountain dwarf, hill dwarf  |
# | Human | 45% | - |


