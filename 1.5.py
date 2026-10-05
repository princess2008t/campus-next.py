#1
print(max(open("names.txt", "r").readlines()))
#2
names = open("names.txt").read().splitlines()
print(sum(len(name) for name in names))
#3
names = open("names.txt").read().splitlines()
min_len = min(len(name) for name in names)
print("\n".join(name for name in names if len(name) == min_len))
#4
names = open("names.txt").read().splitlines()
lengths = "\n".join(str(len(name)) for name in names)
open("name_length.txt", "w").write(lengths)
#5
length = int(input("Enter name length: "))
names = open("names.txt").read().splitlines()
print("\n".join(name for name in names if len(name) == length))