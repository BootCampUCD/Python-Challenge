#Budget Data CSV
import os
import operator
import csv


votescast = 0
Correy = 0
CorreyP = 0
Khan = 0
KhanP = 0
Li = 0
LiP = 0
Otooley = 0
OtooleyP = 0
Winner = 0
Candidate = str
Winnername = str

csvpath = os.path.join("election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        votescast += 1
        Candidate = row[2]
        if Candidate == "Correy":
            Correy += 1
        if Candidate == "Khan":
            Khan += 1
        if Candidate == "Li":
            Li += 1
        if Candidate == "O'Tooley":
            Otooley += 1
    next

CorreyP = round ((Correy / votescast)*100,3)
KhanP = round((Khan / votescast)*100,3)
LiP = round((Li / votescast)*100,3)
OtooleyP = round((Otooley / votescast)*100,3)

Winner = CorreyP
Winnername = "Correy"
if Winner < KhanP:
    Winner = KhanP
    Winnername = "Khan"
if Winner < LiP:
    Winner = LiP
    Winnername = "Li"
if Winner < OtooleyP:
    Winner = OtooleyP
    Winnername = "O'Tooley"

print()
print("Election Results")
print("-------------------------")
print("Total votes: ", votescast)
print("-------------------------")
print("Khan: ", "%.3f%%" % KhanP, "(",Khan, ")")
print("Correy: ", "%.3f%%" % CorreyP, "(", Correy, ")")
print("Li: ", "%.3f%%" % LiP, "(", Li, ")")
print("O'Tooley: ", "%.3f%%" % OtooleyP, "(", Otooley, ")")
print("-------------------------")
print("Winner: ", Winnername)
print("-------------------------")



