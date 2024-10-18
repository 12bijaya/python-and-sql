i = 0
while i!=3:
    print("cow")
    i += 1

# finding data type
print(type(i))

# for loop
for _ in range(5):
    print("gu kha")

# print multiple times
print("meow\n" * 3, end="")

# asking from user
while True:
    x = int(input("enter the value of x: "))
    if x>0:
        break
for _ in range(x):
    print("meow")