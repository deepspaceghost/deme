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
]

names = [
    "Deme", "deme"
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

help_command = commands.DefaultHelpCommand(no_category="Commands")
bot = commands.Bot(command_prefix="!", help_command=help_command)


class languageProcessing():
    """
    """

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
        This function listens for phrases of gratitude.
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
