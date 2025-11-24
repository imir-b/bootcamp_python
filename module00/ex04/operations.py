import sys

if len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    sys.exit(1)

if len(sys.argv) < 3:
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
    sys.exit(1)

try:
    a = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)
try:
    b = int(sys.argv[2])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)

res_sum = a + b
res_dif = a - b
res_pro = a * b
try:
    res_quo = a / b
except ZeroDivisionError:
    res_quo = "ERROR (division by zero)"
try:
    res_rem = a % b
except ZeroDivisionError:
    res_rem = "ERROR (modulo by zero)"

print("Sum:", int(res_sum))
print("Difference:", int(res_dif))
print("Product:", int(res_pro))
print("Quotient:", res_quo)
print("Remainder:", res_rem)