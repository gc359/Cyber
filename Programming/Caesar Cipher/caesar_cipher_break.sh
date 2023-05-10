cipher_break() {
  # Decrypts the given string using a Caesar Cipher with the given shift.

  # Parameters:
  # $1 (str): The string to decrypt.
  # $2 (int): The number of positions to shift the characters back.

  # Returns:
  # str: The decrypted string.

  # Get the input string and shift amount from the function parameters
  text="$1"
  shift_amount="$2"

  # Create an empty string to hold the decrypted message
  result=""

  # Loop through each character in the input string
  for (( i=0; i<${#text}; i++ )); do
    char="${text:$i:1}"

    # If the character is an uppercase letter
    if [[ $char =~ [A-Z] ]]; then
      # Shift the character back by the given amount and wrap around if necessary
      char_code=$(printf '%d' "'$char")
      shifted_code=$(((char_code - 65 - shift_amount + 26) % 26 + 65))
      shifted_char=$(printf \\$(printf '%03o' $shifted_code))
      result+="$shifted_char"

    # If the character is a lowercase letter
    elif [[ $char =~ [a-z] ]]; then
      # Shift the character back by the given amount and wrap around if necessary
      char_code=$(printf '%d' "'$char")
      shifted_code=$(((char_code - 97 - shift_amount + 26) % 26 + 97))
      shifted_char=$(printf \\$(printf '%03o' $shifted_code))
      result+="$shifted_char"

    # If the character is not a letter, leave it as is
    else
      result+="$char"
    fi
  done

  # Return the decrypted message
  echo "$result"
}

encrypted_text=$(caesar_cipher "Hello, World!" 3)
decrypted_text=$(cipher_break "$encrypted_text" 3)
echo "$decrypted_text"  # prints "Hello, World!"
