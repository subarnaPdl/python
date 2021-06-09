try:
    a = int(input("Enter a number: "))
    print(f"{a} is negative" if a < 0 else f"{a} is positive")


# For all kinds of error
# except Exception as e:
#     print(f"Following error occured: {e}")


# For specific error
except TypeError:
    print("Type error occured.")

except ValueError:
    print("Value error occured.")

except:
    print("Error occured.")

else:
    # This is executed only if the try was successful.
    print("Code execution was successful.")

finally:
    # This is executed only if the try was successful.
    print("Nice to meet you.")
