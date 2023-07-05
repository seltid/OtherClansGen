# Determine other clans' names
with open('saves/currentclan.txt', 'r') as f:
    currentclan = f.read()
currentclan = 'saves/' + str(currentclan) + 'clan.json'

with open(currentclan, 'r') as f:
    clanContent = f.readlines()
    for line in clanContent:
        if line.startswith('    "other_clans_names":'):
            clanContentLine = []
            clanContentLine.append(line)
otherClanNames = str(clanContentLine).replace('"other_clans_names": "', '').replace('"', '').replace(' ', '') \
    .replace("[", "").replace("'", "")
otherClansList = otherClanNames.split(",")
otherClansListOriginal = otherClansList[:-1]

# Determine how many clans there are, and how many buttons to make
if len(otherClansListOriginal) == 3:
    buttons_needed = 3
elif len(otherClansListOriginal) == 4:
    buttons_needed = 4
else:
    buttons_needed = 5
otherClansList = otherClansListOriginal
otherClansList.append('blank')
otherClansList.append('blank')
otherClansList.append('blank')
otherClansList.append('blank')