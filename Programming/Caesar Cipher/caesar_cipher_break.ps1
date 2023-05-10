function cipher_break($text, $shift) {
  # Decrypts the given string using a Caesar Cipher with the given shift.

  # Parameters:
  # $text (str): The string to decrypt.
  # $shift (int): The number of positions to shift the characters back.

  # Returns:
  # str: The decrypted string.

  # Create an empty string to hold the decrypted message
  $result = ""

  # Loop through each character in the input string
  foreach ($char in $text.ToCharArray()) {

    # If the character is an uppercase letter
    if ($char -cmatch '[A-Z]') {
      # Shift the character back by the given amount and wrap around if necessary
      $shifted_code = (([int]$char - 65 - $shift + 26) % 26 + 65)
      $shifted_char = [char]$shifted_code
      $result += $shifted_char

    # If the character is a lowercase letter
    elseif ($char -cmatch '[a-z]') {
      # Shift the character back by the given amount and wrap around if necessary
      $shifted_code = (([int]$char - 97 - $shift + 26) % 26 + 97)
      $shifted_char = [char]$shifted_code
      $result += $shifted_char

    # If the character is not a letter, leave it as is
    else {
      $result += $char
    }
  }

  # Return the decrypted message
  return $result
}

$encrypted_text = caesar_cipher "Hello, World!" 3
$decrypted_text = cipher_break $encrypted_text 3
Write-Host $decrypted_text  # prints "Hello, World!"
