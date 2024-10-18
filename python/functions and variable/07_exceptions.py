# def main():
#     x = get_int()
#     print(f"x is {x}")
# def get_int():
#     while True:
#         try:
#             x = int(input("what is x: "))
#         except ValueError:
#             print("x must be integer")
#         else:
#             return x
# main()


# more better way of doing it 
def main():
    x = get_int("what is x: ")
    print(f"x is {x}")
def get_int(prompt):#prompt provide the message from the main function
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x must be integer")
        else:
            return x
main()