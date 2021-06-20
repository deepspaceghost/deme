import random
import time

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


class languageProcessing():
    """
    This class contains functions for language processing. These functions
    listen for words, phrases, or specific sentences, and return
    conversational text responses.
    """

    def continuous_philosophy(self, message):
        """
        This function listens for specific words matching a quote by Alan Watts.
        """

        global philosophers, quote_nouns

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
                you_are_welcome = [
                    f"My pleasure, {message.author}.",
                    f"No problem, {message.author}.",
                    f"You're welcome, {message.author}."
                ]

                return random.choice(you_are_welcome)

            else:
                pass

        else:
            pass


class lieDetector():
    """
    This class contains functions for "lie detection". These functions
    listen for specific sentences, and return the corresponding response
    given by the replicants in the films. Inspired by Philip K. Dick's
    Blade Runner.
    """

    def began_to_spin(self, message):
        """
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
