# Determine other clans' names
with open('saves/currentclan.txt', 'r') as f:
    currentclan = f.read()
currentclan2 = 'saves/' + str(currentclan) + 'clan.json'

with open(currentclan2, 'r') as f:
    clanContent = f.readlines()
    for line in clanContent:
        if line.startswith('    "other_clans_names":'):
            clanContentLine = []
            clanContentLine.append(line)
otherClanNames = str(clanContentLine).replace('"other_clans_names": "', '').replace('"', '').replace(' ', '') \
    .replace("[", "").replace("'", "")
otherClansList = otherClanNames.split(",")
otherClansListOriginal = otherClansList[:-1]
otherClansList = otherClansListOriginal

# Determine how many clans there are, and how many buttons to make
if len(otherClansListOriginal) == 1:
    buttons_needed = 3
    otherClansList.append('blank')
    otherClansList.append('blank')
    otherClansList.append('blank')
    otherClansList.append('blank')
elif len(otherClansListOriginal) == 2:
    buttons_needed = 3
    otherClansList.append('blank')
    otherClansList.append('blank')
    otherClansList.append('blank')
elif len(otherClansListOriginal) == 3:
    buttons_needed = 3
    otherClansList.append('blank')
    otherClansList.append('blank')
elif len(otherClansListOriginal) == 4:
    buttons_needed = 4
    otherClansList.append('blank')
else:
    buttons_needed = 5

all_sg_clans = otherClansList + [currentclan]