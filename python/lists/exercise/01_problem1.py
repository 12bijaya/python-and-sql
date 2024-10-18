def main():
    numbers = []
    strings = []
    a = int(input("how many variables you want to put:_"))
    for num in range(a):
        x = num_from_users()
        y = string_from_users() 
        numbers.append(x)
        strings.append(y)
    print(numbers, end="\n")
    print(strings, end="\n")
    print(f"the second no in the numbers is: {numbers[1]}")
def num_from_users():
    return int(input("enter the number:_"))
def string_from_users():
    return input("enter the strings:_")
main()