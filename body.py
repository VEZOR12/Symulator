class Pokemon:
    def __init__(self, types: tuple, lvl: int, stats: dict, attacks: list, resistance: dict, name=None, ability=None):
        self.name = name
        self.types = types
        self.lvl = lvl
        self.stats = stats
        self.attacks = attacks
        self.lvl_factor = round(0.9 + 0.1 * self.lvl + 0.0004 * self.lvl * self.lvl, 4)
        self.ability = ability
        self.resistance = {
            'normal': 1,
        }


class Type:
    def __init__(self, name: str, normal_resistance=1.0, fire_resistance=1.0, water_resistance=1.0, grass_resistance=1.0, electric_resistance=1.0, flying_resistance=1.0, psychic_resistance=1.0, poison_resistance=1.0,
                 ghost_resistance=1.0, fighting_resistance=1.0, steel_resistance=1.0, ground_resistance=1.0, rock_resistance=1.0, ice_resistance=1.0, dark_resistance=1.0, bug_resistance=1.0, dragon_resistance=1.0, fairy_resistance=1.0):
        self.name = name
        self.normal_resistance = normal_resistance
        self.fire_resistance = fire_resistance
        self.water_resistance = water_resistance
        self.grass_resistance = grass_resistance
        self.electric_resistance = electric_resistance
        self.flying_resistance = flying_resistance
        self.psychic_resistance = psychic_resistance
        self.poison_resistance = poison_resistance
        self.ghost_resistance = ghost_resistance
        self.fighting_resistance = fighting_resistance
        self.steel_resistance = steel_resistance
        self.ground_resistance = ground_resistance
        self.rock_resistance = rock_resistance
        self.ice_resistance = ice_resistance
        self.dark_resistance = dark_resistance
        self.bug_resistance = bug_resistance
        self.dragon_resistance = dragon_resistance
        self.fairy_resistance = fairy_resistance


normal = Type(name='Normal', fighting_resistance=2, ghost_resistance=0)
fire = Type(name='Fire', fire_resistance=0.5, grass_resistance=0.5, steel_resistance=0.5, bug_resistance=0.5, ice_resistance=0.5, fairy_resistance=0.5, water_resistance=2, ground_resistance=2, rock_resistance=2)
water = Type(name="Water", fire_resistance=0.5, water_resistance=0.5, ice_resistance=0.5, steel_resistance=0.5, grass_resistance=2, electric_resistance=2)
grass = Type(name='Grass', electric_resistance=0.5, grass_resistance=0.5, ground_resistance=0.5, water_resistance=0.5, bug_resistance=2, fire_resistance=2, flying_resistance=2, poison_resistance=2, ice_resistance=2)
electric = Type(name='Electric', electric_resistance=0.5, flying_resistance=0.5, steel_resistance=0.5, ground_resistance=2)
flying = Type(name='Flying', ground_resistance=0, grass_resistance=0.5, fighting_resistance=0.5, bug_resistance=0.5, electric_resistance=2, rock_resistance=2, ice_resistance=2)
psychic = Type(name='Psychic', psychic_resistance=0.5, fighting_resistance=0.5, ghost_resistance=2, dark_resistance=2, bug_resistance=2)
poison = Type(name='Poison', grass_resistance=0.5, poison_resistance=0.5, fighting_resistance=0.5, bug_resistance=0.5, fairy_resistance=0.5, psychic_resistance=2, ground_resistance=2)
ghost = Type(name='Ghost', normal_resistance=0, fighting_resistance=0, bug_resistance=0.5, poison_resistance=0.5, ghost_resistance=2, dark_resistance=2)
fighting = Type(name='Fighting', rock_resistance=0.5, dark_resistance=0.5, bug_resistance=0.5, flying_resistance=2, psychic_resistance=2, fairy_resistance=2)
steel = Type(name='Steel', poison_resistance=0, normal_resistance=0.5, grass_resistance=0.5, flying_resistance=0.5, fairy_resistance=0.5, steel_resistance=0.5, rock_resistance=0.5, ice_resistance=0.5, bug_resistance=0.5, dragon_resistance=0.5, psychic_resistance=0.5, fire_resistance=2, fighting_resistance=2, ground_resistance=2)
ground = Type(name='Ground', electric_resistance=0, poison_resistance=0.5, rock_resistance=0.5, water_resistance=2, grass_resistance=2, ice_resistance=2)
rock = Type(name='Rock', poison_resistance=0.5, normal_resistance=0.5, fire_resistance=0.5, flying_resistance=0.5, water_resistance=2, grass_resistance=2, fighting_resistance=2, steel_resistance=2, ground_resistance=2)
ice = Type(name='Ice', ice_resistance=0.5, fire_resistance=2, rock_resistance=2, fighting_resistance=2,steel_resistance=2)
dark = Type(name='Dark', psychic_resistance=0, dark_resistance=0.5, ghost_resistance=0.5, fighting_resistance=2, bug_resistance=2, fairy_resistance=2)
bug = Type(name='Bug', fighting_resistance=0.5, grass_resistance=0.5, ground_resistance=0.5, fire_resistance=2, flying_resistance=2, rock_resistance=2)
dragon = Type(name='Dragon', fire_resistance=0.5, water_resistance=0.5, grass_resistance=0.5, electric_resistance=0.5, ice_resistance=2, dragon_resistance=2, fairy_resistance=2)
fairy = Type(name='Fairy', dragon_resistance=0, fighting_resistance=0.5, dark_resistance=0.5, bug_resistance=0.5, poison_resistance=2, steel_resistance=2)

def final_resistance(type1, type2):
