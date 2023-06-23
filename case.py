# - It returns "Fizz" if parameter(num) is divisible by 3.
# - It returns "Buzz" if parameter(num) is divisible by 5.
def fizz(num):
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"

    return str(num)

print(fizz(3))
print(fizz(5))
print(fizz(7))