def great():
    x=int(input("enter the first no: "))
    y=int(input("enter the second no: "))
    if greatest(x,y):
        print(x," is greatest")
    else :
        print(y," is greatest")
def greatest(a,b):
    if a>b:
        return True
    else :
        return False
great()
