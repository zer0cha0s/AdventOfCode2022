file = open('./Day 19/input.txt').read().strip()
lines = [x for x in file.split('\n')]

#['Blueprint', '30:', 'Each', 'ore', 'robot', 'costs', '2', 'ore.', 'Each', 'clay', 'robot', 'costs', '4', 'ore.', 'Each', 'obsidian', 'robot', 'costs', '3', 'ore', 'and', '20', 'clay.', 'Each', 'geode', 'robot', 'costs', '2', 'ore', 'and', '17', 'obsidian.']

#[(0, 'Blueprint'), (1, '1:'), (2, 'Each'), (3, 'ore'), (4, 'robot'), (5, 'costs'), (6, '4'), (7, 'ore.'), (8, 'Each'), (9, 'clay'), (10, 'robot'), (11, 'costs'), (12, '4'), (13, 'ore.'), (14, 'Each'), (15, 'obsidian'), 
# (16, 'robot'), (17, 'costs'), (18, '2'), (19, 'ore'), (20, 'and'), (21, '11'), (22, 'clay.'), (23, 'Each'), (24, 'geode'), (25, 'robot'), (26, 'costs'), (27, '2'), (28, 'ore'), (29, 'and'), (30, '7'), (31, 'obsidian.')]

#build blueprint sets
for line in lines:
    words = line.split()
    print(list(enumerate(words)))
    ore_value = int(words[6])
    clay_value = int(words[12])
    obsidian_ore_value, obsidian_clay_value = int(words[18]), int(words[21])
    geode_ore_value, geode_obsidian_value = int(words[27]), int(words[30])
    print(ore_value, clay_value, obsidian_ore_value, obsidian_clay_value, geode_ore_value, geode_obsidian_value)

    