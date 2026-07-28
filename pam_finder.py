file = open("../data/HBB_sequence.fasta", "r")

header = file.readline()

sequence = file.read().replace("\n", "").upper()

file.close()

print("Searching for PAM (NGG) sites...\n")

count = 0

for i in range(len(sequence) - 2):
    pam = sequence[i:i+3]

    if pam[1:] == "GG":
        count += 1
        print("Position:", i + 1, "PAM:", pam)

print("\nTotal PAM Sites Found =", count)