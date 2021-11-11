from timeit import timeit




a = """
with open("a.txt", "r") as file:
    s=0
    for line in file.readlines():
        if line.strip().isdigit():
            s += int(line.strip())"""

print(timeit(a, number=50)/50)


a = """
with open("a.txt", "r") as file:
    s=0
    for line in file:
        if line.strip().isdigit():
            s += int(line.strip())"""

print(timeit(a, number=50)/50)


a = """
with open("a.txt", "r") as file:
    s=0
    k = ( int(line.strip()) for line in file if line.strip().isdigit())
    s = sum(k)"""
    
print(timeit(a, number=50)/50)
