function caesarCipher(text, shift) {
    // Encrypts the given string using a Caesar Cipher with the given shift.
  
    // Parameters:
    // text (str): The string to encrypt.
    // shift (int): The number of positions to shift the characters.
  
    // Returns:
    // str: The encrypted string.
  
    // Create an empty string to hold the encrypted message
    let result = "";
  
    // Loop through each character in the input string
    for (let i = 0; i < text.length; i++) {
      let char = text[i];
  
      // If the character is an uppercase letter
      if (/[A-Z]/.test(char)) {
        // Shift the character by the given amount and wrap around if necessary
        let shiftedCode = ((char.charCodeAt() - 65 + shift) % 26 + 65);
        let shiftedChar = String.fromCharCode(shiftedCode);
        result += shiftedChar;
  
      // If the character is a lowercase letter
      } else if (/[a-z]/.test(char)) {
        // Shift the character by the given amount and wrap around if necessary
        let shiftedCode = ((char.charCodeAt() - 97 + shift) % 26 + 97);
        let shiftedChar = String.fromCharCode(shiftedCode);
        result += shiftedChar;
  
      // If the character is not a letter, leave it as is
      } else {
        result += char;
      }
    }
  
    // Return the encrypted message
    return result;
  }

let encryptedText = caesarCipher("Hello, World!", 3);
console.log(encryptedText);  // prints "Khoor, Zruog!"
