from list_generators import *
from trio_class import *
from pokemon_class import *

if mono_type == True:
    pokemon_list = monotype_pokemon_list

# return [Array<Array<Pokemon>>] Array with arrays of pokemon typings that possess that many immunities
def fill_immunity_lists():
    for def_pokemon in pokemon_list:
        counter = 0
        for typ in all_types:
            if typ.attack(def_pokemon) == 0:
                counter += 1
        if counter == 0:
            no_immunity_list.append(def_pokemon)
        elif counter == 1:
            one_immunity_list.append(def_pokemon)
        elif counter == 2:
            two_immunity_list.append(def_pokemon)
        else:
            three_immunity_list.append(def_pokemon)

    multiple_immunity_list = two_immunity_list+three_immunity_list
    return [no_immunity_list, one_immunity_list, multiple_immunity_list]
no_immunity_list = [] # 36
one_immunity_list = [] # 54
two_immunity_list = [] # 25
three_immunity_list = [] # 6
multiple_immunity_list = [] # 25+6=31
immunity_lists = fill_immunity_lists()

# return [Array<Array<Trio>>] Array of arrays of trios of pokemon that obey the given trio relationship.
def fill_trio_relationships():
    for pokemon1 in pokemon_list:
        for pokemon2 in pokemon_list[pokemon_list.index(pokemon1)+1:]:
            for pokemon3 in pokemon_list[pokemon_list.index(pokemon2)+1:]:
                trio = Trio(pokemon1, pokemon2, pokemon3)
                
                if not trio.share_type():
                    
                    if trio.super_effective() == 0:
                        se_se.append(trio)
                    
                    if trio.not_very_effective() == 0:
                        nve_nve.append(trio)
                    
                    if trio.neutral_effective() == 0:
                        neu_neu.append(trio)

                    if trio.super_effective() == 1:
                        if trio.neutral_effective() == 2:
                            se_neu.append(trio)
                        if trio.not_very_effective() == 2:
                            se_nve.append(trio)

                    if trio.super_effective() == 2:
                        if trio.neutral_effective() == 1:
                            se_neu.append(trio)
                        if trio.not_very_effective() == 1:
                            se_nve.append(trio)

                    if trio.not_very_effective() == 1:
                        if trio.neutral_effective() == 2:
                            nve_neu.append(trio)
                    
                    if trio.not_very_effective() == 2:
                        if trio.neutral_effective() == 1:
                            nve_neu.append(trio)
    return [se_se, nve_nve, neu_neu, se_nve, se_neu, nve_neu]
se_se = []    
nve_nve = []   
neu_neu = []    
se_nve = []      
se_neu = []      
nve_neu = []    
trio_relationships = fill_trio_relationships()
'''
As well as having a set relationship with their attacking and defending pokemon, each pokemon
in the trio also had the same self-relation: they all resisted their own typing. Though the 
pokemon we look at don't have to self-resist, they should all share the same self-relation. 
'''
# return [Array<Array<Trio>>] Array of arrays of pokemon that obey the given self-relationship.
def fill_self_relation():
    for pokemon in pokemon_list:
        self_attack = pokemon.attack(pokemon)
        if 0.5 in self_attack or 0.25 in self_attack: 
            self_nve.append(pokemon)
        if 2 in self_attack or 4 in self_attack:
            self_se.append(pokemon)
        if self_attack == [1] or self_attack == [1,1]:
            self_neu.append(pokemon)
        if 0 in self_attack:
            self_imm.append(pokemon)

    return [self_se, self_nve, self_neu, self_imm]
self_se = []   # Can deal SE to self; 44 pokemon
self_nve = []  # Resists at least one of own types; 80 pokemon
self_neu = []  # Only deals neutral to self; 
self_imm = []  # Immune to one of own types; 7 pokemon
self_relationships_lists = fill_self_relation()