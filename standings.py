import statsapi

standings = statsapi.standings_data()

# Division ID mapping
divisions = {
    200: "AL West",
    201: "AL East", 
    202: "AL Central",
    203: "NL West",
    204: "NL East",
    205: "NL Central"
}

# Print standings by division
for div_id, div_name in divisions.items():
    print(f"\n--- {div_name} ---")
    teams = standings[div_id]['teams']
    for team in teams:
        name = team['name']
        w = team['w']
        l = team['l']
        gb = team['gb']
        print(f"{name} | W: {w} L: {l} | GB: {gb}")

