from list_generators import all_types
from termcolor import cprint 

neu_strictness = "semi-strict"
nve_strictness = "strict"
check_immune_balanced = True
self_relation_required = True
mono_type = False


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
        if all(map(lambda attack: any(eff > 1 for eff in attack), self.trio_attack_full())):
            return 0
        elif all(map(lambda attack: any(eff > 1 for eff in attack), self.trio_attack1())):
            return 1
        elif all(map(lambda attack: any(eff > 1 for eff in attack), self.trio_attack2())):
            return 2

    # param: [Array<Array<Int>>]
    # return [Int] Int representing cycle in which the trio can deal NEU damage
    def neutral_effective(self):
        # can only deal NEU damage
        if neu_strictness == "strict":
            if all(map(lambda attack: all(eff == 1 for eff in attack), self.trio_attack_full())):
                return 0
            elif all(map(lambda attack: all(eff == 1 for eff in attack), self.trio_attack1())):
                return 1
            elif all(map(lambda attack: all(eff == 1 for eff in attack), self.trio_attack2())):
                return 2
       # can deal NEU, may deal NVE damage
        elif neu_strictness == "semi-strict":
            if all(map(lambda attack: any(eff == 1 for eff in attack) and not(any(eff > 1 for eff in attack)), self.trio_attack_full())):
                return 0
            elif all(map(lambda attack: any(eff == 1 for eff in attack) and not(any(eff > 1 for eff in attack)), self.trio_attack1())):
                return 1
            elif all(map(lambda attack: any(eff == 1 for eff in attack) and not(any(eff > 1 for eff in attack)), self.trio_attack2())):
                return 2
        # can deal NEU damage and may deal any other
        elif neu_strictness == "non-strict":
            if all(map(lambda attack: any(eff == 1 for eff in attack), self.trio_attack_full())):
                return 0
            elif all(map(lambda attack: any(eff == 1 for eff in attack), self.trio_attack1())):
                return 1
            elif all(map(lambda attack: any(eff == 1 for eff in attack), self.trio_attack2())):
                return 2

    # param: [Array<Array<Int>>]
    # return [Int] Int representing cycle in which the trio can deal NVE damage
    def not_very_effective(self):
        # can only deal NVE damage
        if nve_strictness == "strict":
            if all(map(lambda attack: all(eff < 1 for eff in attack), self.trio_attack_full())):
                return 0
            elif all(map(lambda attack: all(eff < 1 for eff in attack), self.trio_attack1())):
                return 1
            elif all(map(lambda attack: all(eff < 1 for eff in attack), self.trio_attack2())):
                return 2
        # can deal NVE damage, may deal NEU
        if nve_strictness == "semi-strict":
            if all(map(lambda attack: any(eff < 1 for eff in attack) and not(any(eff > 1 for eff in attack)), self.trio_attack_full())):
                return 0
            elif all(map(lambda attack: any(eff < 1 for eff in attack) and not(any(eff > 1 for eff in attack)), self.trio_attack1())):
                return 1
            elif all(map(lambda attack: any(eff < 1 for eff in attack) and not(any(eff > 1 for eff in attack)), self.trio_attack2())):
                return 2
        # can deal NVE damage, may deal any other damage
        if nve_strictness == "non-strict":
            if all(map(lambda attack: any(eff < 1 for eff in attack), self.trio_attack_full())):
                return 0
            elif all(map(lambda attack: any(eff < 1 for eff in attack), self.trio_attack1())):
                return 1
            elif all(map(lambda attack: any(eff < 1 for eff in attack), self.trio_attack2())):
                return 2

    # return [Boolean] Do any two pokemon share a type? 
    # We exclude these trios later since no trio has ever shared a typing before.
    def share_type(self):
        set1 = set(list(self.p1.typing))
        set2 = set(list(self.p2.typing))
        set3 = set(list(self.p3.typing))
        return (set1 & set2) or (set1 & set3) or (set2 & set3)

    
    # param: [Pokemon] Pokemon in trio
    # return [Integer] How many immunities this pokemon gives
    # A Normal/Fighting type would count as giving 2 immunities
    def imm_given(self, pokemon):
        return sum([len(pokemon.typing[y].ne_list) for y in range(len(pokemon.typing))])

    '''
    Note: No starter pokemon has ever had a type which another type was immune to.
    Though Bulbsaur's poison typing means that it gives 1 immunity to steel,
    steel type was introduced in GenII, after Bulbasaur was a starter. 
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
        if check_immune_balanced == True:
            imm_in_trio1 = [0 in attack for attack in self.trio_attack1()]
            imm_in_trio2 = [0 in attack for attack in self.trio_attack2()]
            if all(imm_in_trio1) or all(imm_in_trio2):
                return True
            elif any(imm_in_trio1) or any(imm_in_trio2):
                return False
            else:
                return True
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