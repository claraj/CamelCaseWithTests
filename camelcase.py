import re


def main():

    sentence = get_user_input()

    if not valid_sentence(sentence):
        print("Can't process this input")
        return

    words = split(sentence)

    method_name = ""

    first_word_done = False

    for word in words:

        if not first_word_done:
            camel = first_word(word)
            first_word_done = True

        else:
            camel = camelcase_word(word)

        method_name += camel

    display_output(method_name)


def get_user_input():
    return input("Enter sentence")


def valid_sentence(sentence):
    """Writing this method over restrictive-- just the ASCII valid variable characters a-z, A-Z, _, and 0-9
    https://docs.python.org/3/reference/lexical_analysis.html#identifiers
    link explains that python 3 allows non-ASCII unicode
    :param sentence str
    :return bool
    """
    for i, ch in enumerate(sentence):
        if i == 1:
            if not re.match(r'([a-zA-Z_ ])', ch):
                return False
        else:
            if not re.match(r'([a-zA-Z_ 0-9])', ch):
                return False
    return True


def display_output(output):
    print(output)


def split(words):
    return words.split()


def first_word(word):
    return word.lower()


def camelcase_word(word):
    inlowercase = word.lower()
    firstletter = word[0]
    firstletter = firstletter.upper()
    rest_of_word = inlowercase[1:]

    camelcased = firstletter + rest_of_word

    return camelcased


if '__name__ ' == '__main__':
    main()
