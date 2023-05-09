function caesar_cipher($text, $shift) {
  # Encrypts the given string using a Caesar Cipher with the given shift.

  # Parameters:
  # $text (str): The string to encrypt.
  # $shift (int): The number of positions to shift the characters.

  # Returns:
  # str: The encrypted string.

  # Create an empty string to hold the encrypted message
  $result = ""

  # Loop through each character in the input string
  foreach ($char in $text.ToCharArray()) {

    # If the character is an uppercase letter
    if ($char -cmatch '[A-Z]') {
      # Shift the character by the given amount and wrap around if necessary
      $shifted_code = (([int]$char - 65 + $shift) % 26 + 65)
      $shifted_char = [char]$shifted_code
      $result += $shifted_char

    # If the character is a lowercase letter
    elseif ($char -cmatch '[a-z]') {
      # Shift the character by the given amount and wrap around if necessary
      $shifted_code = (([int]$char - 97 + $shift) % 26 + 97)
      $shifted_char = [char]$shifted_code
      $result += $shifted_char

    # If the character is not a letter, leave it as is
    else {
      $result += $char
    }
  }

  # Return the encrypted message
  return $result
}

$encrypted_text = caesar_cipher "Hello, World!" 3
Write-Host $encrypted_text  # prints "Khoor, Zruog!"
