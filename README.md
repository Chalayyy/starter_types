Fire/Water/Grass is the iconic trio that every starter pokemon has been a part of since Pokemon Gen 1. But what if we could find another trio of types or type combinations that worked just as well for a hypothetical new trio?

starter_types.py will display all trios of pokemon type combinations that satisfy a set of requirements (below). mono_starter_types.py contains the same base code, but only considers individual types, not combinations. All data is displays is already displayed in starter_types.py, but this makes it easier to see this specific subset of the data.

The requirements are:

1. Pokemon must obey some type of dual-relationship with the other pokemon in the trio. For example, they are super effective one way and not very effective the other way, just like the traditional trio. Or perhaps they are neutral one way and neutral the other way. It doesn’t matter as long as all the pokemon in the trio follow the rule. (There are 6 possible relationships: super effective-super effective, super effective-neutral, super effective-not very effective, neutral-neutral, neutral-not very effective, not very effective-not very effective.)
2. Pokemon should share the same self-relationship. Just like Water, Grass, and Fire all resist themselves, all pokemon within the trio should share some self-relationship, whether it’s super effective, neutral, or not very effective.
3. Pokemon should have the same number of immunities or have a direct relationship between the number of immunities had vs immunities given. Water, Grass, and Fire all have 0 immunities and have 0 types immune to them. We want something similar for our trio.
4. We are excluding Water, Grass, and Fire from our possible types. They had a good 20 year run, but now we want something new.
5. No two pokemon within a trio may have a type in common between them.

Pokemon are then displayed based on the requirements they obey. A key is included in the output. 
