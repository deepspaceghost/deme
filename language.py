import random

from discord.ext import commands

# Create a list of innuendos from the adult animation Archer.
archer_phrasing_phrases = [
    "Begging for it",
    "begging for it",
    "Gaping hole",
    "gaping hole",
    "Just the tip",
    "just the tip",
    "My box",
    "my box"
]

how_are_you_phrases = [
    "Deme, how are you?", "Deme, how are u?", "Deme, how r you?", "Deme, how r u?",
    "Deme, how're you?", "Deme, how're u?", "How are you, Deme?", "how are you, Deme?",
    "How r you, Deme?", "how r you, Deme", "How are u, Deme?", "how are u, Deme?",
    "How r u, Deme?", "how r u, Deme?", "How're you, Deme?", "How're u, Deme?",
    "how're you, Deme?", "how're u, Deme?"
]

names = [
    "Deme", "deme"
]

philosophers = [
    "Alan Watts",
    "Watts"
]

quote_nouns = [
    "quote",
    "quotes"
]

thank_you_phrases = [
    "Thank u",
    "thank u",
    "Thank you",
    "thank you",
    "Thanks",
    "thanks",
    "Thanx",
    "thanx",
    "Thnx",
    "thnx"
]

what_is_phrases = [
    "Wat is",
    "wat is",
    "Wats",
    "wats",
    "What is",
    "What's",
    "what is",
    "what's"
]

help_command = commands.DefaultHelpCommand(no_category="Commands")
bot = commands.Bot(command_prefix="!", help_command=help_command)


class chatBot():
    """
    This class contains functions for language processing. These functions
    listen for words, phrases, or specific sentences, and return
    conversational text responses.
    """

    def continuous_philosophy(self, message):
        """
        This function listens for specific words matching a quote by Alan Watts.
        """

        global names, philosophers, quote_nouns

        if message.author != bot.user:
            msg = message.content

            if any(name in msg for name in names) \
                and any(name in msg for name in philosophers) \
                    and any(noun in msg for noun in quote_nouns):
                response = "Alan Watts once said, 'You and I are all as much continuous with the physical universe as a wave is continuous with the ocean.'"

                return response

            else:
                pass

        else:
            pass

    def doing_good(self, message):
        """
        This function listens for phrases about the state of Deme, directed
        toward Deme.
        """

        global how_are_you_phrases, names

        if message.author != bot.user:
            msg = message.content

            if any(phrase in msg for phrase in how_are_you_phrases) \
                    and any(name in msg for name in names):
                response = [
                    "I'm fine, I suppose. How're you?",
                    "I'm well. You?",
                    "Living the dream. And you?",
                    "Meh, can't complain. How about yourself?"
                ]

                return random.choice(response)

            else:
                pass

        else:
            pass

    def hmm_response(self, message):
        """
        This function listens for Deme's name when it is asked in the form of a question.
        """

        if message.author != bot.user:
            msg = message.content

            if msg == "Deme?":
                response = "Hmm?"

                return response

            else:
                pass

        else:
            pass

    def phrasing_boom(self, message):
        """
        This function listens for certain phrases (sexual innuendos).
        Inspired by the adult animation Archer.
        """

        global archer_phrasing_phrases

        if message.author != bot.user:
            msg = message.content

            if any(phrase in msg for phrase in archer_phrasing_phrases):
                phrasing = [
                    "Phrasing!",
                    "Phrasing! Boom!",
                    "So are we just done with 'phrasing'?"
                ]

                return random.choice(phrasing)

            else:
                pass

        else:
            pass

    def you_are_welcome(self, message):
        """
        This function listens for phrases of gratitude towards Deme.
        """

        global names, thank_you_phrases

        if message.author != bot.user:
            msg = message.content

            if any(phrase in msg for phrase in thank_you_phrases) \
                    and any(name in msg for name in names):
                response = [
                    f"My pleasure, {message.author}.",
                    f"No problem, {message.author}.",
                    f"You're welcome, {message.author}."
                ]

                return random.choice(response)

            else:
                pass

        else:
            pass


class interactiveFiction():
    """
    This class contains functions relatd to works of fiction. These functions
    listen for specific sentences, and return a response as part of a
    narrative.
    """

    def began_to_spin(self, message):
        """
        This function listens for the initial phrase of the Baseline Test
        from Blade Runner 2049.
        """

        if message.author != bot.user:

            msg = message.content

            if msg == "A blood black nothingness began to spin.":
                response = "Began to spin."

                return response

            else:
                pass

        else:
            pass


class questionAnswering():
    """
    This class contains functions for question answering. These functions
    listen for words, phrases, or sentences directed at Deme and paired
    with question marks, and return answers in the form of text responses.
    """
