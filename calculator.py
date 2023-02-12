import logging
logging.basicConfig(level=logging.DEBUG)

while True:
    
    print("Available operations:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Exit")
    
    choice = input("Please input a number of requested operation:")

    if choice == "5":
        print("You have left the Calculator")
        break

    else:

        x1 = float(input("Enter first number:"))
        x2 = float(input("Enter second number:"))

        logging.info(f"Entered numbers are:\nx1 = {x1}\nx2 = {x2}")

        if choice == "1":
            logging.info(f"Adding {x1} to {x2}")
            print(f"Addition:\n{x1} + {x2}, = {x1+x2}")

        elif choice == "2":
            logging.info(f"Subtracting {x1} to {x2}")
            print(f"Substraction:\n{x1} - {x2}, = {x1-x2}")

        elif choice == "3":
            logging.info(f"Multiplicating {x1} by {x2}")
            print(f"Multiplication:\n{x1} * {x2}, = {x1*x2}")

        elif choice == "4":
            if x2 == 0.0:
                logging.error("ZeroDivisionError: division by zero")
            else:
                logging.info(f"Dividing {x1} by {x2}")
                print(f"Division:\n{x1} / {x2}, = {x1/x2}")
        else:
            logging.error(f"There is no option {choice}. Select one available.")
            continue
        
    input("Press Enter to continue...")
    print()