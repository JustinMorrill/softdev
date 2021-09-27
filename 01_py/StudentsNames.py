import random
pd1 = ["Alice", "Bob", "Charlie"]
pd2 = ["Dan", "Edward", "Frank"]
if random.randint(0, 1) == 0:
    print(pd1[random.randint(0, len(pd1) - 1)])
else:
    print(pd2[random.randint(0, len(pd2) - 1)])
