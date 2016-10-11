def validate_num(number):
    """Helper function to validate number of questions the user wants in the quiz."""
    if number <= 0:
        new_num = int(raw_input("Oops, your number has to be greater than 0. Please pick again: "))
        return validate_num(new_num)
    else:
        return number

def set_qs():
    """Starts game flow and sets number of questions"""

    print "Hi there! We're going to give you a fun grammar quiz."

    user_name = raw_input("To start, please enter your name: ")

    print "Thanks, {}!".format(user_name)

    user_num = int(raw_input("How many questions would you like us to generate for you? Enter a number: "))

    num_qs = validate_num(user_num)

    print "Ok, we'll make you a quiz with {} questions!".format(num_qs)

    return num_qs

set_qs()
