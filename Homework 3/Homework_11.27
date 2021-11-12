# Trevon McKenzie
# 1880601

def by_jersey(e):
    return e['Jersey Number']

def add_player():
    jersey_number = int(input("Enter a new player's jersey number: "))
    player_rating = int(input("Enter the player's rating: "))
    team_info.append({})
    team_info[-1]['Jersey Number'] = jersey_number
    team_info[-1]['Player Rating'] = player_rating
    team_info.sort(key=by_jersey)

def delete_player():
    i = 0
    jersey_number = int(input("Enter a jersey number:\n"))
    for player in team_info:
        if jersey_number == player.get('Jersey Number'):
            del team_info[i]
        i += 1

def update_rating():
    i = 0
    jersey_number = int(input("Enter a jersey number:\n "))
    player_rating = int(input("Enter a new rating for player:\n "))
    for player in team_info:
        if jersey_number == player.get('Jersey Number'):
            team_info[i]['Player Rating'] = player_rating
        i += 1

def above_a_rating():
    player_rating = int(input("Enter a rating:\n"))
    print("ABOVE {}".format(player_rating))
    for player in team_info:
        if player['Player Rating'] > player_rating:
            print("Jersey number: {}, Rating: {}".format(player['Jersey Number'], player['Player Rating']))

def output_roster():
    print("ROSTER")
    for player in team_info:
        print("Jersey number: {}, Rating: {}".format(player['Jersey Number'], player['Player Rating']))


team_info = []
j = 0

for i in range(1, 6):
    team_info.append({})
    jersey_number = int(input("Enter player {}'s jersey number:\n".format(i)))
    player_rating = int(input("Enter player {}'s rating:\n\n".format(i)))
    team_info[j].update({'Jersey Number': jersey_number})
    team_info[j].update({'Player Rating': player_rating})
    j += 1

team_info.sort(key=by_jersey)

print("ROSTER")
for player in team_info:
    print("Jersey number: {}, Rating: {}".format(player['Jersey Number'], player['Player Rating']))

menu = '''\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n'''
print(menu)

user_choice = input("Choose an option:\n")

while user_choice != 'q':
    if user_choice == 'a':
        add_player()
        print(menu)
    if user_choice == 'd':
        delete_player()
        print(menu)
    if user_choice == 'u':
        update_rating()
        print(menu)
    if user_choice == 'r':
        above_a_rating()
        print(menu)
    if user_choice == 'o':
        output_roster()
        print(menu)
    user_choice = input("Choose an option:\n")


