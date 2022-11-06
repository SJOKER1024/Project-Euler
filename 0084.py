import random
tile = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x = 0
CC = 0
CClist = [2,17,33]
Chance = 0
Chancelist = [7,22,36]

for i in range(10000000):
    y = random.randint(1,4) + random.randint(1,4)
    x += y
    if x >= 40:
        x = x%40
    if x == 10:
        tile[x] += 1
    elif x in CClist:
        CC += 1
        if CC == 1:
            x = 0
            tile[x] += 1
        elif CC == 2:
            x = 10
            tile[x] += 1
        elif CC == 16:
            CC = 0
            tile[x] += 1
        else:
            tile[x] += 1
    elif x in Chancelist:
        Chance += 1
        if Chance == 1:
            x = 0
            tile[x] += 1
        elif Chance == 2:
            x = 10
            tile[x] += 1
        elif Chance == 3:
            x = 11
            tile[x] += 1
        elif Chance == 4:
            x = 24
            tile[x] += 1
        elif Chance == 5:
            x = 39
            tile[x] += 1
        elif Chance == 6:
            x = 5
            tile[x] += 1
        elif Chance == 7 or Chance == 8:
            if x == 7:
                x = 15
                tile[x] += 1
            elif x == 22:
                x = 25
                tile[x] += 1
            else:
                x = 5
                tile[x] += 1
        elif Chance == 9:
            if x == 7:
                x = 12
                tile[x] += 1
            elif x == 22:
                x = 28
                tile[x] += 1
            else:
                x = 12
                tile[x] += 1
        elif Chance == 10:
            x -= 3
            if x == 33:
                CC += 1
                if CC == 1:
                    x = 0
                    tile[x] += 1
                elif CC == 2:
                    x = 10
                    tile[x] += 1
                elif CC == 16:
                    CC = 0
                    tile[x] += 1
                else:
                    tile[x] += 1
            else:
                tile[x] += 1
        elif Chance == 16:
            Chance = 0
            tile[x] += 1
        else:
            tile[x] += 1
    elif x == 30:
        x = 10
        tile[x] += 1
    else:
        tile[x] += 1

print(tile)
