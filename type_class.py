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
        for typ in def_pokemon.typing:
            if typ in self.ne_list: 
                return 0
            elif typ in self.se_list: 
                damage_multiplier *= 2
            elif typ in self.nve_list: 
                damage_multiplier /= 2
        return damage_multiplier