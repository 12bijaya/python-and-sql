def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        x = int(input("enter the number "))
        if x>0:
            break
    return x

def meow(n):
    for a in range(n):
        print("meow")

main()