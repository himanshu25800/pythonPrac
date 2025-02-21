try:
    x = int(input("Enter a number"))
    result = 45/x
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occured {e}")
else :
    print("Operation done ")
finally : 
    print("Done with the work")