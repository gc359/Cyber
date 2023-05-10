def cipher_break(text, shift):
    """
    Decrypts the given string using a Caesar Cipher with the given shift.

    Parameters:
    text (str): The string to decrypt.
    shift (int): The number of positions to shift the characters back.

    Returns:
    str: The decrypted string.
    """

    # Create an empty string to hold the decrypted message
    result = ""

    # Loop through each character in the text
    for char in text:

        # If the character is an uppercase letter
        if char.isupper():
            # Shift the character back by the given amount and wrap around if necessary
            result += chr((ord(char) - shift - 65) % 26 + 65)

        # If the character is a lowercase letter
        elif char.islower():
            # Shift the character back by the given amount and wrap around if necessary
            result += chr((ord(char) - shift - 97) % 26 + 97)

        # If the character is not a letter, leave it as is
        else:
            result += char

    # Return the decrypted message
    return result

encrypted_text = "Khoor, Zruog!"
decrypted_text = cipher_break(encrypted_text, 3)
print(decrypted_text)  # prints "Hello, World!"
