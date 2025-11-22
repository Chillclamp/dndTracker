from baseCharacter import baseCharacter

class dwarf(baseCharacter):
    def __init__(self, name, alignment, location):
        super().__init__(name, alignment, location)

class mountain_dwarf(dwarf):
    def __init__(self, sub_race):
        super().__init__(sub_race)

class hill_dwarf(dwarf):
    def __init__(self, sub_race):
        super().__init__(sub_race)