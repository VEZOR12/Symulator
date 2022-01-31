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
    def __init__(self, types: tuple, lvl: int, stats: dict, attacks: list, resistance: dict, name=None, ability=None):
        self.name = name
        self.types = types
        self.lvl = lvl
        self.stats = stats
        self.attacks = attacks
        self.lvl_factor = round(0.9 + 0.1 * self.lvl + 0.0004 * self.lvl * self.lvl, 4)
        self.ability = ability


# TYPES
types1 = ('Ground', 'Water')
types2 = ('Fire', 'Flying')

# POKEMON1'S ATTACKS
attacks1 = [
    Move(power=50, accuracy=100, type='Fighting', category='Physical', contact=True),
    Move(power=50, accuracy=100, type='Rock', category='Physical', contact=False),
    Move(power=50, accuracy=100, type='Ground', category='Physical', contact=False),
    Move(power=50, accuracy=100, type='Water', category='Physical', contact=True)
]
# POKEMON2'S ATTACKS
attacks2 = [
    Move(power=50, accuracy=100, type='Fire', category='Special', contact=False),
    Move(power=50, accuracy=100, type='Normal', category='Special', contact=True),
    Move(power=50, accuracy=100, type='Flying', category='Special', contact=False),
    Move(power=50, accuracy=100, type='Water', category='Special', contact=True)
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
        'att': 4380,
        'def': 1991,
        'spatt': 946,
        'spdef': 1991,
        'spd': 2000,
        'hp': 9000,
        'pokemon_accuracy': 100,
        'pokemon_dodge': 100,
    }
    # POKEMON2'S STATS
    stats2 = {
        'att': 946,
        'def': 1991,
        'spatt': 4380,
        'spdef': 1991,
        'spd': 1917,
        'hp': 9000,
        'pokemon_accuracy': 100,
        'pokemon_dodge': 100,
    }
    pokemon1 = Pokemon(types=types1, lvl=100, stats=stats1, attacks=attacks1, name=f'Swampert_{i}',
                       ability='Friend Guard')
    pokemon2 = Pokemon(types=types2, lvl=98, stats=stats2, attacks=attacks2, name=f'Charizard_{i}',
                       ability='Flash Fire')

    fight(pokemon1=pokemon1, pokemon2=pokemon2)

toc = time.perf_counter()
print(f'Duration of fight: {toc - tic:0.4f}')
