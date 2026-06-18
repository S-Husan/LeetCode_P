# FizzBuzz Print 1-100, replace multiples of 3 with Fizz, 5 with Buzz, both with FizzBuzz


number = int(input("Enter your number: " ))


if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("Buzz")
elif number %  3 ==0:
        print("Fizz")
else:
    print(number)
