file = open("../data/HBB_sequence.fasta", "r")

header = file.readline()

sequence = file.read().replace("\n", "").upper()

file.close()

count = 0

print("Guide RNA Candidates:\n")

for i in range(len(sequence) - 23):
    pam = sequence[i+20:i+23]

    if pam[1:] == "GG":
        guide = sequence[i:i+20]
        count += 1

        print("Guide", count)
        print("Guide RNA :", guide)
        print("PAM       :", pam)
        print()

print("Total Candidate gRNAs =", count)