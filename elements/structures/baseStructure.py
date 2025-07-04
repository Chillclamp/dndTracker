class baseStructure:
    def __init__(self, name: str, location: dict, materials: list):
        self.name = name              # e.g., "Stone Cottage"
        self.location = location      # e.g., (x, y) coordinates or village name
        #self.materials = materials    # e.g., ["wood", "stone"]

    def describe(self):
        return (f"{self.name} located at {self.location}, size: {self.size}, "
                f"built with: {', '.join(self.materials)}.")


class settlemant(baseStructure):
    def __init__(self, name, location, materials):
        super().__init__(name, location, materials)



########################################
# Settlement
# Strucure [REcreaton]

# method:
#    make struct(an amount)
#       loped
#       random num(0-100)
#           if num < 50 
#               make stall class
#           elif num 50 - 90:
#               make shop class
#           else:
#               make market class
#       add new class to struct's struct list


#########################################
# Trade - Stall
# pick trade class(s) form random?
# random pick num of trades
# for loop
# pull item from database where relevent trade class
# num of items 
#    method -> item traded 
#   method -> restock


#######################################
# # CHARS
#######################################
# Base class
# name
# 

# elven class
#       wood elf
#       elder elf

# dwarf 

# CHAR PROFESIUON
# trader
# 
# 