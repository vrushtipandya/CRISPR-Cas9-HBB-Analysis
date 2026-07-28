file = open("../data/HBB_sequence.fasta", "r")

header = file.readline()

sequence = file.read().replace("\n", "")

file.close()

reverse = sequence[::-1]

complement = reverse.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")

complement = complement.upper()

print("Reverse Complement Sequence:")
print(complement)