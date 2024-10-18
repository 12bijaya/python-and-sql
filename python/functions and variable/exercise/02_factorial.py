# using recursion
def main():
    x = int(input("enter the number: "))
    y = fact(x)
    print(f"the factorial of {x} is: {y}")
def fact(a):
    if a==1:
        return 1
    else:
        return (a*fact(a-1))
main()