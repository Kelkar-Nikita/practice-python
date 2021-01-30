name = ["alice", "bob", "radha"]
title = ["Data software", "hardware", "Data Scientist"]
dataPersons = {n: t for n, t in zip(name, title) if "Data" in t}
print(dataPersons)
dict1 = {i: j for i, j in zip(name, title)}
for key in dict1:
    print(key)
print()
for value in dict1.values():
    print(value)
print()
for key, value in zip(dict1.keys(), dict1.values()):
    print(key, value)
print()
for key, value in dict1.items():
    print(key, value)
