names = []

for _ in range(5):
    name = input("what is your name:_")
    names.append(name)

file = open("name.txt", "a")
for name in sorted(names):
    print(f"hello, {name}")
    file.write(name+"\n")
file.close()


with open("name.txt","r") as file:
    for line in file:
        print("hello",line.rstrip())
        
names = []
with open("name.txt") as file:
    for line in file:
        names.append(line.strip())
        
for name in sorted(names, reverse=False):
    print(f"hello {name}")


with open("student.cvs") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")