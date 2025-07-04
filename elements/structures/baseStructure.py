class baseStructure:
    def __init__(self, name: str, location: dict, materials: list):
        self.name = name              # e.g., "Stone Cottage"
        self.location = location      # e.g., (x, y) coordinates or village name
        #self.materials = materials    # e.g., ["wood", "stone"]

    def describe(self):
        return (f"{self.name} located at {self.location}, size: {self.size}, "
                f"built with: {', '.join(self.materials)}.")

class settlement(baseStructure):
    def __init__(self, name, location, materials):
        super().__init__(name, location, materials)


