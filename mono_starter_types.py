'''
Only examines mono-type options, but with looser requirements
'''

from termcolor import cprint 

class Pokemon:

    # param: [Type] Can be a single Type
    def __init__(self, typing):
        self.typing = typing

    def __repr__(self):
        return str(self.typing)

    # param: [Pokemon] Attacking Pokemon
    # return [Array<Int>] Effectivenesses of attacker's type on defender. 
    def attack(self, def_pokemon):
        return self.typing.attack(def_pokemon)

class Type:
    def __init__(self, name, se_list, nve_list, ne_list):
        self.name = name
        self.se_list = se_list
        self.nve_list = nve_list
        self.ne_list = ne_list

    def __repr__(self):
        return str(self.name)

    # param: [Pokemon] Defending Pokemon
    # return [Int] Single effectiveness of attacker's type on defender.  
    def attack(self, def_pokemon):
        damage_multiplier = 1
        if def_pokemon.typing in self.ne_list: 
            return 0
        elif def_pokemon.typing in self.se_list: 
            damage_multiplier *= 2
        elif def_pokemon.typing in self.nve_list: 
            damage_multiplier /= 2
        return damage_multiplier

class Trio:
    def __init__(self, pokemon1, pokemon2, pokemon3):
        self.p1 = pokemon1
        self.p2 = pokemon2
        self.p3 = pokemon3

    def __repr__(self):
        return str([self.p1, self.p2, self.p3])


    def __iter__(self):
        self.value = 0
        return iter([self.p1, self.p2, self.p3])

    def __next__(self):
        if self.value < 3:
            value = self.value
            self.value += 1
            return __iter__[value]
        raise StopIteration
    
    # return: [Array<Array<Int>>]
    def trio_attack1(self):
        p1p2 = self.p1.attack(self.p2)
        p2p3 = self.p2.attack(self.p3)
        p3p1 = self.p3.attack(self.p1)
        return [p1p2, p2p3, p3p1]

    # return: [Array<Array<Int>>]
    def trio_attack2(self):
        p1p3 = self.p1.attack(self.p3)
        p2p1 = self.p2.attack(self.p1)
        p3p2 = self.p3.attack(self.p2)
        return [p1p3, p3p2, p2p1]

    # return: [Array<Array<Int>>]
    def trio_attack_full(self):
        return self.trio_attack1() + self.trio_attack2()

    # return [Int] Integer representing cycle in which the trio can deal SE damage
    #   0: both directions
    #   1: cycle 1
    #   2: cycle 2
    def super_effective(self):
        if all(map(lambda attack: attack > 1, self.trio_attack_full())):
            return 0
        elif all(map(lambda attack: attack > 1, self.trio_attack1())):
            return 1
        elif all(map(lambda attack: attack > 1, self.trio_attack2())):
            return 2


    '''
    Neutrality is a bit harder to quantify. How strictly do we enforce that the attacker
    deals NEU damage?
        Strict: Attackers are only capable of dealing NEU damage
        Semi-Strict: Attackers deal neutral damage, but may also deal NVE damage
        Non-strict: Attackers deal neutral damage, but may also deal SE or NVE damage. 
    '''
    # STRICT NEU:
    # param: [Array<Array<Int>>]
    # return [Int] Int representing cycle in which the trio can deal only NEU damage
    # def neutral_effective_strict(self):
    #     if all(map(lambda attack: all(eff == 1 for eff in attack), self.trio_attack_full())):
    #         return 0
    #     elif all(map(lambda attack: all(eff == 1 for eff in attack), self.trio_attack1())):
    #         return 1
    #     elif all(map(lambda attack: all(eff == 1 for eff in attack), self.trio_attack2())):
    #         return 2

    # SEMI_STRICT NEU:
    # param: [Array<Array<Int>>]
    # return [Int] Int representing cycle in which the trio can deal NEU damage and not SE damage
    def neutral_effective_semi_strict(self):
        if all(map(lambda attack: attack == 1, self.trio_attack_full())):
            return 0
        elif all(map(lambda attack:  attack == 1, self.trio_attack1())):
            return 1
        elif all(map(lambda attack:  attack == 1, self.trio_attack2())):
            return 2

    # NON_STRICT NEU:
    # param: [Array<Array<Int>>]
    # return [Int] Int representing cycle in which the trio can deal NEU damage
    # def neutral_effective(self):
    #     if all(map(lambda attack: any(eff == 1 for eff in attack), self.trio_attack_full())):
    #         return 0
    #     elif all(map(lambda attack: any(eff == 1 for eff in attack), self.trio_attack1())):
    #         return 1
    #     elif all(map(lambda attack: any(eff == 1 for eff in attack), self.trio_attack2())):
    #         return 2


    '''
    As with neutrality, how strict do we want to enforce the NVE-cycle? 
        Strict: Attackers are only capable of dealing NVE damage.
        Semi-Strict: Attackers can deal NVE, but may also deal NEU.
        Non-strict: Attackers can deal NVE, buy may also be able to deal SE or NEU damage.
    ''' 
    
    # STRICT NVE:
    # param: [Array<Array<Int>>]
    # return [Int] Int representing cycle in which the trio can deal only NEU damage
    def not_very_effective_strict(self):
        if all(map(lambda attack: attack < 1, self.trio_attack_full())):
            return 0
        elif all(map(lambda attack: attack < 1, self.trio_attack1())):
            return 1
        elif all(map(lambda attack: attack < 1, self.trio_attack2())):
            return 2
    
    # SEMI_STRICT NVE:
    # param: [Array<Array<Int>>]
    # return [Int] Int representing cycle in which the trio can deal NVE damage and not SE damage
    # def not_very_effective_semi_strict(self):
    #     if all(map(lambda attack: (any(eff < 1 for eff in attack) and not(any(eff > 1 for eff in attack))), self.trio_attack_full())):
    #         return 0
    #     elif all(map(lambda attack: (any(eff < 1 for eff in attack) and not(any(eff > 1 for eff in attack))), self.trio_attack1())):
    #         return 1
    #     elif all(map(lambda attack: (any(eff < 1 for eff in attack) and not(any(eff > 1 for eff in attack))), self.trio_attack2())):
    #         return 2

    # NON_STRICT NVE:
    # param: [Array<Array<Int>>]
    # return [Int] Int representing cycle in which the trio can deal NEU damage
    # def not_very_effective(self):
    #     if all(map(lambda attack: (any(eff < 1 for eff in attack)), self.trio_attack_full())):
    #         return 0
    #     elif all(map(lambda attack: (any(eff < 1 for eff in attack)), self.trio_attack1())):
    #         return 1
    #     elif all(map(lambda attack: (any(eff < 1 for eff in attack)), self.trio_attack2())):
    #         return 2

    
    # param: [Pokemon] Pokemon in trio
    # return [Integer] How many immunities this pokemon gives
    # A Normal/Fighting type would count as giving 2 immunities despite only one type (Ghost) being
    #   immune to that pokemon. Though we could adjust the logic to count it as one, both types giving
    #    an immunity still seems to warrant counting it twice, even if it's the same type immune to them.
    def imm_given(self, pokemon):
        return len(pokemon.typing.ne_list)

    # return [Array<Integer>] How many immunities each pokemon in the trio gives
    def imm_given_trio(self):
        give_imm = []
        for pokemon in self:
            give_imm.append(self.imm_given(pokemon))
        return give_imm
    
    '''
    Note: No starter pokemon has ever had a type which another type was immune to.
    Though Bulbsaur's poison typing means that it gives 1 immunity to steel,
    steel type was introduced in GenII, after Bulbasaur was a starter. 
    '''

    # return [Boolean] Do all pokemon in trio give same number of immunities?
    def same_imm_given(self):
        given = self.imm_given_trio()
        p1immune = given[0]
        p2immune = given[1]
        p3immune = given[2]
        if (p1immune == p2immune and p2immune == p3immune):
            return True 
        else:
            return False
    
    '''
    Almost every starter had 0 immunities and gave 0 immunities. It's unnecessary to 
    impose those limitations here. It's enough to check that the mathematical difference between 
    immunities given and had is the same among each pokemon in the trio. 
    (Rowlet is the only starter to have an immunity).
    '''

    # return [Boolean] Do the pokemon in the trio possess the same difference between their
    #   given and possessed immunities? 
    def give_has_balance(self):
        balance = []
        for pokemon in self:
            give = self.imm_given(pokemon)
            has = 0
            for typ in all_types:
                if typ.attack(pokemon) == 0:
                    has += 1
            balance.append(has - give)
        return (balance[0] == balance[1] and balance[1] == balance[2])
    
    # return [Boolean] Do all or none of the pokemon have an immunity to their attacker?
    def immune_balanced(self):
        imm_in_trio1 = [0 == attack for attack in self.trio_attack1()]
        imm_in_trio2 = [0 == attack for attack in self.trio_attack2()]
        if all(imm_in_trio1) or all(imm_in_trio2):
            return True
        elif any(imm_in_trio1) or any(imm_in_trio2):
            return False
        else:
            return True    

    # param [List] List to check adherence to
    # return [Boolean] Are all the pokemon within the trio in this list?
    def obey(self, obey_list):
        return all(pokemon in obey_list for pokemon in self)

    # param [List<List>] Lists of lists to check adherence to
    # return [Boolean] Do all the pokemon in the trio appear together in any of these lists?
    def obey_any(self, obey_lists):
        return any(self.obey(obey_list) for obey_list in obey_lists)

    def display(self, current_list, color = 'cyan', highlight = None, text_options = None):
        cprint(f"{current_list.index(self) +1}: {str(self)[1:-1]}",color)

def close(a, b):
    return abs(a-b) < 2

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

    # return [Fire, Water, Grass]

    # includes Fire/Water/Grass
    # return [Bug, Dark, Dragon, Electric, Fairy, Fighting, Fire, Flying,
    # Ghost, Grass, Ground, Ice, Normal, Psychic, Poison, Rock, Steel, Water]

    return [Bug, Dark, Dragon, Electric, Fairy, Fighting, Flying,
    Ghost, Ground, Ice, Normal, Psychic, Poison, Rock, Steel]
all_types = types_generator()

def pokemon_generator():
    return [Pokemon(x) for x in all_types] # 16 pokemon
pokemon_list = pokemon_generator()

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
            multiple_immunity_list.append(def_pokemon)

    return [no_immunity_list, one_immunity_list, multiple_immunity_list]
no_immunity_list = [] # 36
one_immunity_list = [] # 54
multiple_immunity_list = [] # 25
immunity_lists = fill_immunity_lists()

# return [Array<Array<Trio>>] Array of arrays of trios of pokemon that obey the given trio relationship.
def fill_trio_relationships():
    for pokemon1 in pokemon_list:
        for pokemon2 in pokemon_list[pokemon_list.index(pokemon1)+1:]:
            for pokemon3 in pokemon_list[pokemon_list.index(pokemon2)+1:]:
                trio = Trio(pokemon1, pokemon2, pokemon3)
                    
                if trio.super_effective() == 0:
                    se_se.append(trio)
                
                if trio.not_very_effective_strict() == 0:
                    nve_nve.append(trio)
                
                if trio.neutral_effective_semi_strict() == 0:
                    neu_neu.append(trio)

                if trio.super_effective() == 1:
                    if trio.neutral_effective_semi_strict() == 2:
                        se_neu.append(trio)
                    if trio.not_very_effective_strict() == 2:
                        se_nve.append(trio)

                if trio.super_effective() == 2:
                    if trio.neutral_effective_semi_strict() == 1:
                        se_neu.append(trio)
                    if trio.not_very_effective_strict() == 1:
                        se_nve.append(trio)

                if trio.not_very_effective_strict() == 1:
                    if trio.neutral_effective_semi_strict() == 2:
                        nve_neu.append(trio)
                
                if trio.not_very_effective_strict() == 2:
                    if trio.neutral_effective_semi_strict() == 1:
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
        if 0.5 == self_attack: 
            self_nve.append(pokemon)
        if 2 == self_attack:
            self_se.append(pokemon)
        if 1 == self_attack:
            self_neu.append(pokemon)

    return [self_se, self_nve, self_neu]
self_se = []   # Can deal SE to self;
self_nve = []  # Resists at least one of own types;
self_neu = []  # Only deals neutral to self; 
self_relationships_lists = fill_self_relation()

 
# Add trio to the respective list if it obeys the relationships. 
def append_trio(trio, imm_list, self_relation, self_relationships_lists, immunity_lists, current_list, no_self_relation, mixed_immunity):
    if trio.obey(imm_list) or (trio in mixed_immunity and imm_list == mixed_immunity):
        if trio.immune_balanced() and trio.give_has_balance():
            if trio.obey(self_relation):
                current_list.append(trio)
        
            elif not trio.obey_any(self_relationships_lists):
                if trio not in no_self_relation:
                    no_self_relation.append(trio)
    
    elif not trio.obey_any(immunity_lists):
        if trio not in mixed_immunity:
            mixed_immunity.append(trio)

# Display: Trio relationship > Number of immunities > Self-relationship > Trios
# We are not displaying trios with no shared self-relation. 
def display(trio_relationships):
    for trio_relation in trio_relationships:
        display_trio_relation(trio_relation)
        any_trios = False
        mixed_immunity = []

        for imm_list in immunity_lists + [mixed_immunity]:
            printed = False
            no_self_relation = []

            for self_relation in self_relationships_lists + [no_self_relation]:
                if self_relation is not no_self_relation:
                    current_list = []
                    
                    for trio in trio_relation:
                        append_trio(
                            trio, 
                            imm_list, 
                            self_relation, 
                            self_relationships_lists, 
                            immunity_lists, 
                            current_list, 
                            no_self_relation, 
                            mixed_immunity
                        ) 
                else:
                    current_list = no_self_relation  

                if current_list:
                    any_trios = True
                    if not printed:
                        display_immunity(imm_list)
                        printed = True

                    display_self_relation(self_relation)

                    for trio in current_list:
                        trio.display(current_list)
        
        if not any_trios:
            print("None")

def cprint_trio_relation(relation):
    cprint(relation, "red", None, ["underline"])

def cprint_trio_imm(imm):
    cprint(imm, "yellow", None, ["underline"])

def cprint_trio_self_rel(self_rel, color = "blue"):
    cprint(self_rel, color, None, ["underline"])

def display_trio_relation(trio_relation):
    if trio_relation is se_se:
        cprint_trio_relation("Super Effective - Super Effective")
    elif trio_relation is nve_nve:
        cprint_trio_relation("Not Very Effective - Not Very Effective")
    elif trio_relation is neu_neu:
        cprint_trio_relation("Neutral - Neutral")
    elif trio_relation is se_neu:
        cprint_trio_relation("Super Effective - Neutral")
    elif trio_relation is se_nve:
        cprint_trio_relation("Super Effective - Not Very Effective")
    elif trio_relation is nve_neu:
        cprint_trio_relation("Not Very Effective - Neutral")

def display_immunity(imm_list):
    if imm_list is no_immunity_list:
        cprint_trio_imm("   No Immunities")
    elif imm_list is one_immunity_list:
        cprint_trio_imm("   One Immunity")
    elif imm_list is multiple_immunity_list:
        cprint_trio_imm("   Multiple Immunities")
    else:
        cprint_trio_imm("   Mixed Immunities")

def display_self_relation(self_relation):
    if self_relation is self_se:
        cprint_trio_self_rel("      Self Super Effective:")
    elif self_relation is self_nve:
        cprint_trio_self_rel("      Self Not Very Effective:")
    elif self_relation is self_neu:
        cprint_trio_self_rel("      Self Neutral:")
    else: 
        cprint_trio_self_rel("      No Self Relation:")


display(trio_relationships)


