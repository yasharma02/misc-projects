frameRarity = {"wood": 0.1368, "silver" : 0.13, "clear": 0.1118, "gold" : 0.1040, "black": 0.0936, "marble" : 0.0832, 
                "granite": 0.0702, "fur" : 0.0650, "caviar": 0.0520, "galaxy" : 0.0468, "rainbow": 0.0390, "emerald" : 0.0260, 
                "pearl": 0.0208, "neon" : 0.0156, "champagne": 0.0052}
print()
print("*************************")
print()

sum = 0
for key in frameRarity:
    sum = sum + frameRarity[key]
print(sum)
print()

gratitude = {"lava": 279, "gold" : 279, "bubble": 279, "diamond" : 279, "holo": 279}
selfAwa = {"lava": 3126, "gold" : 2085, "bubble": 4689, "diamond" : 1043, "holo": 1043}
accountable = {"lava": 4689, "gold" : 2663, "bubble": 1043, "diamond" : 2663, "holo": 1043}
optimism = {"lava": 4689, "gold" : 2085, "bubble": 2663, "diamond" : 2085, "holo": 1043}
empathy = {"lava": 4689, "gold" : 2663, "bubble": 6231, "diamond" : 2663, "holo": 279}
kindness = {"lava": 2085, "gold" : 2085, "bubble": 2085, "diamond" : 1043, "holo": 1043}
tenacity = {"lava": 2663, "gold" : 2085, "bubble": 1303, "diamond" : 279, "holo": 279}
curiosity = {"lava": 4689, "gold" : 2085, "bubble": 3126, "diamond" : 2085, "holo": 1043}
patience = {"lava": 4689, "gold" : 2085, "bubble": 2085, "diamond" : 2663, "holo": 1043}
conviction = {"lava": 279, "gold" : 279, "bubble": 279, "diamond" : 279, "holo": 279}
humility = {"lava": 4689, "gold" : 1043, "bubble": 2663, "diamond" : 2663, "holo": 1043}
ambition = {"lava": 2663, "gold" : 2663, "bubble": 1043, "diamond" : 1043, "holo": 279}
fuckingCandor = {"lava": 2085, "gold" : 2085, "bubble": 1257, "diamond" : 1257, "holo": 1043}
koala = {"lava": 106, "gold" : 106, "bubble": 106, "diamond" : 106, "holo": 54}
paperHands = {"lava": 106, "gold" : 106, "bubble": 106, "diamond" : 106, "holo": 54}
ogre = {"lava": 3, "gold" : 3, "bubble": 3, "diamond" : 3, "holo": 3}

tokenName = {"gratitude": gratitude, "selfAwa": selfAwa, "accountable": accountable, "optimism": optimism, "empathy": empathy, 
            "kindness": kindness, "tenacity": tenacity, "curiosity": curiosity, "patience": patience, "conviction": conviction, 
            "humility": humility, "ambition": ambition, "fuckingCandor": fuckingCandor, "koala": koala, "paperHands": paperHands, 
            "ogre": ogre}

tokenCountList = {}
for token in tokenName:
    total = 0
    tokenObj = tokenName[token]
    for specRarity in tokenObj:
        total = total + tokenObj[specRarity]
    tokenCountList[token] = total

#print(tokenCountList)
#print()

tokenCountList = dict(sorted(tokenCountList.items(), key = lambda kv:kv[1]))
print("tokens sorted by total count")
print(tokenCountList)
print()

for name in tokenCountList:
    print("--------- starting for token " + name + " ---------------")
    print()
    tokenObj = tokenName[name]
    print(tokenObj)
    print()
    tokenObj = dict(sorted(tokenObj.items(), key = lambda kv:kv[1]))
    print(tokenObj)
    print()
    for specRarity in tokenObj:
        frameRaritybyToken = {}
        for frame in frameRarity:
            frameRaritybyToken[frame] = frameRarity[frame]*tokenObj[specRarity]
        frameRaritybyToken = dict(sorted(frameRaritybyToken.items(), key = lambda kv:kv[1]))
        print("token " + name + ", spec rarity " + specRarity)
        print(frameRaritybyToken)
        print()
    print("--------- ending for token " + name + " ---------------")
    print()
print("*************************")
print()