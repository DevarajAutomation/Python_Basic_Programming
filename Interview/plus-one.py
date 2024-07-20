def plus_one(digits):
    for i in range(reversed(len(digits))):
        if digits[i] !=9:
            digits[i] +=1
            return digits
        digits[i]=0

    return 1+digits

