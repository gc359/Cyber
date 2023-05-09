def caesar_cipher(text, shift):
    """
    Encrypts the given string using a Caesar Cipher with the given shift.

    Parameters:
    text (str): The string to encrypt.
    shift (int): The number of positions to shift the characters.

    Returns:
    str: The encrypted string.
    """

    # Create an empty string to hold the encrypted message
    result = ""

    # Loop through each character in the text
    for char in text:

        # If the character is an uppercase letter
        if char.isupper():
            # Shift the character by the given amount and wrap around if necessary
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # If the character is a lowercase letter
        elif char.islower():
            # Shift the character by the given amount and wrap around if necessary
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # If the character is not a letter, leave it as is
        else:
            result += char

    # Return the encrypted message
    return result

encrypted_text = caesar_cipher("Hello, World!", 3)
print(encrypted_text)  # prints "Khoor, Zruog!"
