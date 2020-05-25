# not blank function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in the string and if it's a number
            for letter in response:
                if letter.isdigit():
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# main routine goes here

item_amount = not_blank("How many of your selected item are you wanting? ",
                        "Your response cannot have numbers or be blank",
                        "yes")

print("you chose {} or your selected item".format(item_amount))


