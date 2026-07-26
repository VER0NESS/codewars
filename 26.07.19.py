regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]{6,}$"
regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]{6,}$"

                # min 6 chars
                #lowercase
                #uppercase
                #digit
                #only contains alphanumeric characters without _

    # r only reading for str
    # ^ starts the adress
    # . any symbols excepts new line
    # @ literal symbol
    # + 1 or more of any symbols from left
    # \ to see next symbols not special but literally
    # .com are seeing by interpreter literally
    # $ end of the address so nothing can be further