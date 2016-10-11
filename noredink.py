import random
from collections import defaultdict

"""Notes for reviewer:
This challenge was really fun to think about and complete! Thanks for creating an assignment
that is comprehensive, and not your typical Hackerrank problem :).

I tried to substitute working code here for perfection, given the time limit. I also tried to
break up my code into logical pieces as much as possible, to set a clear path for unit / integration
testing later.

If I had more time,
some things I would do to improve my code (in addition / compliment to the bonus work):

-Make some more helper functions to move duplicative logic out of main routes (e.g., the random
    assignment / creation of a "winners" dictionary could be a helper function)

-Write unit and integration tests for helper and main functions

-I would order the questions from easiest to hardest by leveraging my questions dictionary -
instead of a list of ids, the question_ids list could be a list of tuples, and sort on difficulty

-Similarly, this approach could be taken to group by both standard and difficulty, since the questions
list already initiates itself standard by standard. I am envisioning a list of lists of tuples perhaps -
where the entire list contains lists of a standard id and then lists of tuples, for example:
questions = [[standard_id, [(question_tuple), (question_tuple), (question_tuple)]], and so on

-I would parse the data from CSV! I have been reading on how to do this but decided to save it as an 
"extra" due to time.

Thanks so much for the opportunity!

"""


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


def pick_standards(strand_info):
    """Takes in strand info from pick_strands function, returns new list of tuples with standard ids
        and number of questions for each"""

    standard_info = []

    # goes through each item (aka strand) and looks at the standards available to it and how many questions
    # that strand is supposed to get. if it can divide q's evenly, it does.
    # otherwise, it goes through the "remainder" it can't evenly divide and picks a random winner until remainder
    # is all allocated. Popping the "winner" out of the choices list each time ensures no item is overrepresented

    for item in strand_info:
        strand_id = item[0]
        count = item[1]
        options = strands[strand_id]["Standards"]
        if not count % len(options):
            for standard in options:
                standard_info.append((standard, count / len(options)))
        else:
            remainder = count % len(options)
            winners = defaultdict(int)
            while remainder:
                choices = options[:]
                winner = random.choice(choices)
                choices.pop(choices.index(winner))
                winners[winner] += 1
                remainder -= 1
            for standard in options:
                standard_info.append((standard, count / len(options) + winners[standard]))

    return standard_info

def pick_questions(standard_info):
    """Goes through standard info input and returns question ids"""

    questions = []

    # goes through each item in the standard into
    for item in standard_info:
        standard_id = item[0]
        count = item[1]
        options = standards[standard_id]["Questions"]
        # if the questions you have allocated to that standard are less than the amount
        # of questions that standard technically has to offer, just add the amount you are able to
        if count < len(options):
            available = options[:count]
            questions.extend(available)
        # alternatively, if the number you have allocated to that standard is exactly equal to the amount
        # of q's that standard has, just "divide evenly" and put all the questions in once
        elif count == len(options):
            questions.extend(options)
        # if you have more questions allocated to that standard than you have questions available, duplicate!
        elif len(options) < count:
            if not count % len(options):
                to_add = options * (count / len(options))
                questions.extend(to_add)
            else:
                to_add = options * (count / len(options))
                questions.extend(to_add)
                remainder = count % len(options)
                winners = defaultdict(int)
                while remainder:
                    choices = options[:]
                    winner = random.choice(choices)
                    choices.pop(choices.index(winner))
                    winners[winner] += 1
                    remainder -= 1
                for q in options:
                    print q
                    for i in range(1, winners[q] + 1):
                        questions.append(q)
                        print questions

    return questions



quiz_length = set_qs()
strand_info = pick_strands(quiz_length)
standard_info = pick_standards(strand_info)
questions = pick_questions(standard_info)
print "Here are your question IDs! {}".format(questions)
