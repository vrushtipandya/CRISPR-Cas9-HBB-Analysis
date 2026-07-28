file = open("../data/HBB_sequence.fasta", "r")

header = file.readline()

sequence = file.read().replace("\n", "")

file.close()

print("Sequence Length =", len(sequence))

print("A Count =", sequence.count("A"))
print("T Count =", sequence.count("T"))
print("G Count =", sequence.count("G"))
print("C Count =", sequence.count("C"))
