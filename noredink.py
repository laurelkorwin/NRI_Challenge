import random

# hard-coded data for now
# initial thought is that separating strands, standards and q's will make it
# easier to interact with each to ensure even distribution
strands = {1: {"Name": "Nouns", "Standards": [1, 2, 3]},
           2: {"Name":"Verbs", "Standards": [4, 5, 6]}}

standards = {1: {"Name": "Common Nouns", "Questions": [1, 2]},
             2: {"Name": "Abstract Nouns", "Questions": [3]},
             3: {"Name": "Proper Nouns", "Questions": [4, 5, 6]},
             4: {"Name": "Action Verbs", "Questions": [7, 8]},
             5: {"Name": "Transitive Verbs", "Questions": [9, 10, 11]},
             6: {"Name": "Reflexive Verbs", "Questions": [12]}}

# dictionary of question id / difficulty key/value pairs
questions = {1: 0.7, 2: 0.6, 3: 0.8, 4: 0.2, 5: 0.5, 6: 0.4, 7: 0.9, 8: 0.1, 9: 0.3,
             10: 0.6, 11: 0.4, 12: 0.2}


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

def pick_strands(quiz_len):
    """Takes in quiz length and determines proportion of q's allocated to each strand
        Returns a list of tuples representing strand id and num questions for each"""

    strand_info = []

    # checks how many strands there are and sees if the quiz can be evenly divided between them
    # if the num_strands evenly goes into the quiz, you can divide q's evenly
    num_strands = len(strands.keys())
    if not quiz_len % num_strands:
        for key in strands.keys():
            strand_info.append((key, quiz_len / num_strands))
    # assigns "leftover" value to a random strand - note, currently, this works for two strands only
    # need to adjust to have it be dynamic based on how big the remainder is
    else:
        # remainder = quiz_len % num_strands
        winner = random.choice(strands.keys())
        for key in strands.keys():
            if key == winner:
                strand_info.append((key, quiz_len / num_strands + 1))
            else:
                strand_info.append((key, quiz_len / num_strands))

    return strand_info




quiz_length = set_qs()
strand_info = pick_strands(quiz_length)
