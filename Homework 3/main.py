# 1880601
# Trevon McKenzie

class Team:
    def __init__(self):
        self.teamname = 'none'
        self.teamwins = 0
        self.team_losses = 0

    def get_win_percentage(self, team_wins, team_losses):
        win_percentage = team_wins / (team_wins + team_losses)
        return win_percentage


go_time1 = Team()
go_time1.teamname = input()
go_time1.teamwins = float(input())
go_time1.team_losses = float(input())

if (go_time1.get_win_percentage(go_time1.teamwins, go_time1.team_losses)) > 0.50:
    print("Congratulations, Team {} has a winning average!".format(go_time1.teamname))
else:
    print("Team {} has a losing average.".format(go_time1.teamname))