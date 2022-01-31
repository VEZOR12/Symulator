import time
from random import randrange


class Move:
    def __init__(self, power=None, accuracy=None, type=None, category=None, contact=None, priority=0,
                 critical_chance=1):
        self.power = power
        self.accuracy = accuracy
        self.type = type
        self.category = category
        self.contact = contact
        self.priority = priority
        self.critical_chance = critical_chance
        # todo: effects


class Pokemon:
    def __init__(self, types: tuple, lvl: int, stats: dict, attacks: list, name=None, ability=None, resistance=None):
        self.name = name
        self.types = types
        self.lvl = lvl
        self.stats = stats
        self.attacks = attacks
        self.lvl_factor = round(0.9 + 0.1 * self.lvl + 0.0004 * self.lvl * self.lvl, 4)
        self.ability = ability
        self.resistance = resistance


class Type:
    def __init__(self, name: str, normal_resistance=1.0, fire_resistance=1.0, water_resistance=1.0,
                 grass_resistance=1.0, electric_resistance=1.0, flying_resistance=1.0, psychic_resistance=1.0,
                 poison_resistance=1.0,
                 ghost_resistance=1.0, fighting_resistance=1.0, steel_resistance=1.0, ground_resistance=1.0,
                 rock_resistance=1.0, ice_resistance=1.0, dark_resistance=1.0, bug_resistance=1.0,
                 dragon_resistance=1.0, fairy_resistance=1.0):
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
fire = Type(name='Fire', fire_resistance=0.5, grass_resistance=0.5, steel_resistance=0.5, bug_resistance=0.5,
            ice_resistance=0.5, fairy_resistance=0.5, water_resistance=2, ground_resistance=2, rock_resistance=2)
water = Type(name="Water", fire_resistance=0.5, water_resistance=0.5, ice_resistance=0.5, steel_resistance=0.5,
             grass_resistance=2, electric_resistance=2)
grass = Type(name='Grass', electric_resistance=0.5, grass_resistance=0.5, ground_resistance=0.5, water_resistance=0.5,
             bug_resistance=2, fire_resistance=2, flying_resistance=2, poison_resistance=2, ice_resistance=2)
electric = Type(name='Electric', electric_resistance=0.5, flying_resistance=0.5, steel_resistance=0.5,
                ground_resistance=2)
flying = Type(name='Flying', ground_resistance=0, grass_resistance=0.5, fighting_resistance=0.5, bug_resistance=0.5,
              electric_resistance=2, rock_resistance=2, ice_resistance=2)
psychic = Type(name='Psychic', psychic_resistance=0.5, fighting_resistance=0.5, ghost_resistance=2, dark_resistance=2,
               bug_resistance=2)
poison = Type(name='Poison', grass_resistance=0.5, poison_resistance=0.5, fighting_resistance=0.5, bug_resistance=0.5,
              fairy_resistance=0.5, psychic_resistance=2, ground_resistance=2)
ghost = Type(name='Ghost', normal_resistance=0, fighting_resistance=0, bug_resistance=0.5, poison_resistance=0.5,
             ghost_resistance=2, dark_resistance=2)
fighting = Type(name='Fighting', rock_resistance=0.5, dark_resistance=0.5, bug_resistance=0.5, flying_resistance=2,
                psychic_resistance=2, fairy_resistance=2)
steel = Type(name='Steel', poison_resistance=0, normal_resistance=0.5, grass_resistance=0.5, flying_resistance=0.5,
             fairy_resistance=0.5, steel_resistance=0.5, rock_resistance=0.5, ice_resistance=0.5, bug_resistance=0.5,
             dragon_resistance=0.5, psychic_resistance=0.5, fire_resistance=2, fighting_resistance=2,
             ground_resistance=2)
ground = Type(name='Ground', electric_resistance=0, poison_resistance=0.5, rock_resistance=0.5, water_resistance=2,
              grass_resistance=2, ice_resistance=2)
rock = Type(name='Rock', poison_resistance=0.5, normal_resistance=0.5, fire_resistance=0.5, flying_resistance=0.5,
            water_resistance=2, grass_resistance=2, fighting_resistance=2, steel_resistance=2, ground_resistance=2)
ice = Type(name='Ice', ice_resistance=0.5, fire_resistance=2, rock_resistance=2, fighting_resistance=2,
           steel_resistance=2)
dark = Type(name='Dark', psychic_resistance=0, dark_resistance=0.5, ghost_resistance=0.5, fighting_resistance=2,
            bug_resistance=2, fairy_resistance=2)
bug = Type(name='Bug', fighting_resistance=0.5, grass_resistance=0.5, ground_resistance=0.5, fire_resistance=2,
           flying_resistance=2, rock_resistance=2)
dragon = Type(name='Dragon', fire_resistance=0.5, water_resistance=0.5, grass_resistance=0.5, electric_resistance=0.5,
              ice_resistance=2, dragon_resistance=2, fairy_resistance=2)
fairy = Type(name='Fairy', dragon_resistance=0, fighting_resistance=0.5, dark_resistance=0.5, bug_resistance=0.5,
             poison_resistance=2, steel_resistance=2)

# POKEMON1'S TYPES
types1 = (water, ground)
# POKEMON2'S TYPES
types2 = (fire, flying)

# POKEMON1'S RESISTANCE
resistance1 = {
    'normal': types1[0].normal_resistance * types1[1].normal_resistance,
    'fire': types1[0].fire_resistance * types1[1].fire_resistance,
}

# POKEMON2'S RESISTANCE
resistance2 = {
    'normal': 0,
}

# POKEMON1'S ATTACKS
attacks1 = [
    Move(power=40, accuracy=100, type='Fairy', category='Special', contact=False),
    Move(power=0, accuracy=100, type='Normal', category='Status', contact=False),
    Move(power=75, accuracy=100, type='Grass', category='Special', contact=False),
    Move(power=70, accuracy=100, type='Bug', category='Physical', contact=True)
]
# POKEMON2'S ATTACKS
attacks2 = [
    Move(power=80, accuracy=100, type='Bug', category='Physical', contact=True),
    Move(power=0, accuracy=100, type='Normal', category='Status', contact=False),
    Move(power=10, accuracy=100, type='Normal', category='Special', contact=False),
    Move(power=70, accuracy=100, type='Normal', category='Physical', contact=True, critical_chance=2)
]


def fight(pokemon1, pokemon2):
    try:
        for x in range(12):
            for round in range(4):

                if pokemon1.attacks[round].priority == pokemon2.attacks[round].priority:
                    if pokemon1.stats['spd'] >= pokemon2.stats['spd']:
                        # ATAK POKA 1
                        attack(attacker=pokemon1, defender=pokemon2, runda=round)
                        # ATAK POKA 2
                        attack(attacker=pokemon2, defender=pokemon1, runda=round)
                    else:
                        # ATAK POKA 2
                        attack(attacker=pokemon2, defender=pokemon1, runda=round)
                        # ATAK POKA 1
                        attack(attacker=pokemon1, defender=pokemon2, runda=round)

                elif pokemon1.attacks[round].priority > pokemon2.attacks[round].priority:
                    # ATAK POKA 1
                    attack(attacker=pokemon1, defender=pokemon2, runda=round)
                    # ATAK POKA 2
                    attack(attacker=pokemon2, defender=pokemon1, runda=round)

                elif pokemon1.attacks[round].priority < pokemon2.attacks[round].priority:
                    # ATAK POKA 2
                    attack(attacker=pokemon2, defender=pokemon1, runda=round)
                    # ATAK POKA 1
                    attack(attacker=pokemon1, defender=pokemon2, runda=round)
    except ValueError:
        pass


def attack(attacker, defender, runda):
    print(f"HP of defender: {defender.stats['hp']} ({defender.name})")
    print(f"HP of attacker: {attacker.stats['hp']} ({attacker.name})")
    # todo: chance of using attack based on accuracy

    if attacker.attacks[runda].category == 'Status':
        print("Move's effect")
    else:
        physical_factor = round(0.27 * (attacker.stats['att'] + 25) / (defender.stats['def'] + 25), 4)
        special_factor = round(0.27 * (attacker.stats['spatt'] + 25) / (defender.stats['spdef'] + 25), 4)
        power_factor = attacker.attacks[runda].power

        if attacker.attacks[runda].type in attacker.types:
            power_factor = power_factor * 1.30
        if attacker.attacks[runda].category == 'Physical':
            stats_factor = physical_factor
        else:
            stats_factor = special_factor

        # power_factor multiplied by items
        # effectiveness
        # weather

        friend_guard_factor = 1
        friend_guard_factor = friend_guard(defender, friend_guard_factor)

        damage = int(power_factor * stats_factor * attacker.lvl_factor * friend_guard_factor)
        # power_factor * stats_factor * attacker.lvl_factor * effectiveness_factor * weather_factor * friend_guard_factor

        damage = randomised_damage(damage)

        damage = critical_strike(attacker, damage, runda)

        defender.stats['hp'] = int(defender.stats['hp']) - int(damage)

        print(f"{attacker.name} attacks as first dealing {int(damage)}")
    print(f"{defender.name} ends up with {defender.stats['hp']} HP \n")

    verifying_winner(attacker, defender)


def friend_guard(defender, friend_guard_factor):
    if defender.ability == 'Friend Guard':
        friend_guard_factor = 0.85
        return friend_guard_factor
    else:
        return friend_guard_factor


def randomised_damage(damage):
    minimally = int(damage * 0.9)
    maximally = int(damage * 1.1)
    damage = randrange(minimally, maximally)
    return damage


def critical_strike(attacker, damage, runda):
    if attacker.attacks[runda].critical_chance == 1:
        if randrange(1000) <= 63:
            return damage * 1.5
        else:
            return damage

    elif attacker.attacks[runda].critical_chance == 2:
        if randrange(1000) <= 125:
            return damage * 1.5
        else:
            return damage

    elif attacker.attacks[runda].critical_chance == 3:
        if randrange(100) <= 50:
            return damage * 1.5
        else:
            return damage

    else:
        return damage * 1.5


def verifying_winner(attacker, defender):
    if defender.stats['hp'] <= 0:
        print(f"{attacker.name} won")
        raise ValueError

    elif attacker.stats['hp'] <= 0:
        print(f"{defender.name} won")
        raise ValueError


tic = time.perf_counter()
for i in range(1):
    # POKEMON1'S STATS
    stats1 = {
        'att': 528,
        'def': 475,
        'spatt': 357,
        'spdef': 692,
        'spd': 526,
        'hp': 1600,
        'pokemon_accuracy': 100,
        'pokemon_dodge': 100,
    }
    # POKEMON2'S STATS
    stats2 = {
        'att': 311,
        'def': 261,
        'spatt': 193,
        'spdef': 131,
        'spd': 588,
        'hp': 1290,
        'pokemon_accuracy': 100,
        'pokemon_dodge': 100,
    }
    pokemon1 = Pokemon(types=types1, lvl=75, stats=stats1, attacks=attacks1, name=f'Skiploom_{i}', ability='Leaf Guard')
    pokemon2 = Pokemon(types=types2, lvl=66, stats=stats2, attacks=attacks2, name=f'Ninjask_{i}', ability='Speed Boost')

    fight(pokemon1=pokemon1, pokemon2=pokemon2)

toc = time.perf_counter()
print(f'Duration of fight: {toc - tic:0.4f}')
