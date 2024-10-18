#comment

#printing first code
print('Welcome to anime world')

#taking input with variable
name = input("enter your name? ").strip().title()
#name is variable strip is function to remove white space character 
"""
strip is used to remove white space character
name = name.strip()

title is used to capatilize 
name = name.title()

combinely it can also be used as
name = name.strip().title()
"""

#ways to print in differently 

#first one
print('hello')
print('name')

#second
print('hello', name) #coma is used as concatination

# third
print('hello '+name) #+ is an concatination operator

# fourth one
print(f"hello {name}")#f determine that name is variable and something special

# fifth
print('hello', end=" ")#end will determine what is in the end
print(name)

#sixth
print('hello'+name, sep=" ")#sep is used as what is used to seperate them

#to print only first name
first, last = name.split(' ')
print(f'hello {first}')
print('hello', first)

# also to capitalize
# name = name.Capitalize()
# print(name)
