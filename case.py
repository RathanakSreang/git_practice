# - It returns "Fizz" if parameter(num) is divisible by 3.
# - It returns "Buzz" if parameter(num) is divisible by 5.
# - It returns "FizzBuzz" if parameter(num) is divisible by 3 and 5.
def fizz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"

    return str(num)

print(fizz(3))
print(fizz(5))
print(fizz(7))
print(fizz(11))
print(fizz(15))
