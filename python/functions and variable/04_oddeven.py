def main():
    x=int(input("enter the number to check. "))
    if even(x):
        print("even")
    else :
        print("odd")
def even(n):
    if n%2==0 :
        return True
    else :
        return False
    # most better
    return(n%2==0)

    # also you can do 

    return True if n%2==0 else False
main()