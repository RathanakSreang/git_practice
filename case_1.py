# - It returns "Fizz" if parameter(num) is divisible by 3.
def fizz(num):
    if num % 3 == 0:
        return "Fizz"
    return str(num)

print(fizz(3))
print(fizz(5))