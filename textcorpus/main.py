import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "text_corpus_alfa.txt")) as f:
    alfa = [word.rstrip('\r\n ') for word in f.readlines() if word != ""]

with open(os.path.join(dir_path, "text_corpus_bravo.txt")) as f:
    bravo = [word.rstrip('\r\n ') for word in f.readlines() if word != ""]

with open(os.path.join(dir_path, "text_corpus_charlie.txt")) as f:
    charlie = [word.rstrip('\r\n ') for word in f.readlines() if word != ""]

with open(os.path.join(dir_path, "text_corpus_delta.txt")) as f:
    delta = [word.rstrip('\r\n ') for word in f.readlines() if word != ""]

with open(os.path.join(dir_path, "text_corpus_echo.txt")) as f:
    echo = [word.rstrip('\r\n ') for word in f.readlines() if word != ""]

all_corpora = alfa + bravo + charlie + delta + echo


def understand_text(message: str):
    """
    """

    if any(word in message for word in all_corpora):

        return f"I do. What would you like to know?"

    else:

        return f"I do not."
