# This program is designed to finds new options for starter pokemon types. Excludes water,fire,grass from options.
# Pokemon are categorized based on their number of immunities and their self relation.
# Trios of pokemon that obey two sets of triangular relationships are put into a specific list
# Pokemon are then displayed based on trio relationship -> number of immunities -> self relation

from termcolor import cprint  # colorize text


class Pokemon:
    # Pokemon are hypothetical combinations of types or individual types

    def __init__(self, *typing):
        # Pokemon have one or two types
        self.typing = typing

    def __repr__(self):
        # Pokemon are represented by their typing
        return "/".join(str(typ) for typ in self.typing)

    # Pokemon may attack other pokemon. Attack considers all types of the attacker and defender
    # and gives a list of damage multipliers from each attacking type against both defending types
    def attack(self, pokemon):
        # Pokemon may attack other pokemon. Attack considers all types of the attacker and defender
        # and gives a list of damage multipliers from each attacking type against both defending types
        offense_set = []
        for attack_type in self.typing:	 # one attacking type considered at a time
            offense_set.append(attack_type.attack(pokemon))
        return offense_set


class Type:
    # Types are the different pokemon elemental types.

    def __init__(self, name, se_list, nve_list, noeffect_list):
        # Types have a name, list of types they are super effective, not very effective, or
        # have no effect against
        self.name = name
        self.se_list = se_list
        self.nve_list = nve_list
        self.noeffect_list = noeffect_list

    def __repr__(self):
        # Types are represented by their name
        return str(self.name)

    def attack(self, pokemon):
        # All attacks are a single type; type-effectiveness of an attakc is
        # the product of its effectiveness against both defending types
        damage_multiplier = 1
        for defend_type in pokemon.typing:
            if defend_type in self.se_list:  # If attack is SE, multiply by 2
                damage_multiplier *= 2
            elif defend_type in self.nve_list:  # If attack is NVE, divide by 2
                damage_multiplier /= 2
            elif defend_type in self.noeffect_list:  # If defender is immune, change to zero
                damage_multiplier *= 0
        return damage_multiplier


# All types in alphetical order. Lists are empty and filled later because they reference each other
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


# Each type's lists are filled with relevent data
Bug.se_list.extend([Dark, Grass, Psychic])
Bug.nve_list.extend([Fairy, Fighting, Fire, Flying, Ghost, Poison, Steel])

Dark.se_list.extend([Ghost, Psychic])
Dark.nve_list.extend([Dark, Fairy, Fighting])

Dragon.se_list.extend([Dragon])
Dragon.nve_list.extend([Steel])
Dragon.noeffect_list.extend([Fairy])

Electric.se_list.extend([Flying, Water])
Electric.nve_list.extend([Dragon, Electric, Grass])
Electric.noeffect_list.extend([Ground])

Fairy.se_list.extend([Dark, Dragon, Fighting])
Fairy.nve_list.extend([Fire, Poison, Steel])

Fighting.se_list.extend([Dark, Ice, Normal, Rock, Steel])
Fighting.nve_list.extend([Bug, Fairy, Flying, Poison, Psychic])
Fighting.noeffect_list.extend([Ghost])

Fire.se_list.extend([Grass, Steel, Bug, Ice])
Fire.nve_list.extend([Fire, Water, Rock, Dragon])

Flying.se_list.extend([Bug, Fighting, Grass])
Flying.nve_list.extend([Electric, Rock, Steel])

Ghost.se_list.extend([Ghost, Psychic])
Ghost.nve_list.extend([Dark])
Ghost.noeffect_list.extend([Normal])

Grass.se_list.extend([Water, Rock, Ground])
Grass.nve_list.extend([Fire, Grass, Steel, Bug, Dragon, Flying, Poison, Steel])

Ground.se_list.extend([Electric, Fire, Poison, Rock, Steel])
Ground.nve_list.extend([Bug, Grass])
Ground.noeffect_list.extend([Flying])

Ice.se_list.extend([Dragon, Flying, Grass, Ground])
Ice.nve_list.extend([Ice, Water, Fire, Steel])

Normal.nve_list.extend([Steel, Rock])
Normal.noeffect_list.extend([Ghost])

Psychic.se_list.extend([Fighting, Poison])
Psychic.nve_list.extend([Psychic, Steel])
Psychic.noeffect_list.extend([Dark])

Poison.se_list.extend([Fairy, Grass])
Poison.nve_list.extend([Poison, Ground, Rock, Ghost])
Poison.noeffect_list.extend([Steel])

Rock.se_list.extend([Bug, Fire, Flying, Ice])
Rock.nve_list.extend([Fighting, Ground, Steel])

Steel.se_list.extend([Ice, Rock, Fairy])
Steel.nve_list.extend([Steel, Water, Fire, Electric])

Water.se_list.extend([Fire, Rock, Ground])
Water.nve_list.extend([Grass, Water, Dragon])


# List containing all non-traditional starter types 
# type_list_trad = [Water, Fire, Grass]  # add these types to consider all 18 types
type_list = [
    Bug, Dark, Dragon, Electric, Fairy, Fighting, Flying,
    Ghost, Ground, Ice, Normal, Psychic, Poison, Rock, Steel
]


# List containing all possible pokemon type combinations (not permutations). Total of 120 pokemon
pokemon_list = [Pokemon(x) for x in type_list]  # 15 pokemon
pokemon_list.extend([Pokemon(x, y) for x in type_list for y in type_list[type_list.index(
    x)+1:] if x != y])  # 105 pokemon; remove this line to only consider mono type pokemon

# # Dictionary containing all pokemon matchups
# # For example:  {Pokemon1: {Type1: Damage, Type2: Damage, ...}, Pokemon2: {Type1: Damage, Type2: Damage, ...}}
# effectiveness_dict = {}
# for defender in pokemon_list:
# 	pokemon_damages = {}  # Dictionary for effectivnesses against a single pokemon
# 	for attacker in pokemon_list:
# 		pokemon_damages[attacker] = attacker.attack(defender)  # Pair attacking type with its effectiveness
# 	effectiveness_dict[defender] = pokemon_damages  # Pair defending type with dictionary of attacking effectiveness

# Lists of pokemon with given number of immunities
no_immunity_list = []  # 36 pokemon
one_immunity_list = []  # 54 pokemon
two_immunity_list = []  # 24 pokemon
three_immunity_list = []  # 6 pokemon

# Fills immunity lists
for pokemon in pokemon_list:
    counter_immunity = 0
    for attacker in type_list:
        damage = attacker.attack(pokemon)
        if damage == 0:
            counter_immunity += 1
    if counter_immunity == 0:
        no_immunity_list.append(pokemon)
    elif counter_immunity == 1:
        one_immunity_list.append(pokemon)
    elif counter_immunity == 2:
        two_immunity_list.append(pokemon)
    else:
        three_immunity_list.append(pokemon)

multiple_immunity_list = two_immunity_list+three_immunity_list
immunity_lists = [no_immunity_list, one_immunity_list, multiple_immunity_list]


# Lists of pokemon trios with given effectiveness relationships.
all_se = []  # 42 options
all_nve = []  # 0 options
all_neu = []  # 725 options
se_nve = []  # 74 options
se_neu = []  # 126 options
nve_neu = []  # 5 options
# doesn't include all_nve since it is empty
effectiveness_lists = [all_se, all_neu, se_nve, se_neu, nve_neu]

# Fills effectiveness relationship lists
for pokemon1 in pokemon_list:
    for pokemon2 in pokemon_list[pokemon_list.index(pokemon1)+1:]:
        for pokemon3 in pokemon_list[pokemon_list.index(pokemon2)+1:]:

            # ensure no type is in 2 pokemon
            set1 = set(list(pokemon1.typing))
            set2 = set(list(pokemon2.typing))
            set3 = set(list(pokemon3.typing))
            if not (set1 & set2) and not (set1 & set3) and not (set2 & set3):

                p1p2 = pokemon1.attack(pokemon2)
                p1p3 = pokemon1.attack(pokemon3)
                p2p1 = pokemon2.attack(pokemon1)
                p2p3 = pokemon2.attack(pokemon3)
                p3p1 = pokemon3.attack(pokemon1)
                p3p2 = pokemon3.attack(pokemon2)
                all_attacks = [p1p2, p1p3, p2p1, p2p3, p3p1, p3p2]
                cycle1 = [p1p2, p2p3, p3p1]
                cycle2 = [p1p3, p3p2, p2p1]
                if all(map(lambda x: any(y > 1 for y in x), all_attacks)):  # All can deal SE to other 2
                    all_se.append([pokemon1, pokemon2, pokemon3])

                # All only deal NVE or 0 to other 2
                if all(map(lambda x: all(y < 1 for y in x), all_attacks)):
                    all_nve.append([pokemon1, pokemon2, pokemon3])

                # All only deal neutral to other 2
                if all(map(lambda x: all(y == 1 for y in x), all_attacks)):
                    all_neu.append([pokemon1, pokemon2, pokemon3])

                # Check if trio deals SE one way
                if any((all(map(lambda x: 2 in x or 4 in x, cycle1)), all(map(lambda x: 2 in x or 4 in x, cycle2)))):
                    # Check if trio deals neutral the other way
                    if any((all(map(lambda x: [1, 1] == x or [1] == x, cycle1)), all(map(lambda x: [1, 1] == x or [1] == x, cycle2)))):
                        se_neu.append([pokemon1, pokemon2, pokemon3])
                    # Check if trio deals nve or 0 the other way
                    if any((all(map(lambda x: all(y < 1 for y in x), cycle1)), all(map(lambda x: all(y < 1 for y in x), cycle2)))):
                        se_nve.append([pokemon1, pokemon2, pokemon3])

                # Check if trio deals nve or 0 one way
                if any((all(map(lambda x: all(y < 1 for y in x), cycle1)), all(map(lambda x: all(y < 1 for y in x), cycle2)))):
                    # Check if trio deals neutral the other way
                    if any((all(map(lambda x: [1, 1] == x or [1] == x, cycle1)), all(map(lambda x: [1, 1] == x or [1] == x, cycle2)))):
                        nve_neu.append([pokemon1, pokemon2, pokemon3])


# Lists of pokemon with the given self-relationship. Some pokemon fall into multiple categories
self_se = []  # Can deal SE to self; 44 pokemon
self_nve = []  # Resists at least one of own types; 80 pokemon
self_neu = []  # Only deals neutral to self; 18 pokemon
self_imm = []  # Immune to one of own types; 7 pokemon
self_relationships_lists = [self_se, self_nve, self_neu, self_imm]

# Fill self-relationship lists
for pokemon in pokemon_list:
    self_attack = pokemon.attack(pokemon)
    if 0.5 in self_attack or 0.25 in self_attack:  # Pokemon may doubly resist attack
        self_nve.append(pokemon)
    if 2 in self_attack or 4 in self_attack:  # Pokemon may be doubly weak to attack
        self_se.append(pokemon)
    if self_attack == [1, 1] or self_attack == [1]:
        self_neu.append(pokemon)
    if 0 in self_attack:
        self_imm.append(pokemon)


# Displays information on which relationship we are looking at
# (nve-nve with 0 options is not displayed here)
# Layers: Trio relationship > Number of immunities > Self-relationship
for trio_list in effectiveness_lists:
    if trio_list is all_se:
        cprint("Super Effective - Super Effective", "blue", None, [])
    elif trio_list is all_neu:
        cprint("Neutral - Neutral", "blue",  None, [])
    elif trio_list is se_neu:
        cprint("Super Effective - Neutral", "blue",  None, [])
    elif trio_list is se_nve:
        cprint("Super Effective - Not Very Effective", "blue",  None, [])
    elif trio_list is nve_neu:
        cprint("Not Very Effective - Neutral", "blue",  None, [])

    # will contain TRIOS (not individual pokemon) of given trio effectiveness with mixed number of immunities
    mixed_immunity = []

    # identify which immunity list we're looking at
    for imm in immunity_lists:

        # printed variable ensures layer is displayed only once for all relevent trios
        printed = False

        # will contain TRIOS (not individual pokemon) of given immunity value with no uniform self relation
        no_self_relation = []

        # identify which self relation list we're looking at
        for self_relation in self_relationships_lists+[no_self_relation]:

            # All pokemon in given trio from trio_list moved to:
            #   current list if it obeys immunity and self relations
            #   placed in no_self_relation if it obeys immunity but aren't all in same self_relation, including non-current ones
            #   placed in mixed_immunity if it doesn't obey immunity
            if self_relation is not no_self_relation:
                # contains trios of pokemon with current trio relationship, immunitiy, self relation
                current_list = []

                for trio in trio_list:
                    if all(pokemon in imm for pokemon in trio):  # obeys immunity requirement
                        # obeys self relation requirement
                        if all(pokemon in self_relation for pokemon in trio):
                            current_list.append(trio)
                        elif not any(all(pokemon in self_relationships_lists[i] for pokemon in trio) for i in range(4)):
                            # obeys immunity, but not any self-relation
                            if trio not in no_self_relation:
                                no_self_relation.append(trio)
                    elif not any(all(pokemon in immunity_lists[i] for pokemon in trio) for i in range(len(immunity_lists))):
                        # does not obey immunity requirement
                        if trio not in mixed_immunity:
                            mixed_immunity.append(trio)
            else:
                current_list = no_self_relation  # OPTIONAL 1/2: NO SELF-RELATION: PT 1/2

            # Display relationships which satisfy requirements by checking if the current_list is non-empty
            # "printed" variable ensures layer is displayed only once for all relevent trios
            color = "green"
            if current_list:
                if imm is no_immunity_list and not printed:
                    cprint("   No Immunities", "magenta",
                           None, [])
                    printed = True
                elif imm is one_immunity_list and not printed:
                    cprint("   One Immunity", "magenta",
                           None, [])
                    printed = True
                elif imm is multiple_immunity_list and not printed:
                    cprint("   Multiple Immunities", "magenta",
                           None, [])
                    printed = True

                # print self relation name and trios obeying all 3 requirements
                if self_relation is self_se:
                    cprint("      Self Super Effective:", "red",
                           None, ["underline"])
                if self_relation is self_nve:
                    cprint("      Self Not Very Effective:", "red",
                           None, ["underline"])
                if self_relation is self_neu:
                    cprint("      Self Neutral:", "red",
                           None, ["underline"])
                if self_relation is self_imm:
                    cprint("      Self Immune:", "red",
                           None, ["underline"])
                if self_relation is no_self_relation:  # OPTIONAL 1/2: NO SELF RELATION: PT 2/2
                    color = "cyan"
                    cprint("      No Self Relation", "red",
                           None, ["underline"])

                # check number of immunities given for each pokemon in trio
                for trio in current_list:
                    text_options = []
                    highlight = None
                    p1immune = sum(len(trio[0].typing[y].noeffect_list)
                                   for y in range(len(trio[0].typing)))
                    p2immune = sum(len(trio[1].typing[y].noeffect_list)
                                   for y in range(len(trio[1].typing)))
                    p3immune = sum(len(trio[2].typing[y].noeffect_list)
                                   for y in range(len(trio[2].typing)))

                    # if all 3 pokemon have the same number of types that are immune to them, bold the text
                    if (p1immune == p2immune and p2immune == p3immune):
                        text_options.append("bold")

                    # # otherwise if they all have similar number of types immune to them (within one of each other), underline the text
                    # elif (p1immune > 0 and p2immune > 0 and p3immune > 0) or (p1immune < 2 and p2immune < 2 and p3immune < 2):
                    # 	text_options.append("underline")

                    # if any pokemon is immune to another pokemon within the trio, darken (soften) the text
                    # but if each pokemon is immune to another pokemon in trio, blacklight the text instead
                    imm_in_trio1 = [0 in trio[x].attack(
                        trio[(x+1) % 3]) for x in range(3)]
                    imm_in_trio2 = [
                        0 in trio[(x+1) % 3].attack(trio[(x)]) for x in range(3)]
                    if all(imm_in_trio1) or all(imm_in_trio2):
                        highlight = "on_grey"
                    elif any(imm_in_trio1) or any(imm_in_trio2):
                        text_options.append("dark")

                    # display the trio
                    cprint(f"{current_list.index(trio) +1}: {str(trio)[1:-1]}",
                           color, highlight, text_options)

    # OPTIONAL 2/2: MIXED IMMUNITY
    # after running through all same-value immunity trios, deal with trios that didn't share the exact same number of immunities
    # We only look at trios placed in the mixed_immunity list

    # printed variable ensures layer is displayed only once for all relevent trios
    printed = False

    # contains TRIOS (not individual pokemon) of given immunity (mixed) that don't share the same self-relation
    no_self_relation = []

    # identify what the each pokemon in the trio relationship to itself is
    for self_relation in self_relationships_lists+[no_self_relation]:

        # All pokemon in given trio eff moved to:
        #   current list if it obeys self relations
        #   placed in no_self_relation if it obeys immunity but aren't all in same self_relation, including non-current ones
        if self_relation is not no_self_relation:
            # contains trios of pokemon with current trio relationship, immunitiy, self relation
            current_list = []

            for trio in mixed_immunity:
                # obeys self relation requirement
                if all(pokemon in self_relation for pokemon in trio):
                    current_list.append(trio)
                elif not any(all(pokemon in self_relationships_lists[i] for pokemon in trio) for i in range(4)):
                    # does not obey self relation requirements
                    if trio not in no_self_relation:
                        no_self_relation.append(trio)
        else:
            current_list = self_relation  # OPTIONAL 2A: NO SELF RELATION: PT 1/2

        # Display which immunity type we're looking at only if it has any pokemon in it
        if current_list:
            if not printed:
                cprint("   Mixed Immunities", "magenta",
                       None, [])
                printed = True

            # print self relation
            if self_relation is self_se:
                cprint("      Self Super Effective:",
                       "red", None, ["underline"])
            if self_relation is self_nve:
                cprint("      Self Not Very Effective:",
                       "red", None, ["underline"])
            if self_relation is self_neu:
                cprint("      Self Neutral:",
                       "red", None, ["underline"])
            if self_relation is self_imm:
                cprint("      Self Immune:",
                       "red", None, ["underline"])
            if self_relation is no_self_relation:  # OPTIONAL 2A: NO SELF RELATION: PT 2/2
                cprint("      No Self Relation",
                       "red", None, ["underline"])

            # check number of immunities each pokemon gives
            for trio in current_list:
                text_options = []
                highlight = None
                color = "cyan"
                p1immune = sum(len(trio[0].typing[y].noeffect_list)
                               for y in range(len(trio[0].typing)))
                p2immune = sum(len(trio[1].typing[y].noeffect_list)
                               for y in range(len(trio[1].typing)))
                p3immune = sum(len(trio[2].typing[y].noeffect_list)
                               for y in range(len(trio[2].typing)))

                # # if all 3 pokemon have the same number of types that are immune to them, bold the text
                # if (p1immune == p2immune and p2immune == p3immune):
                # 	text_options.append("bold")

                # # otherwise if they all have similar number of types immune to them (within one of each other), underline the text
                # elif (p1immune > 0 and p2immune > 0 and p3immune > 0) or (p1immune < 2 and p2immune < 2 and p3immune < 2):
                # 		text_options.append("underline")

                # if any pokemon is immune to another pokemon within the trio, darken (soften) the text
                # but if each pokemon is immune to another pokemon in trio, blacklight the text instead
                imm_in_triangle1 = [0 in trio[x].attack(
                    trio[(x+1) % 3]) for x in range(3)]
                imm_in_triangle2 = [
                    0 in trio[(x+1) % 3].attack(trio[(x)]) for x in range(3)]
                if all(imm_in_triangle1) or all(imm_in_triangle2):
                    highlight = "on_grey"
                elif any(imm_in_triangle1) or any(imm_in_triangle2):
                    text_options.append("dark")

                # # if all pokemon have a similar number of immunities (within one of each other), change text color
                # if all(pokemon in one_immunity_list or pokemon in multiple_immunity_list for pokemon in trio) or all(
                # 	pokemon in one_immunity_list or pokemon in no_immunity_list for pokemon in trio) :
                # 	if self_relation is not no_self_relation:
                # 		color = "yellow"

                # if each pokemon has/gives an equal number of immunities
                imm_difference = []
                for pokemon in trio:
                    counter_immunity = 0  # number of immunities possessed
                    for attacker in type_list:
                        damage = attacker.attack(pokemon)
                        if damage == 0:
                            counter_immunity += 1
                    # find the difference between immunities given/had for each pokemon.
                    imm_difference.append(sum(len(pokemon.typing[y].noeffect_list) for y in range(
                        len(pokemon.typing))) - (counter_immunity))

                # if each pokemon has same value for immunity difference, turn text yellow (semi-obeys immunity requirement)
                if len(set(imm_difference)) == 1:
                    text_options.append("bold")
                    if self_relation is not no_self_relation:
                        color = "yellow"

                # display trio
                cprint(f"{current_list.index(trio) +1}: {str(trio)[1:-1]}",
                       color, highlight, text_options)