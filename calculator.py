print("(__________Hello__________)")
while True:
    try:
        n1 = (int(input("1'st number: ")))
        op = (input("Enter Operation: ")) 
        n2 = (int(input("2'nd number: ")))
    except ValueError:
            print("ERROR!")
            continue
    

    if op not in ['+', '-', '*', '/']:
            print("Please Enter a Valid Operation ")
            continue


    if n1 == 0 or n2 == 0:
        print("Error! Please Enter a Number Other Than 0")
        continue

    else:       
        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "/":
            result = n1 / n2
        elif op == "*":
            result = n1 * n2
        else:
            print("Try Again")

    print("Result: ", result)