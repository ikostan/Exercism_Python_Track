def response(hey_bob):
    """
    Bob is a lackadaisical teenager. In conversation,
    his responses are very limited.

    Bob answers 'Sure.' if you ask him a question,
    such as "How are you?".

    He answers 'Whoa, chill out!' if you
    YELL AT HIM (in all capitals).

    He answers 'Calm down, I know what I'm doing!'
    if you yell a question at him.

    He says 'Fine. Be that way!' if you address him
    without actually saying anything.

    He answers 'Whatever.' to anything else.

    Bob's conversational partner is a purist
    when it comes to written communication
    and always follows normal rules regarding sentence
    punctuation in English.
    :param hey_bob:
    :return:
    """

    if hey_bob is None or hey_bob.strip() == '':
        # He says 'Fine. Be that way!' if you address
        # him without actually saying anything.
        return 'Fine. Be that way!'

    if hey_bob.isupper():
        # He answers 'Calm down, I know what I'm doing!'
        # if you yell a question at him.
        if '?' in hey_bob:
            return 'Calm down, I know what I\'m doing!'
        # He answers 'Whoa, chill out!' if you
        # YELL AT HIM (in all capitals).
        return 'Whoa, chill out!'

    if '?' == hey_bob.strip()[-1]:
        # Bob answers 'Sure.' if you ask him a question,
        # such as "How are you?".
        return 'Sure.'

    # He answers 'Whatever.' to anything else.
    return 'Whatever.'
