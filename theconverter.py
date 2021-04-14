class The_Converter():

    def ascii(self, ascii_code: int, logger):
        """
        Handles the command to convert an integer within ASCII code to an ASCII character.
        """

        print("Checking number...")
        logger.info("Checking number...")
        if ValueError:
            print(f"{ascii_code} is either not within range, or is not an integer.")
            logger.info(f"{ascii_code} is either not within range, or is not an integer.")
            print("To continue, give me a number between 0 and 1,114,111.")
            logger.info("To continue, give me number between 0 and 1,114,111.")

        else:
            print("Converting integer...")
            logger.info("Converting integer...")
            chango = chr(ascii_code)
            print(chango)
            logger.info(chango)

    def bytes(self, number: int, logger):
        """
        Handles the command to convert an integer to a bytes object.
        """

        print("Converting integer...")
        logger.info("Converting integer...")
        cadabra = bytes(number)
        print(cadabra)
        logger.info(cadabra)

    def hexadecimal(self, number: int, logger):
        """
        Handles the command to convert an integer to a string object containing two hexadecimal
        digits.
        """

        print("Converting integer...")
        logger.info("Converting integer...")
        pocus = hex(number)
        print(pocus)
        logger.info(pocus)
