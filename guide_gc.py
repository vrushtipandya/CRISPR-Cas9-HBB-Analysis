guide = "AAGGTGAACGTGGATGAAGT"

g = guide.count("G")
c = guide.count("C")

gc = ((g + c) / len(guide)) * 100

print("Guide RNA =", guide)
print("Length =", len(guide))
print("GC Content =", round(gc, 2), "%")