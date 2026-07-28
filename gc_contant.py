file = open("../data/HBB_sequence.fasta", "r")

header = file.readline()

sequence = file.read().replace("\n", "")

file.close()

g = sequence.count("G")
c = sequence.count("C")

gc = ((g + c) / len(sequence)) * 100

print("GC Content =", round(gc, 2), "%")

