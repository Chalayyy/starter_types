class Pokemon:

    # param: [Type] Can be a single Type or 2 unique Types.
    def __init__(self, *typing):
        self.typing = typing

    def __repr__(self):
        return "/".join(str(typ) for typ in self.typing)

    # param: [Pokemon] Attacking Pokemon
    # return [Array<Int>] All effectivenesses of attacker's types on defender. 
    def attack(self, def_pokemon):
        effectiveness = []
        for typ in self.typing:
            effectiveness.append(typ.attack(def_pokemon))
        return effectiveness