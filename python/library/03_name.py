import sys  #using this function we can direcly write to our program with prompt
#check for error
if len(sys.argv) < 2 :
    sys.exit("to few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("to many arguments")
print("hello my name is ", sys.argv[1])

for arg in sys.argv[1:-1]:
    print("hello my name is ",arg)