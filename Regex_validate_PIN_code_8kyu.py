import re
def validate_pin(pin):
    return False if re.findall("\D",pin) or len(pin) != 6 and len(pin) != 4 else True



print(validate_pin("12345 "))


