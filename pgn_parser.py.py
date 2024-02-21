"""Parses Chess game data(PGN) into a CSV file."""

import sys
import csv

fields = [
    "WhiteElo",
    "BlackElo",
    "TimeControl",
    "Winner",
    "Date",
    "White",
    "Black",
    "Termination",
]


def extract_game_data(fname):
    """Parses data from a given PGN file."""
    matches = []
    with open(fname, encoding="utf-8") as pgn_f:
        lines = pgn_f.read().strip().split("\n")
        match = {}
        for line in lines:
            if line.startswith("["):

                if line.startswith("[Event"):
                    matches.append(match)
                    match = {}

                l = line.replace("[", "").replace("]", "").replace('"', "")
                l = l.split(" ")
                if l[0] in fields:
                    if l[0] == "Termination":
                        match[l[0]] = l[-1]
                        match["Winner"] = l[1]
                    elif l[0] == "Date":
                        date = l[1].replace(".", "/")
                        match[l[0]] = date
                    else:
                        match[l[0]] = l[1]

    return matches


if __name__ == "__main__":
    game_rounds = extract_game_data(sys.argv[1])

    with open("parsed_game_data.csv", "w", encoding="utf-8") as csv_f:
        writer = csv.DictWriter(csv_f, fieldnames=fields)
        writer.writeheader()
        for game_round in game_rounds:
            if game_round != {}:
                writer.writerow(game_round)

    print("Done Writing Parsed Data to CSV file.")

# EOF
