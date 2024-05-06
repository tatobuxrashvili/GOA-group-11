"""https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python"""

def validate_pin(pin):
    if len(pin) == 4:
        try:
            for n in pin:
                num = int(n)
            return True
        except:
            return False
    elif len(pin) == 6:
        try:
            for n in pin:
                num = int(n)
            return True
        except:
            return False
    else:
        return False
