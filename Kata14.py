def remove_smallest(numbers):
    lnumber = numbers
    numbty = []
    for number in numbers:
        if numbers != lnumber:
            return "dfdsfdf  "
        else:
            number = min(numbers)
            if number in numbers:
                lnumber.remove(number)
                return numbers
print(remove_smallest([]))


# Este es el correcto

def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a
print(remove_smallest([]))
 
