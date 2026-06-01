day =int(input("Enter a value from 1 to 7 :"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wed - Thur")
    case _:
        print("Fri-Sunday")