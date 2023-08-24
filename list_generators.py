# Popular Type and Pokemon lists

from pokemon_class import *
from type_class import *

def types_generator():
    Bug = Type("Bug", [], [], [])
    Dark = Type("Dark", [], [], [])
    Dragon = Type("Dragon", [], [], [])
    Electric = Type("Electric", [], [], [])
    Fairy = Type("Fairy", [], [], [])
    Fighting = Type("Fighting", [], [], [])
    Fire = Type("Fire", [], [], [])
    Flying = Type("Flying", [], [], [])
    Ghost = Type("Ghost", [], [], [])
    Grass = Type("Grass", [], [], [])
    Ground = Type("Ground", [], [], [])
    Ice = Type("Ice", [], [], [])
    Normal = Type("Normal", [], [], [])
    Poison = Type("Poison", [], [], [])
    Psychic = Type("Psychic", [], [], [])
    Rock = Type("Rock", [], [], [])
    Steel = Type("Steel", [], [], [])
    Water = Type("Water", [], [], [])

    Bug.se_list.extend([Dark, Grass, Psychic])
    Bug.nve_list.extend([Fairy, Fighting, Fire, Flying, Ghost, Poison, Steel])

    Dark.se_list.extend([Ghost, Psychic])
    Dark.nve_list.extend([Dark, Fairy, Fighting])

    Dragon.se_list.extend([Dragon])
    Dragon.nve_list.extend([Steel])
    Dragon.ne_list.extend([Fairy])

    Electric.se_list.extend([Flying, Water])
    Electric.nve_list.extend([Dragon, Electric, Grass])
    Electric.ne_list.extend([Ground])

    Fairy.se_list.extend([Dark, Dragon, Fighting])
    Fairy.nve_list.extend([Fire, Poison, Steel])

    Fighting.se_list.extend([Dark, Ice, Normal, Rock, Steel])
    Fighting.nve_list.extend([Bug, Fairy, Flying, Poison, Psychic])
    Fighting.ne_list.extend([Ghost])

    Fire.se_list.extend([Grass, Steel, Bug, Ice])
    Fire.nve_list.extend([Fire, Water, Rock, Dragon])

    Flying.se_list.extend([Bug, Fighting, Grass])
    Flying.nve_list.extend([Electric, Rock, Steel])

    Ghost.se_list.extend([Ghost, Psychic])
    Ghost.nve_list.extend([Dark])
    Ghost.ne_list.extend([Normal])

    Grass.se_list.extend([Water, Rock, Ground])
    Grass.nve_list.extend([Fire, Grass, Steel, Bug, Dragon, Flying, Poison, Steel])

    Ground.se_list.extend([Electric, Fire, Poison, Rock, Steel])
    Ground.nve_list.extend([Bug, Grass])
    Ground.ne_list.extend([Flying])

    Ice.se_list.extend([Dragon, Flying, Grass, Ground])
    Ice.nve_list.extend([Ice, Water, Fire, Steel])

    Normal.nve_list.extend([Steel, Rock])
    Normal.ne_list.extend([Ghost])

    Psychic.se_list.extend([Fighting, Poison])
    Psychic.nve_list.extend([Psychic, Steel])
    Psychic.ne_list.extend([Dark])

    Poison.se_list.extend([Fairy, Grass])
    Poison.nve_list.extend([Poison, Ground, Rock, Ghost])
    Poison.ne_list.extend([Steel])

    Rock.se_list.extend([Bug, Fire, Flying, Ice])
    Rock.nve_list.extend([Fighting, Ground, Steel])

    Steel.se_list.extend([Ice, Rock, Fairy])
    Steel.nve_list.extend([Steel, Water, Fire, Electric])

    Water.se_list.extend([Fire, Rock, Ground])
    Water.nve_list.extend([Grass, Water, Dragon])

    # includes Fire/Water/Grass
    # return [Bug, Dark, Dragon, Electric, Fairy, Fighting, Fire, Flying,
    # Ghost, Grass, Ground, Ice, Normal, Psychic, Poison, Rock, Steel, Water]

    return [Bug, Dark, Dragon, Electric, Fairy, Fighting, Flying,
    Ghost, Ground, Ice, Normal, Psychic, Poison, Rock, Steel]

    # return [Bug, Ice, Normal, Fire, Water, Grass, Ghost]
all_types = types_generator()

def pokemon_generator():
    monotype_pokemon_list = [Pokemon(x) for x in all_types] # 16 pokemon
    dualtype_pokemon_list = [Pokemon(x, y) for x in all_types for y in all_types[all_types.index(x)+1:]] #120 pokemon
    all_pokemon_list = monotype_pokemon_list + dualtype_pokemon_list # 136 pokemon
    return all_pokemon_list
pokemon_list = pokemon_generator()

def monotype_pokemon_generator():
    return [Pokemon(x) for x in all_types] # 16 pokemon
monotype_pokemon_list = monotype_pokemon_generator()

