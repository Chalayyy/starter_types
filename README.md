Fire/Water/Grass is the iconic trio that every starter pokemon has been a part of since Pokemon Red & Blue. But what if we could find another trio of types or type combinations that worked just as well for a hypothetical new trio?

starter_trios.py displays all trios of pokemon type combinations that satisfy the set of requirements below. monotype_starter_trios.py contains the same base code, but only considers individual types, not pokemon with dual-typing. 

The requirements are:

1. Each pokemon in the trios obeys a dual-relationship with the other pokemon in the trio. For example, they are super effective one way and not very effective the other way, just like the traditional trio. Or they can are neutral one way and neutral the other way. It doesn’t matter as long as all the pokemon in the trio follow the rule. (There are 6 possible relationships: super effective-super effective, super effective-neutral, super effective-not very effective, neutral-neutral, neutral-not very effective, not very effective-not very effective.)
2. No two pokemon within a trio may have a type in common between them.
3. We are excluding Water, Grass, and Fire from our possible types. They had a good 20 year run, but now we want something new.
4. Pokemon have the same difference between their immunities had vs immunities given. Water, Grass, and Fire all have 0 immunities and have 0 types immune to them. We want something similar for our trio. For example, Ghost, Flying/Ground, and Fairy each have one more immunity than the number of types that are immune to them (2/1, 2/1, 1/0).
5. Pokemon should share the same self-relationship. Just like Water, Grass, and Fire all resist themselves, all pokemon within the trio should share some self-relationship, whether it’s super effective, neutral, or not very effective.

Pokemon are displayed based on the requirements they obey.

Data Printout: 

Super Effective - Super Effective
None
Not Very Effective - Not Very Effective
None
Neutral - Neutral
   No Immunities
      Self Not Very Effective:
1: Electric, Fighting/Ice, Poison/Rock
   Mixed Immunities
      Self Super Effective:
1: Dragon/Fairy, Ghost/Psychic, Ground/Rock
      Self Not Very Effective:
1: Electric, Fighting/Ice, Normal/Poison
2: Ice, Electric/Fairy, Ghost/Psychic
3: Electric/Fairy, Ghost/Psychic, Ice/Rock
Super Effective - Not Very Effective
None
Super Effective - Neutral
   Mixed Immunities
      Self Not Very Effective:
1: Ice, Bug/Ground, Dragon/Steel
2: Ice, Bug/Ground, Normal/Rock
Not Very Effective - Neutral
None
