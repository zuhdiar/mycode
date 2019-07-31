#!/usr/bin/env python3

calc1 = 0.0
calc2= 0.0
operation = " "
while (calc1 !="q"):
    print("\nfirst operation?, or q to quit: ")
    calc1=input()
    if calc1.lower =="q":
        break
    calc1 = float(calc1)
    print("\nsecond iperator?,or q to quit: ")
    calc2=input()
    if calc2.lower =="q":
        break
    calc2 = float(calc2)
    print("operation (+ or -): ")
    operation = input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation == "-":
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry, restarting ..." )

