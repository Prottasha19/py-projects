import random

with open("team.txt", "r") as f:
	teams = f.read().splitlines()
	
# shuffle team names
random.shuffle(teams)

with open("shuffled_teams.txt", "w") as f:
    for team in teams:
        f.write(team + "\n")






# print shuffled team names
print(teams)
