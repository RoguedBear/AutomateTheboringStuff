def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result


# Enter number to begin
while True:
    try:
        number = int(input("Enter number:\n"))
        break
    except ValueError:
        print("Enter an integer plez.")
        continue

while True:
    result = collatz(number)
    if result == 1:
        break
    else:
        number = result
