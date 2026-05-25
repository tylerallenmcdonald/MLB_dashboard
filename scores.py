import statsapi

# Get today's games
games = statsapi.schedule(sportId=1)

# Print games and scores 
for game in games:
    home = game['home_name']
    away = game['away_name']
    status = game['status']
    home_score = game['home_score']
    away_score = game['away_score']
    print(f"{away} @ {home} | {away_score}-{home_score} | {status}")