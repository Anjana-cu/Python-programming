
def calculate_bill(units):
    if units < 0:
        raise ValueError("Units cannot be negative.")

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + (units - 100) * 7
    elif units <= 300:
        bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    else:
        bill = (100 * 5) + (100 * 7) + (100 * 10) + (units - 300) * 15

    return bill


try:
    units = float(input("Enter units consumed: "))
    total_bill = calculate_bill(units)

except ValueError as e:
    print("Input Error:", e)

except Exception as e:
    print("Unexpected Error:", e)

else:
    print("\nUnits Consumed:", units)
    print("Total Electricity Bill: ₹", total_bill)

finally:
    print("\nThank you for using the Electricity Bill Calculator.")
