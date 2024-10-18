# student =[]
# with open("student.cvs") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student.append(f"{name} is in {house}")

# for stud in sorted(student):
#     print(stud)
        
student =[]
with open("student.cvs") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student.append(f"{name} is in {house}")
        studen = {}
        studen["name"] = name
        studen["house"] = house
        student.append(studen)
        
for studen in student:
    print(f"{studen['name']} is in {studen['house']}")