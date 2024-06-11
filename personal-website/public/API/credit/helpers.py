# initlizae the dataset to include user_id from 
# the session, credit_card_hashed, card_type



# Luhn's Algorithm checksum function

#make sure to check if it's greater than a certain threshold
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
    return 1

'''card_type = card_type(credit_card)

    user_id = session["user_id"]
    if user_id:
        db = sqlite3.connect
        cursor = db.cursor()
        db.execute("INSERT INTO credit_log (user_id, credit_card, card_type) VALUES (?, ?, ?)", user_id, int(credit_card), card_type)
        db.commit()
        db.close'''