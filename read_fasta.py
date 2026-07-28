file = open("../data/HBB_sequence.fasta", "r")

header = file.readline()

sequence = file.read()

sequence = sequence.replace("\n", "")

print(header)

print(sequence)

print("Sequence Length =", len(sequence))

file.close()
