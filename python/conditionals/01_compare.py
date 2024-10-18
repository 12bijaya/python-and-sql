x = int(input('put the value of x '))
y = int(input('put the value of y '))
#using if as a conditional sentence
if x>y:
    print(x,' is greater than', y)
if y>x:
    print(y,' is greater than', x)
if x==y:
    print(x, 'and y is equal', y)
# this is the not correct way of programming 

# using elif (Improved form of code)

if x>y:
    print(x,' is greater than', y)
elif y>x:
    print(y,' is greater than', x)
else :
    print(x, 'and y is equal', y)

# using or as a conditional sentence
if x>y or y>x:
    print(x,' is not equal', y)
else:
    print(x, 'and y is equal', y)

# using != operator
if x!=y:
    print(x,' is not equal', y)
else:
    print(x, 'and y is equal', y)