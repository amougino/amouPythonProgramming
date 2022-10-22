crafts = []

important = '(Acacia, Spruce, Dark oak, Oak, Warped, Crimson, Birch, Jungle) Log = Log \n(Acacia, Spruce, Dark oak, Oak, Warped, Crimson, Birch, Jungle) Plank = Plank \nCharcoal, Coal = Coal \nBlackstone, cobblestone = Cobblestone'

plank_4 = ['0','0','0','0','Log','Log','0','0','0','plank_4']
stick_4 = ['0','0','0','0','Plank','0','0','Plank','0','stick_4']
torch_4 = ['0','0','0','0','Coal','0','0','Stick','0','torch_4']
craftingTable = ['0','0','0','Plank','Plank','0','Plank','Plank','0','craftingtable_1']
furnace = ['Cobblestone','Cobblestone','Cobblestone','Cobblestone','0','Cobblestone','Cobblestone','Cobblestone','Cobblestone','furnace_1']
chest = ['Plank','Plank','Plank','Plank','0','Plank','Plank','Plank','Plank','chest_1']
ladder_3 = ['Stick','0','Stick','Stick','Stick','Stick','Stick','0','Stick','ladder_3']


crafts.append(plank_4)
crafts.append(stick_4)
crafts.append(torch_4)
crafts.append(craftingTable)
crafts.append(furnace)
crafts.append(chest)
crafts.append(ladder_3)

listCrafts = []

def availableWith(craft):
    length = len(crafts)
    for i in range(length):
        for o in range(9):
            if crafts[i][o] == craft:
                e = crafts[i][9]
                e = e.split('_')
                length2 = len(listCrafts)
                f = 0
                for p in range(length2):
                    if listCrafts[p] == e[0]:
                        f = 1
                if f == 0:
                    listCrafts.append(e[0])
                f = 0
    print(important)
    print('With',craft,'you can craft :')
    print(listCrafts)
    length = len(listCrafts)
    for i in range(length):
        listCrafts.clear()

def findCraft(item):
    length = len(crafts)
    for i in range(length):
        b = crafts[i][9]
        c = b.split('_')
        if c[0] == item:
            print(important)
            print(c[0],':')
            print(' ')
            for o in range(3):
                d = o*3
                print(crafts[i][d],'   ',crafts[i][d+1],'   ',crafts[i][d+2])
                print(' ')
            print('Quantity',':',c[1])

#availableWith('Log')
findCraft('torch')