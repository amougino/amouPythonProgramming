
armors = ["chainmail", "golden", "diamond", "netherite", "iron"]

pieces = ["helmet", "chestplate", "leggings", "boots"]

trims = ["crying_obsidian", "echo_shard", "ender_pearl", "glowstone", "magma_cream", "netherite_scrap", "netherrack", "obsidian", "popped_chorus_fruit", "prismarine"]



for trim in trims:
    for armor in armors:
        for piece in pieces:
            file = armor + "_" + piece + "_" + trim + "_trim.json"
            f = open(file, "w")
            content = [
                "{\n",
                '  "parent": "minecraft:item/generated",\n',
                '  "textures": {\n',
                '    "layer0": "minecraft:item/' + armor + '_' + piece + '",\n',
                '    "layer1": "minecraft:trims/items/' + piece + '_trim_' + trim + '"\n',
                '  }\n',
                '}'
            ]
            f.writelines(content)
            f.close()
    
    file = "turtle_helmet_" + trim + "_trim.json"
    f = open(file, "w")
    content = [
        "{\n",
        '  "parent": "minecraft:item/generated",\n',
        '  "textures": {\n',
        '    "layer0": "minecraft:item/turtle_helmet",\n',
        '    "layer1": "minecraft:trims/items/helmet_trim_' + trim + '"\n',
        '  }\n',
        '}'
    ]
    f.writelines(content)
    f.close()