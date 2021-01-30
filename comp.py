name=["alice","bob"]
title=["software","hardware"]
dict1={i:j for i,j in zip(name,title)}
for key in dict1:
    print(key)
print()
for value in dict1.values():
    print(value)
print()
for key,value in zip(dict1.keys(), dict1.values()):
    print(key, value)
print()
for key, value in dict1.items():
  print(key, value)
