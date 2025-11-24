from baseCharacter import baseCharacter

class elf(baseCharacter):
    def __init__(self, name, alignment, location):
        super().__init__(name, alignment, location)
        

class wood_elf(elf):
    def __init__(self, sub_race):
        super().__init__(sub_race)

class high_elf(elf):
    def __init__(self, sub_race):
        super().__init__(sub_race)