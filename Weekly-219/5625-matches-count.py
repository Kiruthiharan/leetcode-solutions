n = 14

teams = n
matches = 0
while (teams != 1):
    if (teams % 2 == 0):
        matches += int(teams/2)
        teams = int (teams/2)
    else:
        matches += int ((teams- 1)/2)
        teams = int( (teams-1) / 2) + 1

print(matches)