import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "text_corpus_alfa.txt")) as f:
    alfa = [word.rstrip('\r\n ') for word in f.readlines() if word != ""]

with open(os.path.join(dir_path, "text_corpus_bravo.txt")) as f:
    bravo = [word.rstrip('\r\n ') for word in f.readlines() if word != ""]

all_corpora = alfa + bravo


def get_text(message: str):
    """
    """

    if any(word in message for word in all_corpora):

        return f"{message} was found, i.e. it is a basic or common word."

    else:
        return f"{message} was not found, i.e. it is not a basic or common word."
