'''
Finds new potential options for starter pokemon trios. (Water/Fire/Grass Excluded)
Pokemon categorized based on number of immunities and their self relation.
Trios of pokemon that obey two sets of triangular relationships are grouped together.
Pokemon are then displayed based on trio relationship -> number of immunities -> self relation.
With:
  Least Strict Restrictions: ~1800 trios
  Semi-Strict Restrictions: ~50 trios
  Most Strict Restrictions: 7 trios
  Least Strict Monotype: 2trios
'''

from termcolor import cprint 
from list_generators import *
from trio_class import *
from relationship_populator import *

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
    count = 0
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
                elif not self_relation_required:
                    current_list = no_self_relation  

                if current_list:
                    any_trios = True
                    if not printed:
                        display_immunity(imm_list)
                        printed = True

                    display_self_relation(self_relation)

                    for trio in current_list:
                        trio.display(current_list)
                        count +=1
        
        if not any_trios:
            print("None")
    print(count)

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
    elif self_relation is self_imm:
        cprint_trio_self_rel("      Self Immune:")
    else: 
        cprint_trio_self_rel("      No Self Relation:")


display(trio_relationships)


