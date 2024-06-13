import sqlite3


# Luhn's Algorithm checksum function
def checksum(credit_card):
    #credit card number sent as a string
    credit_card = str(credit_card)[::-1]
    total = 0

    ## Luhn's Algorithm
    for i, digit in enumerate(credit_card):
        digit = int(digit)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9 
        total += digit
    
    return total % 10 == 0

# card_type function
def card_type(credit_card):
    
    if len(credit_card) == 13:
        if credit_card[0] == '4':
            return 'VISA'
        return 0
    
    if len(credit_card) == 16:
        if credit_card[0] == '4':
            return ('VISA')
        if 51 <= int(credit_card[0:2]) <= 55:
            return ('MASTERCARD')
        if 2221 <= int(credit_card[0:4]) <= 2720:
            return 'MASTERCARD'
        return 0

    if len(credit_card) == 15:
        if credit_card[0:2] in ('34', '37'):
            return 'AMEX'
        return 0
    return 0
