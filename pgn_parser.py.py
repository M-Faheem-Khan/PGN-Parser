import sys
import csv

fields = ["WhiteElo", "BlackElo", "TimeControl", "Winner", "Date", "White", "Black", "Termination"]

def extract_game_data(fname):
    rounds =[]
    with open (fname) as f:
        lines = f.read().strip().split("\n")
        round = {}
        for line in lines:
            if line.startswith("["):

                if line.startswith("[Event"):
                    rounds.append(round)
                    round = {}

                l = line.replace("[", "").replace("]", "").replace('"', "")
                l = l.split(" ")
                if l[0] in fields:
                    if l[0] == "Termination":
                        round[l[0]] = l[-1]
                        round["Winner"] = l[1]
                    elif l[0] == "Date":
                        date = l[1].replace(".", "/")
                        round[l[0]] = date
                    else:
                        round[l[0]] = l[1]
            
    return rounds

if __name__ == "__main__":
    rounds = extract_game_data(sys.argv[1])


    with open("parsed_game_data.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for round in rounds:
            if round != {}:
                writer.writerow(round)

    
    print("Done Writing Parsed Data to CSV file.")

# EOF