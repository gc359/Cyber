def caesar_cipher(text, shift)
    # Encrypts the given string using a Caesar Cipher with the given shift.
  
    # Parameters:
    # text (str): The string to encrypt.
    # shift (int): The number of positions to shift the characters.
  
    # Returns:
    # str: The encrypted string.
  
    # Create an empty string to hold the encrypted message
    result = ""
  
    # Loop through each character in the input string
    text.each_char do |char|
  
      # If the character is an uppercase letter
      if /[A-Z]/.match?(char)
        # Shift the character by the given amount and wrap around if necessary
        shifted_code = ((char.ord - 65 + shift) % 26 + 65)
        shifted_char = shifted_code.chr
        result += shifted_char
  
      # If the character is a lowercase letter
      elsif /[a-z]/.match?(char)
        # Shift the character by the given amount and wrap around if necessary
        shifted_code = ((char.ord - 97 + shift) % 26 + 97)
        shifted_char = shifted_code.chr
        result += shifted_char
  
      # If the character is not a letter, leave it as is
      else
        result += char
      end
    end
  
    # Return the encrypted message
    return result
  end

encrypted_text = caesar_cipher("Hello, World!", 3)
puts encrypted_text  # prints "Khoor, Zruog!"
