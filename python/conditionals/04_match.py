name = input("Input the name of the user ")
match name:
    case "hari" | "sita" | "janaki":
        print("Pokhara")
    case "Ram" | "ravan" | "rubina":
        print("Janakpur")
    case _:
        print("Not found")