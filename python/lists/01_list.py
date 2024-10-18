students = ["bijaya", "bikash", "saugat"]
print(students[1:3])#start from 1 to 3rd character of the lists 
for student in students:
    print(student)

# itterate
for i in students[0:2]:
    print(i)

# next way to print
for i in range(len(students)):
    print(i+1 , students[i])