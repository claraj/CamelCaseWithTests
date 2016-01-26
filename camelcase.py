

def main():

    sentence = get_user_input()


    # validate sentence  - -check for invalid chars or numbers
    # put this into function - test the sentence is split into words correctly?

    words = split(sentence)

    methodName = ""

    first_word_done = False

    for word in words:

        if not first_word_done:
            camel = first_word(word)
            first_word_done = True

        else:
            camel = camelcase_word(word)

        methodName += camel

    display_output(methodName)


def get_user_input():

    return input("Enter sentence")


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

