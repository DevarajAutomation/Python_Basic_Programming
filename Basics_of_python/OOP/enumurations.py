from enum import Enum,unique,auto

@unique
class Fruits(Enum):

    ORANGE = 1
    BANANA = 2
    GRAPE  = 3
    GOLD = auto()

print(Fruits.GOLD.name)
print(Fruits.GOLD.value)