mountain = ["Fiji", "kilimanjaro", "Everest"]

del mountain[1]

mountain.insert(3, "Kangchenjunga")
mountain.append("Lhotse")

mountain.pop()

print (sorted(mountain))

print (sorted(mountain , reverse=True))

mountain.reverse()
print (mountain)

mountain.sort()
print (mountain)

mountain.sort(reverse=True)
print (mountain) 

print (f"\n{len(mountain)}")