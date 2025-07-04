class baseCharacter:
    def __init__(self, name: str, race: str, sub_race: str, alignment: str, location: dict):
        self.name = name 
        self.race = race
        self.sub_race = sub_race
        self.alignment = alignment
        self.location = location

    def describe(self):
        return (f"{self.name} located at {self.location}, race: {self.race}, sub_race: {self.sub_race}, alignment: {self.alignment}.")



class elf:
    def __init__(self):
        pass

class wood_elf(elf):
    def __init__(self):
        super().__init__()

class high_elf(elf):
    def __init__(self):
        super().__init__()
        


# | Sub-class | Chance | Race class |
# |-|-|-|
# | Elven | 25% | wood elf, high elf  |
# | Dwarf | 30% | mountain dwarf  |
# | Human | 45% | - |


