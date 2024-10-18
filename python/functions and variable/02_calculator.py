#intizer
''''
x = 1
y = 2
z = x + y
print(z)
'''
#input from the user 

x = int(input('what is the value of x? '))
y = int(input('what is the value of y? '))
#also z = int(x)+int(y)
z = x + y
#also print (x+y)
print(f'the sum of two numbers is {z}')

#also one best method
print(int(input('what is the value of x? ')) + int(input('what is the value of y? ')))



#float
x = float(input('what is the value of x? '))
y = float(input('what is the value of y? '))
#also z = int(x)+int(y)
z = x + y
#also print (x+y)
print(f'the sum of two numbers is {z}')

#also one best method
print(float(input('what is the value of x? ')) + float(input('what is the value of y? ')))

#rounding up the number 
print(round(x+y))
print(f'{z:.2f}')
print(round(z,2))

# to print with comma
print(f"{z:,}")