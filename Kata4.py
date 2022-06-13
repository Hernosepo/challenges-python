def high_and_low(numbers):
    for number in numbers:
        numbers = numbers.split(" ")
        number = [int(number) for number in numbers]
        number = sorted(number, reverse= True)]['{}  {}'.format(number[0], number[-1])]
        return number
print(high_and_low("1 2 3 4 5"))
