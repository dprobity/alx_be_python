# match statement 

day = input("Please the day")

match day:
    case "monday" | "tuesday" | "wednesday":
        print("There is work today ooH!")
    case "saturday" | "sunday":
        print("this is weekend")
    case _:
        print("inc=valid day")




# looping, is condition met? else repeat until the condition is met 

fruits = ["banana", "apple", "orange", "mango"]


