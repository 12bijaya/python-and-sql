def main():
    print_column(3)
    print_row(4)
    print_square(3)



def print_column(height):#for tower
    for _ in range(height):
        print("#")

def print_row(length):#for ubstacle
    print("?" * length, end = "")
    print()

def print_square(size):#for the block
    for i in range(size):#for vertical column
        for j in range(size):#for horizontal row
            print("#",end="")#printing brick
        print() 

main()