import statsapi
import json

# Look at a single game in detail
games = statsapi.schedule(sportId=1)
print("=== SINGLE GAME FIELDS ===")
print(json.dumps(games[0], indent=2))
# current_inning, inning_state (top/bottom), venue_name

# Player stats - try a player ID (660271 = Shohei Ohtani)
player = statsapi.player_stat_data(660271, group="hitting", type="season")
print("\n=== PLAYER HITTING STATS ===")
print(json.dumps(player, indent=2))

# Team roster
roster = statsapi.roster(143)  # 143 = Phillies, change to your team
print("\n=== ROSTER FIELDS ===")
print(json.dumps(roster, indent=2))

standings = statsapi.standings_data()
print("\n=== STANDINGS DATA ===")
print(json.dumps(standings, indent=2))
