while True:
    try:
        x = int(input("what is x: "))
    except ValueError:
        print("x must be integer")
    else:
        break