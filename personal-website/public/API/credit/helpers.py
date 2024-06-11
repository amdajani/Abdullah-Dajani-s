# initlizae the dataset to include user_id from 
# the session, credit_card_hashed, card_type



# Luhn's Algorithm checksum function
def checksum(credit_card):
    #credit card number sent as a string
    credit_card = str(credit_card)[::-1]
    sum = 0

    ## Luhn's Algorithm
    for i, digit in enumerate(credit_card):
        digit = int(digit)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9 
        sum += digit
    
    return sum % 10 == 0

# card_type function
def card_type(credit_card):
    return 1