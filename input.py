
import re

# Email validation
email = input("Enter email: ")

if re.match(r'^[\w.]+@[\w.]+\.\w+$', email):
    print("Valid Email")
else:
    print("Invalid Email")

# Phone number validation
phone = input("\nEnter phone number: ")

if re.match(r'^[0-9]{10}$', phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

# Extract transaction ID
log = "Transaction ID: TXN12345"

result = re.findall(r'TXN[0-9]+', log)

print("\nTransaction ID:", result)
