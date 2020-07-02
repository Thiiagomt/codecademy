# These are the emails you will be censoring. The open() function is opening the text file that the emails are
# contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# Lists
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "herself",
                     "her"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]
big_list = proprietary_terms + negative_words


# Function censor a word from text
def censor_word(word, text):
    if text.find(word):
        text = text.replace(word, "*" * len(word))
        return text
    else:
        return text


# Function censor a list of words from text
def censor_list(words_list, text):
    for word in words_list:
        text = censor_word(word, text)
    return text


# Function censor a list of negative words and other list with some words from text
def censor_negative_words(negative_list, words_list, text):
    count = 0
    for word in negative_list:
        if text.find(word):
            count += 1
        if count >= 2:
            text = censor_word(word, text)
    for word in words_list:
        text = censor_word(word, text)
    return text


# Function censor before and after a word from list appear from text
def censor_all(words_list, text):
    all_words = text.split(' ')

    i = 0
    while i < len(all_words):
        for word in words_list:
            if word == all_words[i]:
                all_words[i] = "*" * len(all_words[i])
                all_words[i - 1] = "*" * len(all_words[i - 1])
                all_words[i + 1] = "*" * len(all_words[i + 1])
        i += 1

    text = ' '
    text = text.join(all_words)
    return text
